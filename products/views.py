from django.shortcuts import get_object_or_404
from django.http import HttpResponse, JsonResponse
from .models import Product, Category
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.conf import settings
from .forms import OrderForm
from django.contrib import messages


# Отображение списка товаров
def product_list(request):
    products = Product.objects.all()
    return render(request, 'products/product_list.html', {'products': products})

# Отображение категории товаров
def category_list(request, category_id):
    products = Product.objects.filter(category=category_id)

    category_name = ""
    for choice in Product.CATEGORY_CHOICES:
        if choice[0] == category_id:
            category_name = choice[1]
            break

    return render(request, 'products/product_list.html', {'products': products, 'category_name': category_name})

# Детали товара
def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'products/product_detail.html', {'product': product})

# Добавить товар в корзину
def add_to_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    cart = request.session.get('cart', {})  # Получаем корзину из сессии
    product_price = str(product.price)

    if str(product_id) in cart:
        cart[str(product_id)]['quantity'] += 1  # Увеличиваем количество товара
    else:
        cart[str(product_id)] = {
            'name': product.name,
            'price': product_price,
            'quantity': 1,
        }

    request.session['cart'] = cart  # Сохраняем корзину обратно в сессию
    
    total_items = sum(item['quantity'] for item in cart.values()) # Подсчитываем общее количество товаров в корзине

    request.session['total_items'] = total_items # Сохраняем общее количество товаров в сессии

    return redirect('products:product_list')  # Правильный редирект на маршрут корзины

# Просмотр корзины
def view_cart(request):
    cart = request.session.get('cart', {})  # Получаем корзину
    total_price = sum(float(item['price']) * item['quantity'] for item in cart.values())  # Считаем общую цену
    return render(request, 'products/cart.html', {'cart_items': cart, 'total_price': total_price})

# Оформление заказа
def checkout(request):
    cart = request.session.get('cart', {})
    cart_items = []
    total_price = 0

    for item_id, data in cart.items():
        try:
            product = Product.objects.get(id=item_id)
            cart_items.append({
                'product': product,
                'quantity': data['quantity'],
                'total_price': float(data['price']) * data['quantity'],
            })
            total_price += float(data['price']) * data['quantity']
        except Product.DoesNotExist:
            continue

    if request.method == 'POST':
       form = OrderForm(request.POST)
       if form.is_valid():
             full_name = form.cleaned_data['full_name']
             email = form.cleaned_data['email']
             address = form.cleaned_data['address']
             phone_number = form.cleaned_data['phone_number']
             payment_method = request.POST.get('payment_method')

             # Очищаем корзину и устанавливаем cart_count здесь
             request.session['cart'] = {}
             default_cart_count = settings.DEFAULT_CART_COUNT
             request.session['cart_count'] = default_cart_count
             request.session['total_items'] = 0 # Обновляем счетчик товаров здесь
             request.session.modified = True # Говорим django, что сессия была изменена
            
             if payment_method == 'online':
                 request.session['payment_data'] = {
                 'full_name': full_name,
                 'email': email,
                 'address': address,
                 'total_price': total_price,
                 'phone_number': phone_number
                }
                # Переходим на страницу оплаты
                 return redirect('products:payment')  
             else:
                # Отображаем страницу ответа при оплате при получении
                return render(request, 'products/httpresponce.html', {'payment_method': 'При получении' })
       else:
            return render(request, 'products/checkout.html', {
                'cart_items': cart_items,
                'total_price': total_price,
                'form':form
           })

    else:
        form = OrderForm()
        return render(request, 'products/checkout.html', {
            'cart_items': cart_items,
            'total_price': total_price,
            'form':form
       })

# Удалить товар из корзины
def remove_from_cart(request, product_id):
    cart = request.session.get('cart', {})  # Получаем корзину из сессии

    if str(product_id) in cart:
        del cart[str(product_id)]  # Удаляем товар из корзины
        request.session['cart'] = cart  # Обновляем корзину в сессии

        # Пересчитываем общее количество товаров в корзине
        total_items = sum(item['quantity'] for item in cart.values())
        request.session['total_items'] = total_items  # Сохраняем количество в сессии
    else:
        # Если корзина пуста или товара нет, устанавливаем total_items в 0
        default_cart_count = settings.DEFAULT_CART_COUNT
        request.session['cart_count'] = default_cart_count

    return redirect('products:view_cart')  # Перенаправляем на страницу корзины

# Оплата онлайн
def payment(request):
    if request.method == 'POST':
        card_number = request.POST.get('card_number')
        expiry_date = request.POST.get('expiry_date')
        cvv = request.POST.get('cvv')

        # Логика обработки платежа (например, проверка данных карты)
        # Для демонстрации просто выводим данные
        print(f'Card Number: {card_number}, Expiry: {expiry_date}, CVV: {cvv}')

        # Если оплата успешна, возвращаем успешный ответ
        return JsonResponse({'status': 'success'})

    return render(request, 'products/payment.html')

# Просмотр корзины
def cart(request):
    cart = request.session.get('cart', {})

    # Если корзина пуста, сбросим счётчик товаров
    if not cart:
        request.session['total_items'] = 0
        request.session.modified = True

    # Дальше логика вывода товаров в корзине
    cart_items = []
    total_price = 0
    for item_id, data in cart.items():
        try:
            product = Product.objects.get(id=item_id)
            cart_items.append({
                'product': product,
                'quantity': data['quantity'],
                'total_price': float(data['price']) * data['quantity'],
            })
            total_price += float(data['price']) * data['quantity']
        except Product.DoesNotExist:
            continue

    return render(request, 'products/cart.html', {'cart_items': cart_items, 'total_price': total_price})

