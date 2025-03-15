
```markdown
# Интернет-магазин на Django

## Описание проекта

Этот проект представляет собой базовый интернет-магазин, созданный с использованием Django и PostgreSQL. В проекте реализованы следующие возможности:
- Просмотр списка товаров.
- Добавление товара в корзину (только для авторизованных пользователей).
- Очистка корзины.
- Добавление новых товаров через веб-интерфейс (форма добавления товара).
- Регистрация, авторизация и выход пользователей.

## Используемые технологии

- **Django 5.1.7**
- **PostgreSQL**
- **Python 3.12.4**
- HTML, CSS (статические файлы)

## Структура проекта

```
student_shop/              # Корневая папка проекта
├── manage.py              # Скрипт управления проектом
├── student_shop/          # Папка с настройками проекта Django
│   ├── settings.py        # Основные настройки проекта
│   ├── urls.py            # Главный URL-конфиг проекта
│   └── ...
├── store/                 # Приложение магазина
│   ├── migrations/        # Миграции для базы данных
│   │   └── __init__.py    # Пакет миграций
│   ├── templates/         # Шаблоны HTML
│   │   └── store/         # Шаблоны приложения (product_list.html, add_product.html, login.html, register.html)
│   ├── static/            # Статические файлы (CSS, изображения)
│   ├── forms.py           # Формы для работы с моделями (например, для добавления товара)
│   ├── models.py          # Модели (Product, CartItem)
│   ├── views.py           # Представления (views)
│   └── urls.py            # URL-конфигурация приложения
└── requirements.txt       # Зависимости проекта (опционально)

```

## Установка и настройка

1. **Клонируйте репозиторий:**
   ```bash
   git clone <URL_репозитория>
   ```
2. **Перейдите в папку проекта:**
   ```bash
   cd student_shop
   ```
3. **Создайте виртуальное окружение:**
   ```bash
   python -m venv venv
   ```
4. **Активируйте виртуальное окружение:**
   - На Windows:
     ```bash
     venv\Scripts\activate
     ```
   - На Linux/macOS:
     ```bash
     source venv/bin/activate
     ```
5. **Установите зависимости:**
   Если есть файл `requirements.txt`:
   ```bash
   pip install -r requirements.txt
   ```
   Если файла нет, установите необходимые пакеты:
   ```bash
   pip install django psycopg2-binary
   ```

6. **Настройте подключение к базе данных:**

   Откройте файл `student_shop/settings.py` и настройте секцию `DATABASES`:
   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.postgresql',
           'NAME': 'student_shop_db',
           'USER': 'postgres',
           'PASSWORD': 'your_password',
           'HOST': 'localhost',
           'PORT': '5432',
       }
   }
   ```

7. **Создайте базу данных PostgreSQL:**

   Создайте базу данных `student_shop_db` через PGAdmin или с помощью командной строки:
   ```sql
   CREATE DATABASE student_shop_db;
   ```

8. **Примените миграции:**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

9. **Создайте суперпользователя для админ-панели:**
   ```bash
   python manage.py createsuperuser
   ```

## Запуск проекта

Запустите сервер разработки:
```bash
python manage.py runserver
```
Перейдите в браузере по адресу [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

## Функциональные возможности

- **Просмотр товаров:**  
  На главной странице отображается список товаров с информацией о названии, описании, цене и изображении.

- **Добавление товара в корзину:**  
  Авторизованные пользователи могут добавлять товары в корзину. Для неавторизованных пользователей отображается сообщение "Авторизуйтесь для добавления в корзину".

- **Очистка корзины:**  
  Пользователи могут очищать корзину.

- **Добавление нового товара:**  
  На отдельной странице с формой можно добавить новый товар, указав название, описание, цену, изображение и категорию.

- **Регистрация и авторизация:**  
  Реализованы страницы регистрации, входа и выхода. После входа пользователя происходит перенаправление на главную страницу.

## Контакты

Если у вас возникли вопросы или предложения, пожалуйста, свяжитесь со мной:

## 🏗️ Разработчик
👤 **Nora Serdyukova**  
✉️ Email: nora.serdyukova@gmail.com  
🔗 GitHub: [Noras2001](https://github.com/Noras2001)
Этот проект является базовой реализацией интернет-магазина, которую можно расширять и улучшать. Если появятся идеи или вопросы – буду рад обсудить!



