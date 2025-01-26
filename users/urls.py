from django.urls import path
from . import views
from django.contrib.auth.views import PasswordResetView

app_name = 'users'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('password_reset/', PasswordResetView.as_view(), name='password_reset'),
]