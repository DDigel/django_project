"""
URL configuration for apple_world project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import render
from users import views as user_views, views

def home(request):
    context = {
        'welcome_message': 'Добро пожаловать в Apple World!',
        'categories': [
            {'name': 'iPhone', 'url': '/category/1'},
            {'name': 'Watch', 'url': '/category/2'},
            {'name': 'Airpods', 'url': '/category/3'},
            {'name': 'Корзина', 'url': '/products/view_cart'},
        ],
    }
    return render(request, 'home.html', context)

urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),
    path('products/', include('products.urls')),  # Путь для Весь каталог
    path('users/', include('users.urls', namespace='users')),
    path('login/', user_views.login_view, name='login'),
    path('register/', views.register, name='register'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)