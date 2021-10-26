import time

from selenium.common.exceptions import NoSuchElementException
from .locators import MainPageLocators, BasePageLocators
from .base_page import BasePage
from .login_page import LoginPage
from selenium.webdriver.common.by import By


class ProductPage(BasePage):
    def should_be_product_page(self):
        self.should_not_be_message_good_addition_after_page_open()#

        self.should_be_add_button()
        self.add_product_to_basket()

        self.solve_quiz_and_get_code()

        # self.should_not_be_message_good_addition_after_adding_product_to_basket()#
        # self.should_not_be_success_message_disappeared_after_adding_product_to_basket()#

        self.should_be_message_good_addition()
        self.get_message_good_addition()
        self.should_be_name_card_product()
        self.get_name_card_product()
        self.should_be_equal_names()
        self.should_be_message_price_basket()
        self.get_message_price_basket()
        self.should_be_good_price()
        self.get_card_price()
        self.should_be_equal_prices()



    def should_be_add_button(self):
        assert self.is_present_element(*MainPageLocators.ADD_GOOD), \
            'No such element!!!'

    def add_product_to_basket(self):
        self.browser.find_element(*MainPageLocators.ADD_GOOD).click()

    def should_be_message_good_addition(self):
        assert self.is_present_element(*MainPageLocators.MESSAGE_EXIST_GOOD_ADDION), \
            'No such element, as message about good addition!!!'

    def get_message_good_addition(self):
        mess_text = self.browser.find_element(*MainPageLocators.MESSAGE_NAME_GOOD).text
        return mess_text

    def should_be_name_card_product(self):
        assert self.is_present_element(*MainPageLocators.NAME_CARD_PRODUCT), \
            'No such element, as NAME_CARD_PRODUCT!!!'

    def get_name_card_product(self):
        card_text = self.browser.find_element(*MainPageLocators.NAME_CARD_PRODUCT).text
        return card_text

    def should_be_equal_names(self):
        assert self.get_message_good_addition() == self.get_name_card_product(), \
            'The product names do not equal'

    def should_be_message_price_basket(self):
        print('========== check basket price======')
        assert self.is_present_element(*MainPageLocators.MESSAGE_EXIST_PRICE_BASKET_GOOD), \
        'No such element, as PRICE_BASKET_GOOD!!!'

    def get_message_price_basket(self):
        message_price_basket_text = self.browser.find_element(*MainPageLocators.MESSAGE_PRICE_BASKET_GOOD).text
        print(f'===========basket price========>{message_price_basket_text}')
        return message_price_basket_text

    def should_be_good_price(self):
        assert self.is_present_element(*MainPageLocators.CARD_PRICE_GOOD),'No such element, as CARD_PRICE_GOOD!!!'

    def get_card_price(self):
        card_price_text = self.browser.find_element(*MainPageLocators.CARD_PRICE_GOOD).text
        return card_price_text

    def should_be_equal_prices(self):
        assert self.get_message_price_basket()==self.get_card_price(),'The product prices do not equal !'

    def should_not_be_success_message_disappeared_after_adding_product_to_basket(self):
        assert self.is_disappeared(*MainPageLocators.MESSAGE_EXIST_GOOD_ADDION),\
            "Success message is presented and don't dissapeared, but should not be finally"

    def should_not_be_message_good_addition_after_adding_product_to_basket(self):
        assert self.is_not_element_present(*MainPageLocators.MESSAGE_EXIST_GOOD_ADDION),\
            "Success message is presented, but should not be at all"

    def should_not_be_message_good_addition_after_page_open(self):
        assert self.is_not_element_present(*MainPageLocators.MESSAGE_EXIST_GOOD_ADDION)


