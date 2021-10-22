import time
from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.base_page import BasePage



def test_guest_can_go_to_login_page(browser):
    login_link = "http://selenium1py.pythonanywhere.com/"
    # login_link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    # browser.get(login_link)   # открываем страницу
    br = BasePage(login_link, browser)
    br.open()
    page = MainPage(login_link, browser)  # инициализируем  Page Object(MainPage), передаем в конструктор экземпл€р драйвера
    page.to_go_login_page()     # выполн€ем метод страницы Ч переходим на страницу логина
    login_page_obj = LoginPage(login_link,browser) # инициализируем Page Object(LoginPage), передаем в конструктор экземпл€р драйвера
    # проинициализировали в функции to_go_login_page(классе MainPage)
    page.should_be_login_link() # check assert login_link

    login_page_obj.should_be_login_page()
    # login_page_obj.should_be_login_url() # провер€ем url (текущий)
    # login_page_obj.should_be_register_form() # check assert register_form
    # login_page_obj.should_be_login_form() # check assert login_form
    # login_page_obj.solve_quiz_and_get_code()


