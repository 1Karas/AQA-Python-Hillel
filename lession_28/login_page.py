from selenium.webdriver.common.by import By
from lession_28.base_page import BasePage


class LoginPage(BasePage):
    # Locators
    LOGIN_BUTTON = (By.XPATH, "//button[contains(text(),'Sign up')]")
    EMAIL_INPUT = (By.XPATH, "//input[@id='signupEmail' and @name='email']")
    PASSWORD_INPUT = (By.XPATH, "//input[@id='signupPassword' and @name='password']")
    CONFIRM_PASSWORD_INPUT = (By.XPATH, "//input[@id='signupRepeatPassword' and @name='repeatPassword']")
    NAME_INPUT = (By.XPATH, "//input[@id='signupName' and @name='name']")
    SURNAME_INPUT = (By.XPATH, "//input[@id='signupLastName' and @name='lastName']")
    REGISTER_SUBMIT_BUTTON = (By.XPATH, "//button[@type='button' and contains(text(), 'Register') and @class='btn btn-primary']")
    SUCCESS_MESSAGE = (By.XPATH, "//h1[text()='Garage']")

    # Methods
    def open_registration_form(self):
        self.click_element(self.LOGIN_BUTTON)

    def register_user(self, email, password, name, surname):
        self.enter_text(self.EMAIL_INPUT, email)
        self.enter_text(self.PASSWORD_INPUT, password)
        self.enter_text(self.CONFIRM_PASSWORD_INPUT, password)
        self.enter_text(self.NAME_INPUT, name)
        self.enter_text(self.SURNAME_INPUT, surname)
        self.click_element(self.REGISTER_SUBMIT_BUTTON)

    def verify_success_message(self):
        return self.find_element(self.SUCCESS_MESSAGE).is_displayed()