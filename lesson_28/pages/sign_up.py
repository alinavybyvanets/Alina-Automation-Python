from selenium.webdriver.common.by import By

class SignUp:
    FIRST_NAME = (By.ID, "signupName")
    LAST_NAME = (By.ID, "signupLastName")
    EMAIL = (By.ID, "signupEmail")
    PASSWORD = (By.ID, "signupPassword")
    REPEAT_PASSWORD = (By.ID, "signupRepeatPassword")

    REGISTER_BTN = (
        By.XPATH,
        "//ngb-modal-window//button[contains(@class,'btn-primary') and "
        "(normalize-space()='Register' or normalize-space()='Sign up')]"
    )

    REGISTER_BTN_DISABLED = (
        By.XPATH,
        "//ngb-modal-window//button[contains(@class,'btn-primary') and "
        "(normalize-space()='Register' or normalize-space()='Sign up') and "
        "(@disabled or @aria-disabled='true' or contains(@class,'disabled'))]"
    )

    REGISTER_BTN_ENABLED = (
        By.XPATH,
        "//ngb-modal-window//button[contains(@class,'btn-primary') and "
        "(normalize-space()='Register' or normalize-space()='Sign up') and "
        "not(@disabled) and not(@aria-disabled='true') and not(contains(@class,'disabled'))]"
    )

    GARAGE_HEADER = (By.XPATH, "//h1[normalize-space()='Garage' or normalize-space()='My garage']")
    ADD_CAR_BTN = (By.XPATH, "//button[contains(., 'Add car')]")