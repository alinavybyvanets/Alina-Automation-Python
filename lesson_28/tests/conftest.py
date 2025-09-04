import time
import uuid

import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from pages.sign_up import SignUp
from pages.home_page import HomePage

@pytest.fixture(scope="session")
def creds():
    """Дані для Basic Auth"""
    return {
        "login": "guest",
        "password": "welcome2qauto",
        "host": "qauto2.forstudy.space",
    }

@pytest.fixture(scope="session")
def base_url(creds):
    """URL із Basic Auth для прямого доступу"""
    return f'https://{creds["login"]}:{creds["password"]}@{creds["host"]}/'

@pytest.fixture(scope="session")
def driver():
    """Ініціалізація Chrome WebDriver"""
    options = Options()
    options.add_argument("--window-size=1366,900")
    drv = webdriver.Chrome(options=options)
    yield drv
    drv.quit()

@pytest.fixture(scope="session")
def wait(driver):
    return WebDriverWait(driver, 15)

@pytest.fixture
def open_home(driver, base_url, wait):
    """Відкрити головну сторінку з базовою авторизацією"""
    driver.get(base_url)
    wait.until(lambda d: d.find_elements(*HomePage.SIGN_UP_BTN) or d.find_elements(*HomePage.SIGN_UP_ALT))

@pytest.fixture
def open_signup(driver, wait):
    """Відкрити модальне вікно реєстрації"""
    try:
        wait.until(EC.element_to_be_clickable(HomePage.SIGN_UP_BTN)).click()
    except Exception:
        wait.until(EC.element_to_be_clickable(HomePage.SIGN_UP_ALT)).click()
        # ключ: чекаємо доки модалка відкрита (видиме перше поле)
        wait.until(EC.visibility_of_element_located(SignUp.FIRST_NAME))



@pytest.fixture
def assert_register_btn_disabled(driver, wait):
    """Початково кнопка має бути disabled."""
    wait.until(EC.presence_of_element_located(SignUp.REGISTER_BTN_DISABLED))

@pytest.fixture
def new_user_data():
    """Згенерувати унікальні валідні дані користувача"""
    uniq = uuid.uuid4().hex[:8]
    return {
        "first_name": "Alina",
        "last_name": "Tester",
        "email": f"alina.auto.{uniq}@example.com",
        "password": f"Aa1!{uniq}",
    }

@pytest.fixture
def fill_signup_form(driver, wait, new_user_data):
    """Заповнити форму реєстрації валідними даними"""
    wait.until(EC.visibility_of_element_located(SignUp.FIRST_NAME)).send_keys(new_user_data["first_name"])
    driver.find_element(*SignUp.LAST_NAME).send_keys(new_user_data["last_name"])
    driver.find_element(*SignUp.EMAIL).send_keys(new_user_data["email"])
    driver.find_element(*SignUp.PASSWORD).send_keys(new_user_data["password"])
    driver.find_element(*SignUp.REPEAT_PASSWORD).send_keys(new_user_data["password"])

@pytest.fixture
def wait_register_btn_enabled(driver, wait):
    """Дочекатися, поки кнопка стане enabled (зникне [disabled])"""
    wait.until(EC.presence_of_element_located(SignUp.REGISTER_BTN_ENABLED))
    #додаткова перевірка
    def _really_enabled(drv):
        btn = drv.find_element(*SignUp.REGISTER_BTN)
        aria = (btn.get_attribute("aria-disabled") or "").lower()
        classes = (btn.get_attribute("class") or "")
        return btn.is_enabled() and aria != "true" and "disabled" not in classes.split()
    WebDriverWait(driver, 10).until(_really_enabled)

@pytest.fixture
def submit_signup(driver, wait, wait_register_btn_enabled):
    """Клік по активній кнопці Register"""
    btn= wait.until(EC.element_to_be_clickable(SignUp.REGISTER_BTN_ENABLED))
    btn.click()

@pytest.fixture
def assert_registration_success(driver, wait):
    """Підтвердити успішну реєстрацію (редірект/елементи панелі)."""
    ok = False
    # Варіант 1: URL містить /panel/garage
    for _ in range(30):
        if "/panel/garage" in driver.current_url:
            ok = True
            break
        time.sleep(0.5)
    # Варіант 2: є ознаки гаража на сторінці
    if not ok:
        try:
            wait.until(
                lambda d: d.find_elements(*SignUp.GARAGE_HEADER) or
                          d.find_elements(*SignUp.ADD_CAR_BTN),
            )
            ok = True
        except Exception:
            ok = False
    assert ok, "Не вдалося підтвердити успішну реєстрацію: немає /panel/garage і маркери гаража відсутні."



