from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

DEFAULT_TIMEOUT = 20

class BasePage:
    def __init__(self, driver, timeout: int = DEFAULT_TIMEOUT):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, timeout)

    def open(self, url: str):
        self.driver.get(url)

    def wait_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def wait_present(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def elements_present(self, locator):
        return self.driver.find_elements(*locator)

    def safe_click_if_present(self, locator):
        elems = self.elements_present(locator)
        if elems:
            try:
                elems[0].click()
            except Exception:
                pass
