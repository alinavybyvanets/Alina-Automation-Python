import os
import re
import pytest
from pages.tracking_page import TrackingPage

TEST_DATA = [("20710223187184", "Отримана")]

env_ttn = os.getenv("NP_TTN")
env_expected = os.getenv("NP_EXPECTED", "Отримана")

if env_ttn:
    TEST_DATA.append((env_ttn, env_expected))

def norm(s: str) -> str:
    s = (s or "").replace("\u00a0", " ")
    return re.sub(r"\s+", " ", s).strip()

@pytest.mark.parametrize("ttn, expected_status", TEST_DATA)
def test_tracking_status(driver, ttn, expected_status):
    page = TrackingPage(driver)
    page.open_page()
    page.enter_ttn_and_submit(ttn)

    if page.is_not_found():
        pytest.skip("Цей ТТН не знайдено (можливо, старший за 3 місяці або помилковий).")

    actual = page.get_status_text()
    assert norm(actual) == norm(expected_status), \
        f'Очікували: {expected_status!r}, отримали: {actual!r}'

def test__skip_if_no_data():
    if not TEST_DATA:
        pytest.skip("Не задано NP_TTN/TEST_DATA. Вкажи TTN або додай пару (TTN, 'Отримана').")
