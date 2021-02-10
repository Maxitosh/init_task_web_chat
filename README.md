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
  "id": 5,
  "username": "Test3",
  "email": "",
  "first_name": "",
  "last_name": ""
}
```

## Chat API endpoints

### Создание нового чата

#### Общие сведения

Создание нового чата. Функция доступна только для авторизованных пользователей, существующие логин и пароль пользователя
должны быть переданы в запросе к серверу.

#### Параметры

| Parameters | Required | Type | Description |
| -------- | -------- | -------- |  -------- |
| credentials     | :heavy_check_mark:     | Text     | Логин и пароль юзера|
| members     | :heavy_check_mark:     | Text     | Лист из **
2** id юзеров нового чата, один из id обязательно должен принадлежать текущему юзеру, к примеру id=5 соответсвует id юзера, созданного выше|

#### CURL

```console
curl --data '{"members": [1,5]}' -u Test3:testpass123 -H "Content-Type: application/json" -X POST http://localhost:8000/chats/
```

#### Пример ответа

```json
{
  "id": 23,
  "members": [
    1,
    5
  ]
}
```

В ответе получаем id созданного чата.

## Веб интерфейс приложения