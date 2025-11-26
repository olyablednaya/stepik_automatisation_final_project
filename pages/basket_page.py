from .base_page import BasePage
from .locators import LoginPageLocators
from .locators import CartPageLocators

class BasketPage(BasePage):
    #под вопросом, должен ли инит для класса баскет пейдж чем-то отличаться от например бейс пейдж
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)
        
        
    # метод 1 проверяет ТЕКСТ, что корзина пуста
    def check_message_about_empty_string_in_page(self):
        empty_basket_message = CartPageLocators.MESSAGE_EMPTY_CART_EN
        assert empty_basket_message in self.browser.find_element(*CartPageLocators.BASKET_EMPTY).text, "There is no message 'Your basket is empty' on page"

    #метод 2 проверяет, что корзина пуста
    def check_there_no_products_in_cart(self):
        assert self.is_not_element_present(*CartPageLocators.BASKET_NOT_EMPTY), "There are items in the cart that shouldn't be there"