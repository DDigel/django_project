from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class NewUserForm(forms.Form):
    username = forms.CharField(max_length=150, label="Имя пользователя")
    password = forms.CharField(widget=forms.PasswordInput, label="Пароль")
    password2 = forms.CharField(widget=forms.PasswordInput, label="Подтверждение пароля")

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("Пользователь с данным именем пользователя уже зарегистрирован!")
        return username

    def clean(self):
         cleaned_data = super().clean()
         password = cleaned_data.get("password")
         password2 = cleaned_data.get("password2")

         if password and password2:
             if password != password2:
                 raise ValidationError("Пароли не совпадают")
        
         return cleaned_data
    
    def save(self):
        username = self.cleaned_data["username"]
        password = self.cleaned_data["password"]
        user = User.objects.create_user(username=username, password=password)
        return user

class PasswordResetRequestForm(forms.Form):
    email = forms.EmailField(
        label="Email",
        widget=forms.TextInput(attrs={'placeholder': 'Введите ваш email'})
    )