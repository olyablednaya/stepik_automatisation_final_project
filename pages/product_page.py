from .base_page import BasePage
from .locators import ProductPageLocators
import time

#2строки ниже нужны для добавления ожидания (кнопка корзины похоже не сразу появляется)

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#не совсем понимаю что должно передоваться как аргумент в этом классе
#метод для добавления в корзину
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

        #ожидание нужно для появляющегося окна
        # time.sleep(5) 

# 4. дописать методы проерки - пока не понимаю о чем речь
