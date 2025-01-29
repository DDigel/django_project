from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'), #Подробная страница продукта
    path('products/add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'), #Добавление в корзину
    path('products/view_cart/', views.view_cart, name='view_cart'), #Показать корзину
    path('products/remove_from_cart/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'), #Удалить из корзины
    path('products/checkout/', views.checkout, name='checkout'), #Оформление заказа
    path('payment/', views.payment, name='payment'), #Оплата
    path('category/<str:category_id>/', views.category_list, name='category_list'), #Отображение продукта по категории
]


