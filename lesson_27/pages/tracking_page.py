from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage


class TrackingPage(BasePage):
    URL = "https://tracking.novaposhta.ua/#/uk"

    TRACKING_INPUT = (
        By.XPATH,
        "//input[contains(@class,'track__form-group-input') and contains(@placeholder,'Номер посил')]"
    )
    COOKIES_ACCEPT_UA = (
        By.XPATH,
        "//*[self::button or self::a][.='Прийняти' or contains(., 'Прийняти')]"
    )
    COOKIES_ACCEPT_EN = (
        By.XPATH,
        "//*[self::button or self::a][.='Accept' or contains(., 'Accept')]"
    )
    SEARCH_BUTTON = (
        By.XPATH,
        "//*[self::button or self::a or @role='button'][normalize-space()='Пошук' or contains(normalize-space(.),'Пошук')]"
    )

    NOT_FOUND_ALERT = (
        By.XPATH,
        "//*[contains(., 'Ми не знайшли посилку')"
        "   or contains(., 'не знайдено посилку')"
        "   or contains(., 'не знайдено')]"
    )

    STATUS_TEXT = (By.CSS_SELECTOR, "div.header__status-text")

    def open_page(self):
        self.open(self.URL)
        self.safe_click_if_present(self.COOKIES_ACCEPT_UA)
        self.safe_click_if_present(self.COOKIES_ACCEPT_EN)

    def enter_ttn_and_submit(self, ttn: str):
        input_element = self.wait_visible(self.TRACKING_INPUT)
        input_element.clear()
        input_element.send_keys(ttn)
        input_element.send_keys(Keys.ENTER)
        try:
            WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable(self.SEARCH_BUTTON)).click()
        except Exception:
            pass

    def is_not_found(self) -> bool:
        """Чи показано алерт 'Ми не знайшли посилку'."""
        return bool(self.elements_present(self.NOT_FOUND_ALERT))

    def get_status_text(self) -> str:
        """Повертає текст поточного статусу (наприклад, «Отримана»). Порожній рядок, якщо не знайдено/таймаут."""
        try:
            WebDriverWait(self.driver, 20).until(
                lambda d: d.find_elements(*self.STATUS_TEXT) or d.find_elements(*self.NOT_FOUND_ALERT)
            )

            if self.is_not_found():
                return ""

            def _non_empty(d):
                try:
                    txt = d.find_element(*self.STATUS_TEXT).text.strip()
                    return txt if txt else False
                except Exception:
                    return False

            return WebDriverWait(self.driver, 15).until(_non_empty)
        except TimeoutException:
            return ""