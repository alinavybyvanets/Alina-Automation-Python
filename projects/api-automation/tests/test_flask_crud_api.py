import pytest
import allure
from app import can_connect, init_db, clear_users, insert_user, update_user, delete_user, select_users

@pytest.fixture(scope="session", autouse=True)
def wait_and_init():
    assert can_connect(retries=30, delay=1.0), "Postgres is not reachable"
    init_db()
    yield

@pytest.fixture(autouse=True)
def clean_table():
    """Очищаємо таблицю перед кожним тестом, щоб не було колізій UNIQUE(email)."""
    clear_users()
    yield

@allure.feature("DB CRUD")
@allure.title("Підключення до бази доступне")
def test_connection():
    with allure.step("Перевіряємо can_connect()"):
        assert can_connect() is True

@allure.feature("DB CRUD")
@allure.title("INSERT + SELECT працюють коректно")
def test_insert_and_select():
    with allure.step("Вставляємо користувача Bob"):
        uid = insert_user("Bob", "bob@example.com")
    with allure.step("Отримуємо всі рядки з таблиці"):
        rows = select_users()
    with allure.step("Перевіряємо, що новий запис існує"):
        assert any(r[0] == uid and r[1] == "Bob" and r[2] == "bob@example.com" for r in rows )

@allure.feature("DB CRUD")
@allure.title("UPDATE змінює ім'я користувача")
def test_update():
    with allure.step("Вставляємо користувача Angelina"):
        uid = insert_user("Angelina", "angelina@example.com")

    with allure.step("Оновлюємо імʼя на Angela"):
        affected = update_user(uid, name="Angela")
        assert affected == 1

    with allure.step("Перевіряємо, що оновлення відобразилось в SELECT"):
        rows = select_users()
        assert any(r[0] == uid and r[1] == "Angela" for r in rows)

@allure.feature("DB CRUD")
@allure.title("DELETE видаляє запис")
def test_delete():
    with allure.step("Вставляємо користувача Diana"):
        uid = insert_user("Diana", "diana@example.com")
    with allure.step("Видаляємо цього користувача"):
        affected = delete_user(uid)
        assert affected == 1
    with allure.step("Перевіряємо, що запису більше немає"):
        rows = select_users()
        assert all(r[0] != uid for r in rows)