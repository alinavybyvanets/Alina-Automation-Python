import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--window-size=1400,900")

    driver = webdriver.Chrome(options=options)
    try:
        yield driver
    finally:
        driver.quit()

