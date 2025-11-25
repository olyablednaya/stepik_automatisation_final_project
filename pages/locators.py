from selenium.webdriver.common.by import By

# каждый селектор — это пара: как искать и что искать
class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    
#1. В файле locators.py создайте класс LoginPageLocators 
class LoginPageLocators():
    #локаторы для Войти
    LOGIN_EMAIL = (By.CSS_SELECTOR, "#id_login-username")
    LOGIN_PASSWORD = ((By.CSS_SELECTOR, "#id_login-password"))
    
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[name='login_submit']")

    #локаторы для Зарегистрироваться
    REGISTRATION_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTRATION_PASSWORD = (By.CSS_SELECTOR, "input[name='registration-password1'].form-control")
    REGISTRATION_PASSWORD_REPEAT = (By.CSS_SELECTOR, "input[name='registration-password2'].form-control")

    REGISTRATION_BUTTON = (By.CSS_SELECTOR, "button[name='registration_submit']")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
    

#локаторы для страницы товара
class ProductPageLocators():
    ADD_TO_CART_BUTTON = ((By.CSS_SELECTOR, "#add_to_basket_form"))

    #цена и имя на карточке товара
    PRODUCT_NAME = (By.CSS_SELECTOR, '.col-sm-6.product_main h1')
    PRODUCT_PRICE = (By.CSS_SELECTOR, '.col-sm-6.product_main .price_color')

    #цена и имя в уведомлении после добавления в корзину
    NAME_IN_ALERT = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div > strong")
    PRICE_IN_ALERT = (By.CSS_SELECTOR, ".alert-info .alertinner strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR,"#messages > div:nth-child(1)")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")

    CART_LINK = (By.CSS_SELECTOR, "a[href='/en-gb/basket/']")

class CartPageLocators():
    #локатор который ищет сообщение о пустой корзине
    BASKET_EMPTY = (By.ID, "content_inner")
    #сообщение которое выводится в анг версии сайта
    MESSAGE_EMPTY_CART_EN = "Your basket is empty"

    #локатор для корзины когда там есть товары
    BASKET_NOT_EMPTY = (By.CSS_SELECTOR, ".basket-title")
    
    #локатор иконки пользователя, который появляется только после регистрации
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
    
    


    
