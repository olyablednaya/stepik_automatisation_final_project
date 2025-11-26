from .base_page import BasePage
from .locators import ProductPageLocators
import time

#2строки ниже нужны для добавления ожидания (кнопка корзины похоже не сразу появляется)
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ProductPage(BasePage):

    def adding_product_to_the_cart(self):
        # Ожидаем, пока кнопка "Добавить в корзину" станет кликабельной
        wait = WebDriverWait(self.browser, 10)
        add_to_cart_button = wait.until(
            EC.element_to_be_clickable(ProductPageLocators.ADD_TO_CART_BUTTON)
        )

        # Проверяем, что кнопка действительно есть
        assert self.is_element_present(*ProductPageLocators.ADD_TO_CART_BUTTON), "Basket button is not presented"
        add_to_cart_button.click()


    def product_price_in_alert_same_as_on_product_card(self):
        
        product_price = self.browser.find_element(
            *ProductPageLocators.PRODUCT_PRICE
        ).text
        product_price_in_alert = self.browser.find_element(
            *ProductPageLocators.PRICE_IN_ALERT
        ).text
        assert (
            product_price == product_price_in_alert
        ), 'The price of the product in the alert does not match the price on the product card'

    def product_name_in_alert_same_as_on_product_card(self):
        product_name = self.browser.find_element(
            *ProductPageLocators.PRODUCT_NAME
        ).text
        product_name_in_alert = self.browser.find_element(
            *ProductPageLocators.NAME_IN_ALERT
        ).text
        assert (
            product_name == product_name_in_alert
        ), 'The name of the product in the alert does not match the name on the product card'

    #метод который проверяет, что элемент не появляется на странице в течение заданного времени
    #ожидаем, что элемент вообще НЕ появится, ни в начале, ни в процессе ожидания
    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    #метод-проверка для is_dicsappeared form base_page
    #ждет пока уже существующий элемент не исчезнет в течение заданного времени
    def should_disappear(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Element '*book name* был добавлен в вашу корзину' did not disappear after timeout 4"