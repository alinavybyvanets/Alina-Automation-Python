# locators.py

class Locators:
    # -------------------- XPATH --------------------
    XPATH = {
        # Home
        "home_link": "//header//a[text()='Home']",
        "signin_button": "//header//button[text()='Sign In']",
        "guest_login_button": "//header//button[text()='Guest log in']",
        "signup_button": "//section//button[text()='Sign up']",
        "youtube_iframe": "//section//iframe[contains(@src, 'youtube')]",

        # Log In
        "email_input_id": "//input[@id='signinEmail']",
        "email_input_label": "//div//label[text()='Email']/following::input[1]",
        "password_input_id": "//input[@id='signinPassword']",
        "password_input_label": "//div//label[text()='Password']/following::input[1]",
        "remember_me_checkbox": "//div//input[@type='checkbox']",
        "forgot_password_button": "//div//button[contains(text(),'Forgot password')]",
        "registration_button": "//div//button[contains(text(),'Registration')]",
        "login_button": "//div//button[contains(text(),'Login')]",
        "close_button": "//div//button[@aria-label='Close' or contains(@class,'close')]",

        # Garage
        "garage_header": "//h1[text()='Garage']",
        "add_car_button": "//div//button[contains(text(),'Add car')]",

        # Add Car
        "add_car_header": "//div//*[text()='Add a car']",
        "brand_select_label": "//label[text()='Brand']//following::select[1]",
        "brand_select": "//select[@formcontrolname='brand']",
        "brand_options": "//select[@formcontrolname='brand']/option",
        "brand_option_audi": "//select[@formcontrolname='brand']/option[text()='Audi']",
        "model_select_label": "//label[text()='Model']/following::select[1]",
        "model_select": "//select[@formcontrolname='model']",
        "model_options": "//select[@formcontrolname='model']/option",
        "model_option_r8": "//select[@formcontrolname='model']/option[text()='R8']",
        "add_button": "//button[text()='Add']",
        "cancel_button": "//div[contains(@class,'modal-footer')]//button[text()='Cancel']",
    }

    # -------------------- CSS --------------------
    CSS = {
        # Home
        "guest_login_button": "button.header-link.-guest",
        "signin_button": "button.header_signin",
        "youtube_iframe": "section iframe[src*='youtube'], section iframe[src*='youtu']",
        "home_title": "section h1",
        "signup_button": "button.hero-descriptor_btn",

        # Log In
        "email_input": "#signinEmail",
        "email_input_formcontrol": "input[formcontrolname='email']",
        "password_input": "input[name='password']",
        "remember_me_checkbox": "input[type='checkbox']",
        "forgot_password_button": "button.btn.btn-link",
        "login_button": ".modal button.btn.btn-primary",

        # Garage
        "add_car_button": "button.btn.btn-primary",
        "car_cards": ".car-list .car-item",
        "first_car_card": ".car-list .car-item:first-child",
        "second_car_card": ".car-list .car-item:nth-child(2)",
        "last_car_card": ".car-list .car-item:last-child",
        "car_name": "p.car_name",
        "car_edit_button": ".car-item .btn-edit, .car-item button[class*='edit' i]",

        # Add Car
        "brand_select_id": "select#addCarBrand",
        "model_select_id": "select#addCarModel",
        "brand_select": "select[formcontrolname='brand']",
        "brand_options": "select[formcontrolname='brand'] option",
        "model_select": "select[formcontrolname='model']",
        "model_options": "select[formcontrolname='model'] option",
        "mileage_input": "input[formcontrolname='mileage']",
    }
