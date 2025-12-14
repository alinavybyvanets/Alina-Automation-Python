from selenium.webdriver.common.by import By

class HomePage:
        SIGN_UP_BTN = (By.CSS_SELECTOR, "button.hero-descriptor_btn.btn.btn-primary")

        SIGN_UP_ALT = (
            By.XPATH,
            "//button[normalize-space(translate(., 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'))='sign up']")