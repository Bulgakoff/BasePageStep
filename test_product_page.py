# -*- coding: utf-8 -*-
import time

import faker
import pytest

from .pages.login_page import LoginPage
from .pages.base_page import BasePage
from .pages.basket_page import BasketPage
from .pages.product_page import ProductPage


# @pytest.mark.parametrize('login_link',['0', '1', '2', '3', '4', '5', '6', pytest.param('7', marks=pytest.mark.xfail), '8', '9'])
@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser):
    login_link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    brow_page_product = ProductPage(login_link, browser)
    brow_page_product.open()
    brow_page_product.should_be_product_page()


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    login_link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    brow_page_product = ProductPage(login_link, browser)
    brow_page_product.open()
    brow_page_product.should_be_add_button()
    brow_page_product.add_product_to_basket()
    brow_page_product.should_not_be_message_good_addition_after_adding_product_to_basket()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    login_link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    brow = BasePage(login_link, browser)
    brow.open()
    page_product = ProductPage(login_link, browser)
    page_product.should_be_add_button()
    page_product.add_product_to_basket()
    page_product.should_not_be_success_message_disappeared_after_adding_product_to_basket()


def test_guest_should_see_login_link_on_product_page(browser):
    login_link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    brow_page_product = ProductPage(login_link, browser)
    brow_page_product.open()
    brow_page_product.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    login_link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    br_page_product = ProductPage(login_link, browser)
    br_page_product.open()
    br_page_product.should_be_login_link()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    login_link = "http://selenium1py.pythonanywhere.com/en-gb/"
    brow_page = BasketPage(login_link, browser)
    brow_page.open()
    brow_page.should_be_basket_page_1()


@pytest.mark.login_guest
class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        self.login_link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
        self.login_page = LoginPage(self.login_link, browser)
        self.login_page.open()
        self.f = faker.Faker()
        self.email = self.f.email()
        self.password = str(time.time())
        self.login_page.register_new_user(self.email, self.password)
        self.login_page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        login_link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
        brow_page_product = ProductPage(login_link, browser)
        brow_page_product.open()
        brow_page_product.should_not_be_message_good_addition_after_page_open()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        login_link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
        brow_page_product = ProductPage(login_link, browser)
        brow_page_product.open()
        brow_page_product.should_be_product_page()
