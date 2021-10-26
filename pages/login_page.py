import time

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from .base_page import BasePage
from .locators import MainPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def register_new_user(self, email=None, password=None, ):
        self.should_be_register_form()

        self.should_be_email_address()
        self.add_value_to_email_address(email)
        # Email address :"#id_registration-email",
        self.should_be_password1()
        self.add_value_to_password1(password)
        # Password:"#id_registration-password1" ,
        self.should_be_password2()
        self.add_value_to_password2(password)
        # Confirm password :"#id_registration-password2"
        self.should_be_register_buttton()
        self.press_register_button()
        # ".btn.btn-lg.btn-primary"

        # here items html check
        # self.add_email_value_to_loginfield_(email)
        # here items html check
        # self.add_pasword_value_to_loginfield_(password)
        # self.press_login_button()
    #

    def is_present_element(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def should_be_login_url(self):
        assert '/login' in self.browser.current_url, 'no'

    def should_be_login_form(self):
        assert self.is_present_element(*MainPageLocators.LOGIN_FORM),\
            f'#login_form element not found'

    def should_be_register_form(self):
        assert self.is_present_element(*MainPageLocators.REGISTER_FORM),\
            f'#register_form element not found'

    def should_be_email_address(self):
        assert self.is_present_element(*MainPageLocators.REG_IS_EMAIL_FIELD),\
            '#EMAIL_FIELD element from rerister area  not found'

    def should_be_password1(self):
        assert self.is_present_element(*MainPageLocators.REG_IS_PASSWORD1_FIELD),\
            '#PASSWORD1_FIELD element from rerister area  not found'

    def should_be_password2(self):
        assert self.is_present_element(*MainPageLocators.REG_IS_PASSWORD2_FIELD),\
            '#PASSWORD2_FIELD element from rerister area  not found'

    def add_value_to_email_address(self, email):
        self.browser.find_element(*MainPageLocators.REG_IS_EMAIL_FIELD).send_keys(email)
        time.sleep(1)

    def add_value_to_password1(self, password):
        self.browser.find_element(*MainPageLocators.REG_IS_PASSWORD1_FIELD).send_keys(password)
        time.sleep(1)

    def add_value_to_password2(self, password):
        self.browser.find_element(*MainPageLocators.REG_IS_PASSWORD2_FIELD).send_keys(password)
        time.sleep(1)

    def should_be_register_buttton(self):
        assert self.is_present_element(*MainPageLocators.REG_IS_REGISTER_BUTTTON), \
            'REGISTER_BUTTTON element from rerister area  not found'

    def press_register_button(self):
        button = WebDriverWait(self.browser, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR,"#register_form > button"))
        )
        button.click()
        # self.browser.find_element(*MainPageLocators.REG_IS_REGISTER_BUTTTON).click()

    def add_email_value_to_loginfield_(self, email):
        self.browser.find_element(*MainPageLocators.LOGIN_IS_EMAIL_FIELD).send_keys(email)

    def add_pasword_value_to_loginfield_(self, password):
        self.browser.find_element(*MainPageLocators.LOGIN_IS_PASSWORD_FIELD).send_keys(password)

    def press_login_button(self):
        button = WebDriverWait(self.browser, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "qweqweqweqweqweqweqweqweqweqweqweeeeeeeeeeeeeeeeeeeeeeee"))
        )
        button.click()
