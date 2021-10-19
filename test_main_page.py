import time
from .pages.main_page import MainPage


def test_guest_can_go_to_login_page(browser):
    login_link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(login_link, browser)  # инициализируем Page Object, передаем в конструктор экземпл€р драйвера
    browser.get(login_link)   # открываем страницу
    page.to_go_login_page()     # выполн€ем метод страницы Ч переходим на страницу логина
    time.sleep(4)
