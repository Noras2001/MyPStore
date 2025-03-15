from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from .models import Product
from .forms import ProductForm
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

from django.core.paginator import Paginator
from django.db.models import Q
from django.utils import timezone
from datetime import timedelta
from django.http import JsonResponse




def product_list(request):
    products = Product.objects.all()
    return render(request, 'store/product_list.html', {'products': products})

@login_required(login_url='login')
@require_POST
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    cart = request.session.get('cart', {})
    cart[str(product_id)] = cart.get(str(product_id), 0) + 1
    request.session['cart'] = cart
    return redirect('product_list')

def cart(request):
    cart = request.session.get('cart', {})
    cart_items = []
    total_price = 0
    for product_id, quantity in cart.items():
        product = get_object_or_404(Product, pk=product_id)
        cart_items.append({'product': product, 'quantity': quantity})
        total_price += product.price * quantity
    return render(request, 'store/cart.html', {'cart_items': cart_items, 'total_price': total_price})

@require_POST
def clear_cart(request):
    request.session['cart'] = {}
    return redirect('cart')


def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product_list')  # После успешного добавления перенаправляем на главную
    else:
        form = ProductForm()
    return render(request, 'store/add_product.html', {'form': form})



def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Входим автоматически после регистрации
            return redirect('product_list')
    else:
        form = UserCreationForm()
    return render(request, 'store/register.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('product_list')



def product_list(request):
    products = Product.objects.all()

    # Фильтрация по категории
    category = request.GET.get('category')
    if category:
        products = products.filter(category__icontains=category)

    # Фильтрация по диапазону цен
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')
    if min_price:
        products = products.filter(price__gte=min_price)
    if max_price:
        products = products.filter(price__lte=max_price)

    # Фильтрация по дате добавления (например, за последние N дней)
    last_days = request.GET.get('last_days')
    if last_days:
        try:
            days = int(last_days)
            date_threshold = timezone.now() - timedelta(days=days)
            products = products.filter(date_added__gte=date_threshold)
        except ValueError:
            pass

    # Сортировка
    sort_by = request.GET.get('sort_by')
    sort_order = request.GET.get('sort_order', 'asc')
    ordering = None
    if sort_by == 'popularity':
        ordering = 'orders_count'
    elif sort_by == 'price':
        ordering = 'price'
    elif sort_by == 'date':
        ordering = 'date_added'
    if ordering:
        if sort_order == 'desc':
            ordering = '-' + ordering
        products = products.order_by('-date_added')  # сортировка по дате добавления (от новых к старым)

    # Пагинация: 10 товаров на страницу
    paginator = Paginator(products, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # Если запрос AJAX, возвращаем данные в формате JSON
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        products_list = []
        for product in page_obj:
            products_list.append({
                'name': product.name,
                'price': str(product.price),
                'category': product.category,
                'date_added': product.date_added.strftime('%Y-%m-%d'),
                'orders_count': product.orders_count,
            })
        data = {
            'products': products_list,
            'page_number': page_obj.number,
            'num_pages': paginator.num_pages,
        }
        return JsonResponse(data)

    return render(request, 'store/product_list.html', {'page_obj': page_obj})

