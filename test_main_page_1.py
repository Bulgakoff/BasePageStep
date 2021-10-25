# -*- coding: utf-8 -*-
import time
from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.base_page import BasePage
from .pages.basket_page import BasketPage
from .pages.product_page import ProductPage
"""
# Гость открывает главную страницу 
# Переходит в корзину по кнопке в шапке сайта "span.btn-group>a.btn.btn-default"
# Ожидаем, что в корзине нет товаров ".basket-items"
# Ожидаем, что есть текст о том что корзина пуста "#content_inner > p"
"""

def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    login_link = "http://selenium1py.pythonanywhere.com/en-gb/"
    brow_page = BasketPage(login_link, browser)
    brow_page.open()
    brow_page.should_be_basket_page_1()


