
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from student_shop import settings



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('store.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
