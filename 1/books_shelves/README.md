## Полки для книг

### Для запуска:

1. Создать бд в PostgreSQL
2. Вписать свои данные в параматры бд в файле cmd/main.go
3. При необходимости изменить параметры в файле internal/app/shelf_for_books/server/start_server.go
4. Выполнить команду migrate -database postgres://postgres:password@localhost:5432/example?sslmode=disable -path db/migrations up

### Запросы:

1.POST /book - создание книги, содержание Body:
```
{
"author":"А. С. Пушкин",
"name":"Евгений Онегин",
"status":false,
"book_shelf":2
}
```
 Значение "book_shelf" должно существовать.

2. GET /book/id - получение книги по if
3. GET /book/all - получение списка книг

4. POST /shelf - создание полки вместе с книгами,
содержание  Body:
```
{
    "shelf_gerne": {
        "id_gerne": 3
    },
    "books": [
        {
            "author": "Конан Дойл",
            "name": "Собака Баскервилей",
            "status": false
        },
        {
            "author": "Агата Кристи",
            "name": "Занавес",
            "status": true
        }
    ]
}
```
Значение "id_gerne" должно существовать.
5. GET /shelf/all - получение списка полок с книгами