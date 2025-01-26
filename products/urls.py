from django.urls import path, include
from . import views

app_name = 'products'

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
    path('products/add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('products/view_cart/', views.view_cart, name='view_cart'),
    path('products/remove_from_cart/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('products/checkout/', views.checkout, name='checkout'),
    path('payment/', views.payment, name='payment'),
    path('category/<str:category_id>/', views.category_list, name='category_list'),
]


