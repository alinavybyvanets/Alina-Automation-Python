# Python + PostgreSQL (CRUD) у Docker

## 1) Створити мережу Docker
```bash
docker network create mynet
```

## 2) Запустити PostgreSQL (БД)
```bash
docker run --name mydb --network mynet   -e POSTGRES_USER=user   -e POSTGRES_PASSWORD=pass   -e POSTGRES_DB=testdb   -d postgres:16
```

(Опційно) подивитися логи:
```bash
docker logs -f mydb   # Ctrl+C, щоб вийти
```

## 3) Зібрати образ застосунку
```bash
docker build -t myapp .
```

## 4) Запустити тести (pytest)
```bash
docker run --rm --name myapp-tests --network mynet   -e DB_HOST=mydb -e DB_PORT=5432   -e DB_NAME=testdb -e DB_USER=user -e DB_PASSWORD=pass   myapp pytest -q
```
Очікувано: `.... [100%]` і `4 passed in ...s`.

## 5) Запустити демо-CRUD
```bash
docker run --rm --name myapp --network mynet   -e DB_HOST=mydb -e DB_PORT=5432   -e DB_NAME=testdb -e DB_USER=user -e DB_PASSWORD=pass   myapp
```
Результат: Insert → Select → Update → Select → Delete → Select.

## 6) (Опційно) Відкрити psql у контейнері БД
```bash
docker exec -it mydb psql -U user -d testdb
```
Деякі команди в `psql`:
```sql
\dt          -- список таблиць
\d users     -- структура таблиці
SELECT * FROM users;
\q           -- вийти
```

## 7) Прибирання
```bash
docker rm -f myapp myapp-tests 2>/dev/null || true
docker rm -f mydb
docker network rm mynet
```

