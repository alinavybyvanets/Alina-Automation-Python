import pytest
from app import can_connect, init_db, clear_users,  insert_user, update_user, delete_user, select_users
@pytest.fixture(scope="session", autouse=True)
def wait_and_init():
    assert can_connect(retries=30, delay=1.0), "Postgres is not reachable"
    init_db()
    yield

def clean_table():
    clear_users()
    yield

def test_connection():
    assert can_connect() is True

def test_insert_and_select():
    uid = insert_user("Bob", "bob@example.com")
    rows = select_users()
    assert any(r[0] == uid and r[1] == "Bob" and r[2] == "bob@example.com" for r in rows )

def test_update():
    uid = insert_user("Angelina", "angelina@example.com")
    update_user(uid, name="Angela")
    rows = select_users()
    assert any(r[0] == uid and r[1] == "Angela" for r in rows)

def test_delete():
    uid = insert_user("Diana", "diana@example.com")
    delete_user(uid)
    rows = select_users()
    assert all(r[0] != uid for r in rows)