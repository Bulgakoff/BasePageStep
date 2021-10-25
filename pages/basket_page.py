import time

from selenium.common.exceptions import NoSuchElementException
from .locators import MainPageLocators, BasePageLocators
from .base_page import BasePage
from .login_page import LoginPage
from selenium.webdriver.common.by import By


class BasketPage(BasePage):
    def should_be_basket_page(self):
        self.should_be_login_basket_link()
        self.go_to_basket()
        self.should_not_be_basket_items()
        self.should_be_basket_itemtext()
        self.should_be_basket_itemtext_say_empty()
        self.should_be_equal_empty_text()

    def should_be_login_basket_link(self):
        print('should_be_login_baket_link go from Base')
        assert self.is_present_element(*MainPageLocators.BASKET_LINK), 'BASKET_LINK element not found'

    def go_to_basket(self):
        self.browser.find_element(*MainPageLocators.BASKET_LINK).click()

    def should_not_be_basket_items(self):
        assert self.is_not_element_present(
            *MainPageLocators.BASKET_IS_CONTEXT), 'BASKET_IS_CONTEXT element found but not be!'

    def should_be_basket_itemtext(self):
        self.is_present_element(*MainPageLocators.BASKET_IS_TEXT_EMPTY), 'BASKET_IS_TEXT_EMPTY element NOT found!'

    def should_be_basket_itemtext_say_empty(self):
        return self.browser.find_element(*MainPageLocators.BASKET_IS_TEXT_EMPTY).text.split(".")[0]

    def should_be_equal_empty_text(self):
        assert self.should_be_basket_itemtext_say_empty() == "Your basket is empty", \
            'TEXT_EMPTY element NOT equal !'
