# -*- coding: utf-8 -*-
import time

import pytest

from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.base_page import BasePage
from .pages.basket_page import BasketPage
from .pages.product_page import ProductPage


@pytest.mark.parametrize('login_link',
                         ['0', '1', '2', '3', '4', '5', '6', pytest.param('7', marks=pytest.mark.xfail), '8', '9'])
def test_guest_can_add_product_to_basket(browser, login_link):
    # def test_guest_can_add_product_to_basket(browser):
    #     login_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    #     login_link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{login_link}"
    login_link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    # login_link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209"
    brow_page_product = ProductPage(login_link, browser)
    brow_page_product.open()
    brow_page_product.should_be_product_page()


...


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    # *Открываем страницу товара
    # *Добавляем товар в корзину
    # *Проверяем, что нет сообщения об успехе с помощью is_not_element_present

    login_link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    brow_page_product = ProductPage(login_link, browser)
    brow_page_product.open()
    brow_page_product.should_be_add_button()
    brow_page_product.add_product_to_basket()
    brow_page_product.should_not_be_message_good_addition_after_adding_product_to_basket()


def test_guest_cant_see_success_message(browser):
    # *Открываем страницу товара (только)
    # *Проверяем, что нет сообщения об успехе с помощью is_not_element_present

    login_link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    brow_page_product = ProductPage(login_link, browser)
    brow_page_product.open()
    brow_page_product = ProductPage(login_link, browser)
    # brow_page_product.should_not_be_message_good_addition_after_page_open()
    brow_page_product.should_be_login_link()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    # *Открываем страницу товара
    # *Добавляем товар в корзину
    # *Проверяем, что нет сообщения об успехе с помощью is_disappeared
    login_link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    brow = BasePage(login_link, browser)
    brow.open()
    page_product = ProductPage(login_link, browser)
    page_product.should_be_add_button()
    page_product.add_product_to_basket()
    page_product.should_not_be_success_message_disappeared_after_adding_product_to_basket()


#

def test_guest_should_see_login_link_on_product_page(browser):
    login_link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    brow_page_product = ProductPage(login_link, browser)
    brow_page_product.open()
    brow_page_product.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(browser):
    login_link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    br_page_product = ProductPage(login_link, browser)
    br_page_product.open()
    br_page_product.should_be_login_link()


"""
--------------->Гость открывает страницу товара
--------------->Переходит в корзину по кнопке в шапке 
--------------->жидаем, что в корзине нет товаров
--------------->Ожидаем, что есть текст о том что корзина пуста 
"""


def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    login_link = "http://selenium1py.pythonanywhere.com/en-gb/"
    brow_page = BasketPage(login_link, browser)
    brow_page.open()
    brow_page.should_be_basket_page_1()
