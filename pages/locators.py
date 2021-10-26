from selenium.webdriver.common.by import By


class MainPageLocators():
    # LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')
    ADD_GOOD = (By.CSS_SELECTOR, '.btn.btn-lg.btn-primary.btn-add-to-basket')
    MESSAGE_EXIST_GOOD_ADDION = (By.CSS_SELECTOR, '#messages > div:nth-child(1) > div')
    MESSAGE_NAME_GOOD = (By.CSS_SELECTOR, '#messages > div:nth-child(1) > div > strong')
    NAME_CARD_PRODUCT = (By.CSS_SELECTOR, '.row > div.col-sm-6.product_main > h1')
    MESSAGE_EXIST_PRICE_BASKET_GOOD = (By.CSS_SELECTOR, 'div.alertinner > p:nth-child(1)')
    MESSAGE_PRICE_BASKET_GOOD = (By.CSS_SELECTOR, 'div.alertinner > p:nth-child(1)>strong')
    CARD_PRICE_GOOD = (By.CSS_SELECTOR, 'div.col-sm-6.product_main > p.price_color')
    BASKET_LINK = (By.CSS_SELECTOR, "span.btn-group>a.btn.btn-default")
    BASKET_IS_CONTEXT = (By.CSS_SELECTOR, ".basket-items")
    BASKET_IS_TEXT_EMPTY = (By.CSS_SELECTOR, "#content_inner > p")
    REG_IS_EMAIL_FIELD = (By.CSS_SELECTOR, "#id_registration-email")
    REG_IS_PASSWORD1_FIELD = (By.CSS_SELECTOR, "#id_registration-password1")
    REG_IS_PASSWORD2_FIELD = (By.CSS_SELECTOR, "#id_registration-password2")
    REG_IS_REGISTER_BUTTTON = (By.CSS_SELECTOR, "#register_form > button.btn.btn-lg.btn-primary")
    LOGIN_IS_EMAIL_FIELD = (By.CSS_SELECTOR, "#id_login-username")
    LOGIN_IS_PASSWORD_FIELD = (By.CSS_SELECTOR, "#id_login-password")



class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON  = (By.CSS_SELECTOR, ".icon-user")

