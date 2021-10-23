import time

import pytest

from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.base_page import BasePage
from .pages.product_page import ProductPage

# @pytest.mark.parametrize('login_link',['0','1','2','3','4','5','6', pytest.param('7',marks=pytest.mark.xfail),'8','9'])
# def test_guest_can_add_product_to_basket(browser, login_link):
def test_guest_can_add_product_to_basket(browser):
#     login_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
#     login_link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{login_link}"
    login_link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    # login_link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209"
    browr = BasePage(login_link, browser)
    browr.open()
    page_product = ProductPage(login_link, browser)
    page_product.should_be_product_page()



