from django.test import TestCase
from django.contrib.auth.models import User, Category
from users.models import Profile, UserProfile, Order, Product as UsersProduct

# Create your tests here.
class ProfileModelTest(TestCase):
    def setUp(self):
        # Создаем тестового пользователя и профиль
        self.user = User.objects.create_user(username="testuser", password="testpass123")
        self.profile = Profile.objects.create(user=self.user, phone="+1234567890")

    def test_profile_creation(self):
        """Проверка создания объекта Profile"""
        self.assertEqual(self.profile.user.username, "testuser")
        self.assertEqual(self.profile.phone, "+1234567890")

    def test_profile_str_representation(self):
        """Проверка строкового представления Profile"""
        self.assertEqual(str(self.profile), "testuser Profile")


class UserProfileModelTest(TestCase):
    def setUp(self):
        # Создаем тестового пользователя и профиль
        self.user = User.objects.create_user(username="testuser2", password="testpass123")
        self.user_profile = UserProfile.objects.create(user=self.user, birth_date="1990-01-01")

    def test_user_profile_creation(self):
        """Проверка создания объекта UserProfile"""
        self.assertEqual(self.user_profile.user.username, "testuser2")
        self.assertEqual(str(self.user_profile.birth_date), "1990-01-01")

    def test_user_profile_str_representation(self):
        """Проверка строкового представления UserProfile"""
        self.assertEqual(str(self.user_profile), "Профиль testuser2")


class OrderModelTest(TestCase):
    def setUp(self):
        # Создаем тестового пользователя и продукты
        self.user = User.objects.create_user(username="orderuser", password="orderpass123")
        self.product1 = UsersProduct.objects.create(
            name="Laptop",
            description="Powerful laptop",
            price=1500.00,
            image="products/laptop.jpg",
            category=Category.objects.create(name="Electronics")
        )
        self.product2 = UsersProduct.objects.create(
            name="Keyboard",
            description="Mechanical keyboard",
            price=100.00,
            image="products/keyboard.jpg",
            category=Category.objects.create(name="Accessories")
        )
        # Создаем заказ
        self.order = Order.objects.create(user=self.user)
        self.order.products.add(self.product1, self.product2)

    def test_order_creation(self):
        """Проверка создания объекта Order"""
        self.assertEqual(self.order.user.username, "orderuser")
        self.assertEqual(self.order.products.count(), 2)

    def test_order_str_representation(self):
        """Проверка строкового представления Order"""
        self.assertEqual(str(self.order), "Order #1 by orderuser")


