import time
from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.base_page import BasePage



def test_guest_can_go_to_login_page(browser):
    login_link = "http://selenium1py.pythonanywhere.com/"
    # browser.get(login_link)   # ��������� ��������
    br = BasePage(login_link, browser)
    br.open()
    page = MainPage(login_link, browser)  # ��������������  Page Object(MainPage), �������� � ����������� ��������� ��������
    page.to_go_login_page()     # ��������� ����� �������� � ��������� �� �������� ������
    form_login_register = LoginPage(login_link,browser) # �������������� Page Object(LoginPage), �������� � ����������� ��������� ��������
    form_login_register.should_be_login_url() # ��������� url (�������)
    page.should_be_login_link() # check assert login_link
    form_login_register.should_be_register_form() # check assert register_form
    form_login_register.should_be_login_form() # check assert login_form

