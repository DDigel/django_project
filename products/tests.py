from django.test import TestCase
from products.models import Category, Product as ProductModel
from django.core.exceptions import ValidationError
from products.models import Product

# Create your tests here.
class CategoryModelTest(TestCase):
    def setUp(self):
        # Создаем тестовую категорию
        self.category = Category.objects.create(
            name="Телефоны",
            description="Категория для смартфонов"
        )

    def test_category_creation(self):
        """Проверка создания объекта Category"""
        self.assertEqual(self.category.name, "Телефоны")
        self.assertEqual(self.category.description, "Категория для смартфонов")

    def test_category_str_representation(self):
        """Проверка строкового представления Category"""
        self.assertEqual(str(self.category), "Телефоны")


class ProductModelTest(TestCase):
    def setUp(self):
        # Создаем тестовый продукт
        self.product = ProductModel.objects.create(
            name="iPhone 14",
            category="smartphone",
            description="Новый iPhone 14",
            price=999.99,
            stock=10
        )

    def test_product_creation(self):
        """Проверка создания объекта Product"""
        self.assertEqual(self.product.name, "iPhone 14")
        self.assertEqual(self.product.category, "smartphone")
        self.assertEqual(self.product.price, 999.99)
        self.assertEqual(self.product.stock, 10)

    def test_product_str_representation(self):
        """Проверка строкового представления Product"""
        self.assertEqual(str(self.product), "iPhone 14")

    def test_price_validation(self):
        """Проверка валидации поля price"""
        product = Product(
            name="Invalid Product",
            category="smartphone",
            description="Invalid price",
            price=-100,  # Отрицательная цена должна вызвать ошибку
            stock=5
    )
        with self.assertRaises(ValidationError) as context:
            product.full_clean()  # Вызываем валидацию

    # Проверяем, что ошибка связана с полем price
        self.assertIn('price', context.exception.error_dict)
        self.assertEqual(context.exception.error_dict['price'][0].message, 'Цена не может быть отрицательной.')