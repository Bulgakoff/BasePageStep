from selenium.common.exceptions import NoSuchElementException

from .base_page import BasePage
from .locators import MainPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def is_present_element(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def should_be_login_url(self):
        assert '/login' in self.browser.current_url,'no'


    def should_be_login_form(self):
        assert self.is_present_element(*MainPageLocators.LOGIN_FORM), f'#login_form element not found'

    def should_be_register_form(self):
        assert self.is_present_element(*MainPageLocators.REGISTER_FORM),f'#register_form element not found'
