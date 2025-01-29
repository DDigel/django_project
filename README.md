Дигель Дмитрий

__Онлайн-магазин техники Apple AppleWorld__ 

Разработка веб-приложения на Python;
It-Academy;
Python 3.12.7;
Фреймворк Django 5.1.4;

Контакты для связи:
Telegram - @onehonest (https://t.me/onehonest); 
Inst - @1_honest

На финальный проект для окончания курса, я решил сделать простенький магазин техники apple с названием AppleWorld, используя фреймворк django,
также использовались html, css для разметки и bootstrap https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha3/dist/css/bootstrap.min.css для более эстетичного вида приложения

__ДИСКЛЕЙМЕР: Вся информация и медиафайлы используются исключительно в информационных целях и не используются для коммерции :)__

Начну с админ-панели, где мы логинимся под суперпользователем admin, тут я настроил каждый продукт, присвоил ему категорию, описание, фото для отображения на своём веб-сайте

![Image alt](https://github.com/DDigel/django_project/blob/project_branch/for%20readme/admpannel2.jpg)

![Image alt](https://github.com/DDigel/django_project/blob/project_branch/for%20readme/admpannel1.jpg)

Далее переходим на главную страницу сайта, нас встречает вот такой короткий ролик и в принципе больше здесь никакой информации на главной странице нет
В навигационной панели видим вкладки с названиями разделов Справа название магазина "AppleWorld" при нажатии на него нас переадресовывают на главную страницу, слева - "Весь каталог", "Iphone", "Watch", "Airpods", "Корзина" и "Профиль"

![Image alt](https://github.com/DDigel/django_project/blob/project_branch/for%20readme/gif-for-readme.gif)

![Image alt](https://github.com/DDigel/django_project/blob/project_branch/for%20readme/navbar.jpg)

Весь Каталог выглядит таким образом

![Image alt](https://github.com/DDigel/django_project/blob/project_branch/for%20readme/catalog1.jpg)

![Image alt](https://github.com/DDigel/django_project/blob/project_branch/for%20readme/catalog2.jpg)

Тут у нас есть кнопки "Добавить в корзину", благодаря которой мы можем добавить товар в корзину и "Подробнее", где мы можешь посмотреть краткую информацию о товаре

![Image alt](https://github.com/DDigel/django_project/blob/project_branch/for%20readme/cart.jpg)

![Image alt](https://github.com/DDigel/django_project/blob/project_branch/for%20readme/podrobnee.jpg)

Iphone у нас показывает страницу со всеми смартфонами из базы данных

![Image alt](https://github.com/DDigel/django_project/blob/project_branch/for%20readme/iphone.jpg)

Watch у нас показывает страницу со всеми часами из базы данных

![Image alt](https://github.com/DDigel/django_project/blob/project_branch/for%20readme/watch.jpg)

Airpods у нас показывает страницу со всеми наушниками из базы данных

![Image alt](https://github.com/DDigel/django_project/blob/project_branch/for%20readme/airpods.jpg)

Из корзины мы можем сразу же оформить заказ

![Image alt](https://github.com/DDigel/django_project/blob/project_branch/for%20readme/checkout.jpg)

Ну и через "Профиль" мы можем войти уже в существующий профиль или же зарегестрироваться, указав нужные данные:

![Image alt](https://github.com/DDigel/django_project/blob/project_branch/for%20readme/log%20in.jpg)

![Image alt](https://github.com/DDigel/django_project/blob/project_branch/for%20readme/registration.jpg)

Если авторизоваться, то можно указать некоторые данные для пользователя

![Image alt](https://github.com/DDigel/django_project/blob/project_branch/for%20readme/profile.jpg)

Вот сообственно и всё! Такой краткий обзор небольшое на веб-приложение

# Инструкция как сохранить и запустить проект у себя, все команды нужно прописывать в терминале

1. Клонируйте репозиторий:

```git clone https://github.com/DDigel/django_project.git```

```cd django_project```

2. Создайте виртуальное окружение:

```python -m venv venv```

```source venv/bin/activate  #Для Linux/Mac```

```venv\Scripts\activate     #Для Windows```

3. Установите зависимости:

```pip install -r requirements.txt```

4. Примените миграции:

```python manage.py migrate```

5. Создайте суперпользователя:

```python manage.py createsuperuser```

6. Запустите сервер:

```python manage.py runserver```

Перейди в браузере по адресу: http://127.0.0.1:8000/.
