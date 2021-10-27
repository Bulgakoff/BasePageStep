import pytest

from .pages.login_page import LoginPage


@pytest.mark.login_guest
class TestLoginFromMainPage():
    def test_guest_can_go_to_login_page(self, browser):
        login_link = "http://selenium1py.pythonanywhere.com/"
        login_page_obj = LoginPage(login_link, browser)
        login_page_obj.open()
        login_page_obj.to_go_login_page()

        login_page_obj.should_be_login_page()
        login_page_obj.register_new_user('hldrfssgsbu@yandex.ru', 'rtghdfrtfbsstyu7866867nb')
        login_page_obj.should_be_authorized_user()

    def test_guest_should_see_login_link(self, browser):
        login_link = "http://selenium1py.pythonanywhere.com/"
        brow_page = LoginPage(login_link, browser)
        brow_page.open()
        brow_page.should_be_login_link()
