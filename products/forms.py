from django import forms
from django.core.exceptions import ValidationError

class OrderForm(forms.Form):
    full_name = forms.CharField(label="ФИО", max_length=255)
    email = forms.EmailField(label="Email")
    address = forms.CharField(label="Адрес доставки", widget=forms.Textarea)
    phone_number = forms.CharField(label="Номер телефона", max_length=20)

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        if not phone_number:
            return phone_number
        if not any([
            phone_number.startswith('+375')
        ]):
            raise ValidationError("Неверный формат номера телефона. Номер должен начинаться с +375")
        if len(phone_number) != 13:
            raise ValidationError("Неверный формат номера телефона. Номер должен содержать 13 символов")
        
        return phone_number