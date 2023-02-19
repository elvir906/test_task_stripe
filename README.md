[![Python](https://img.shields.io/badge/-Python-464646?style=flat-square&logo=Python)](https://www.python.org/)
[![Django](https://img.shields.io/badge/-Django-464646?style=flat-square&logo=Django)](https://www.djangoproject.com/)
[![SQLite](https://img.shields.io/badge/-SQLite-464646?style=flat-square&logo=SQLite)](https://www.sqlite.org/)
[![Nginx](https://img.shields.io/badge/-NGINX-464646?style=flat-square&logo=NGINX)](https://nginx.org/ru/)
[![gunicorn](https://img.shields.io/badge/-gunicorn-464646?style=flat-square&logo=gunicorn)](https://gunicorn.org/)
[![docker](https://img.shields.io/badge/-Docker-464646?style=flat-square&logo=docker)](https://www.docker.com/)

Задание:
-------

- Реализовать Django + Stripe API бэкенд со следующим функционалом и условиями:
- Django Модель `Item` с полями `(name, description, price) `
- API с двумя методами:
    * GET `/buy/{id}`, c помощью которого можно получить Stripe Session Id для оплаты выбранного Item. При выполнении
      этого метода c бэкенда с помощью python библиотеки stripe должен выполняться
      запрос` stripe.checkout.Session.create(...)` и полученный session.id выдаваться в результате запроса
    * GET `/item/{id}`, c помощью которого можно получить простейшую HTML страницу, на которой будет информация о
      выбранном `Item` и кнопка Buy. По нажатию на кнопку Buy должен происходить запрос на `/buy/{id}`, получение
      session_id и далее с помощью JS библиотеки Stripe происходить редирект на Checkout
      форму `stripe.redirectToCheckout(sessionId=session_id)`

- Залить решение на Github, описать запуск в README.md

- Запуск используя `Docker`

- Использование environment variables

- Просмотр Django Моделей в Django Admin панели - __доступно по адресу `127.0.0.1/admin`

- Запуск приложения на удаленном сервере, доступном для тестирования - запущенно на `127.0.0.1`

Описание:
-------------------------
Тестовое задание выполнено на языке Python с использованием фреймворка Django. Запуск проекта производится с помощью Doсker. Так же использовал возможности Nginx для раздачи статики, чтобы Django-админка смотрелась презентабельней с DEBUG = False в settings.py. Бэкэнд-приложение и Nginx запускаются в двух разных контейнерах. Nginx и Django связываются благодаря Gunicorn.

Получение api-ключей
-------------------------

Publishable key (STRIPE_PUBLIC_KEY):
https://dashboard.stripe.com/apikeys

Secret key (STRIPE_SECRET_KEY):
https://dashboard.stripe.com/apikeys

Webhooks:
https://dashboard.stripe.com/webhooks


Подготовка
------

Склонировать репозиторий на локальную машину
```
git clone https://github.com/elvir906/test_task_stripe.git
```
Создать .env файл в директории stripe_app, в той, в которой расположен manage.py,
и прописать в нём полученные api-ключи. 

```
STRIPE_PUBLIC_KEY='ключ, полученный по ссылке'
STRIPE_SECRET_KEY='ключ, полученный по ссылке'

```

Запуск приложения в Docker
------
```
docker-compose up -d --build
```
Docker сам установит нужные зависимости из requirements.txt, запустит наше приложение
и серверные прилолжения Gunicorn и Nginx

Для отображения статики в админки выполнить
```
docker compose exec stripe-backend python manage.py collectstatic
```

Проект будет досупен по адресу http://127.0.0.1/.
Админка будет доступна по адресу http://127.0.0.1/admin/
login: admin, пароль: 123456

Проект так же запущен и доступен для тестирования по адресу: http://84.201.160.140/
Админка login: admin, пароль: 123456
