# Тестовое задание

## Курейкин Макс Александрович
---
## Описание проекта

Веб чат на Django, REST API и веб интерфейс.


## Технологии в проекте
* Docker
* Django
* DRF
* Postgres

## Инструкция по запуску

1. Клонируйте [GitHub репозиторий](https://github.com/Maxitosh/init_task_web_chat) на локальную машину.
1. Запустите проект, используя композицию Docker-контейнеров командой:
   > docker-compose up
1. Дождитесь инициализации базы данных и запуска Django сервера.

## Инициированный пользователь

* login=Test
* password=testpass123
* id=1

# API

## Accounts API endpoints

### Регистрация пользователя

#### Общие сведения

Регистрация нового пользователя.

#### Параметры

| Parameters | Required | Type |
| -------- | -------- | -------- | 
| username     | :heavy_check_mark:     | Text     |
| password     | :heavy_check_mark:     | Text     |
| password2     | :heavy_check_mark:     | Text     |

#### CURL

```console
curl --data '{"username": "Test3", "password": "testpass123", "password2":"testpass123"}' -H "Content-Type: application/json" -X POST http://localhost:8000/accounts/register/
```

#### Пример ответа

```json
{
   "id": 2,
   "username": "Test3",
   "email": "",
   "first_name": "",
   "last_name": ""
}
```

### Список пользователей

#### Общие сведения

Получение списка пользователей и соотвествующие id

#### Параметры

#### CURL

```console
curl http://localhost:8000/accounts/users/
```

#### Пример ответа

```json
[
   {
      "id": 1,
      "username": "Test"
   },
   {
      "id": 2,
      "username": "Test3"
   }
]
```

---

## Chat API endpoints

### Создание нового чата

#### Общие сведения

Создание нового чата. Функция доступна только для авторизованных пользователей, существующие логин и пароль пользователя
должны быть переданы в запросе к серверу.

#### Параметры

| Parameters | Required | Type | Description |
| -------- | -------- | -------- |  -------- |
| credentials     | :heavy_check_mark:     | Text     | Логин и пароль юзера|
| members     | :heavy_check_mark:     | Text     | Лист из 2 id юзеров нового чата*|

*Один из id обязательно должен принадлежать текущему юзеру, к примеру id=2 соответсвует id юзера, созданного выше

#### CURL

```console
curl --data '{"members": [1,2]}' -u Test3:testpass123 -H "Content-Type: application/json" -X POST http://localhost:8000/chats/
```

#### Пример ответа

```json
{
   "id": 1,
   "members": [
      1,
      2
   ]
}
```

В ответе получаем id созданного чата.

### Получение списка чатов

#### Общие сведения

Получение списка чатов конкретного пользователя. Функция доступна только для авторизованных пользователей, существующие
логин и пароль пользователя должны быть переданы в запросе к серверу.

#### CURL

```console
curl -u Test3:testpass123 http://localhost:8000/chats/
```

#### Пример ответа

```json
[
   {
      "id": 1,
      "members": [
         1,
         2
      ]
   }
]
```

В ответе получаем лист чатов.

### Отправка сообщение

#### Общие сведения

Отправка нового сообщения в чат от лица пользователя. Функция доступна только для авторизованных пользователей,
существующие логин и пароль пользователя должны быть переданы в запросе к серверу.

#### Параметры

| Parameters | Required | Type | Description |
| -------- | -------- | -------- |  -------- |
| chat_id     | :heavy_check_mark:     | Integer     | id чата, должен быть указан в url запроса chats/[ID]/messages/|
| message     | :heavy_check_mark:     | Text     | Сообщение в чат|

#### CURL

```console
curl --data '{"message":"Test from console"}' -H "Content-Type: application/json" -u Test3:testpass123 -X POST http://localhost:8000/chats/1/messages/
```

#### Пример ответа

```json
{
   "id": 52,
   "message": "Test from console",
   "pub_date": "2021-02-10T11:00:03.662929+03:00",
   "is_read": false,
   "author_id": 2,
   "chat_id": 1
}
```

В ответе получаем новое сообщение.

### Получение сообщений чата

#### Общие сведения

Получение списка сообщений конкретного чата. Функция доступна только для авторизованных пользователей, существующие
логин и пароль пользователя должны быть переданы в запросе к серверу.

| Parameters | Required | Type | Description |
| -------- | -------- | -------- |  -------- |
| chat_id     | :heavy_check_mark:     | Integer     | id чата, должен быть указан в url запроса chats/[ID]/messages/|

#### CURL

```console
curl -u Test3:testpass123 http://localhost:8000/chats/1/messages/
```

#### Пример ответа

```json
[
   {
      "id": 52,
      "message": "Test from console",
      "pub_date": "2021-02-10T11:00:03.662929+03:00",
      "is_read": true,
      "author_id": 2,
      "chat_id": 1
   },
   {
      "id": 53,
      "message": "Here you can write and send new message",
      "pub_date": "2021-02-10T11:06:54.846459+03:00",
      "is_read": true,
      "author_id": 2,
      "chat_id": 1
   },
   {
      "id": 54,
      "message": "Reply from another user",
      "pub_date": "2021-02-10T11:07:36.941232+03:00",
      "is_read": true,
      "author_id": 1,
      "chat_id": 1
   }
]
```

В ответе получаем лист сообщений.

## Веб интерфейс приложения

[Веб интерфейс доступен по ссылке](http://127.0.0.1:8000/)

### Внешний вид

#### Главная страница

![](https://i.imgur.com/NDQSeQM.png)

#### Регистрация

![](https://i.imgur.com/Dfoddt6.png)

#### Авторизация

![](https://i.imgur.com/SWdcwuz.png)

#### Страница с диалогами

![](https://i.imgur.com/SVKa3dK.png)

#### Страница с сообщениями диалога

![](https://i.imgur.com/eruXL5m.png)

#### Новое сообщение

![](https://i.imgur.com/NJANDO4.png)

