import time
from .pages.main_page import MainPage


def test_guest_can_go_to_login_page(browser):
    login_link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(login_link, browser)  # �������������� Page Object, �������� � ����������� ��������� ��������
    browser.get(login_link)   # ��������� ��������
    page.to_go_login_page()     # ��������� ����� �������� � ��������� �� �������� ������
    time.sleep(4)
