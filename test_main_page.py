import time

import pytest

from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.base_page import BasePage

@pytest.mark.login_guest
class TestLoginFromMainPage():
    def test_guest_can_go_to_login_page(self, browser):
        login_link = "http://selenium1py.pythonanywhere.com/"
        # login_link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
        login_page_obj = LoginPage(login_link, browser)
        login_page_obj.open()
        login_page_obj.to_go_login_page()   # выполняем метод страницы — переходим на страницу логина

        login_page_obj.should_be_login_page()
        # login_page_obj.should_be_login_url() # проверяем url (текущий)
        # login_page_obj.should_be_register_form() # check assert register_form
        # login_page_obj.should_be_login_form() # check assert login_form
        # login_page_obj.solve_quiz_and_get_code()
        login_page_obj.register_new_user('hldrfssgsbu@yandex.ru','rtghdfrtfbsstyu7866867nb')
        login_page_obj.should_be_authorized_user()

    def test_guest_should_see_login_link(self, browser):
        login_link = "http://selenium1py.pythonanywhere.com/"
        brow_page = LoginPage(login_link, browser)
        brow_page.open()
        brow_page.should_be_login_link()
