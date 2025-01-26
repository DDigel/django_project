# Create your views here.
from django.shortcuts import render, redirect
from django.urls import path
from . import views
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.db.models import Q
from django.db import IntegrityError
from datetime import timedelta
from django.conf import settings
from django.contrib.auth.decorators import login_required
from .forms import NewUserForm
from users.models import UserProfile


app_name = 'users'

# Регистрация
def register(request):
    if request.method == 'POST':
        form = NewUserForm(request.POST)  # Используем NewUserForm
        if form.is_valid():
            try:
                user = form.save()  # Сохраняем пользователя через save метод нашей формы
                user.backend = 'django.contrib.auth.backends.ModelBackend'
                login(request, user)
                messages.success(request, 'Регистрация прошла успешно!')
                return redirect('products:product_list')
            except IntegrityError:
                messages.error(request, 'Пользователь с данным именем пользователя уже существует!')
                return render(request, 'users/register.html', {'form': form})
        else:
            return render(request, 'users/register.html', {'form': form})
    else:
        form = NewUserForm()  # Используем NewUserForm
    return render(request, 'users/register.html', {'form': form})

# Авторизация
def login_view(request):
    # Если пользователь уже авторизован, перенаправляем на главную страницу
    if request.user.is_authenticated:
        return redirect('products:product_list')

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)

            # Настраиваем сессию
            if request.POST.get('remember_me'):
                request.session.set_expiry(1209600)  # 2 недели
            else:
                request.session.set_expiry(0)  # До закрытия браузера

            messages.success(request, f'Добро пожаловать, {user.username}!')
            return redirect('products:product_list')
        else:
            messages.error(request, 'Неверный логин или пароль.')
    else:
        form = AuthenticationForm()

    return render(request, 'users/login.html', {'form': form})

# Выход
def logout_view(request):
    logout(request)
    messages.success(request, 'Вы вышли из системы!')
    return redirect('products:product_list')

# Профиль
def profile(request):
    return render(request, 'users/profile.html')

@login_required
def profile_view(request):
    user = request.user
    profile, created = UserProfile.objects.get_or_create(user=user)

    if request.method == "POST":
        user.first_name = request.POST.get("first_name")
        user.last_name = request.POST.get("last_name")
        profile.birth_date = request.POST.get("birth_date")
        user.save()
        profile.save()
        return redirect("users:profile")

    orders = user.order_set.all()  # Предполагается, что заказы связаны с пользователем
    return render(request, "users/profile.html", {"user": user, "profile": profile, "orders": orders})