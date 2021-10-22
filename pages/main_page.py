import time

from selenium.common.exceptions import NoSuchElementException
from .locators import MainPageLocators
from .base_page import BasePage
from .login_page import LoginPage
from selenium.webdriver.common.by import By

class MainPage(BasePage):
    def to_go_login_page(self):
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()
        # return LoginPage(url=self.browser.current_url, browser=self.browser)
        # alert =self.browser.switch_to.alert
        # alert.accept()




    def is_present_element(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True


    def should_be_login_link(self):
        assert self.is_present_element(*MainPageLocators.LOGIN_LINK), 'element not found'


