#nagative tests for productpage

from .pages.main_page import MainPage
from .pages.product_page import ProductPage
import time
from .pages.base_page import BasePage
import pytest

#негативная проверка: после добавления в корзину НЕ появляется сообщение формата 'Coders at Work был добавлен в вашу корзину'
@pytest.mark.xfail(reason="В задании 4.3 урок 6 сказано отметить ожидаемо упавшие тесты как XFail или skip ")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()

    page.adding_product_to_the_cart()

    #Проверяем, что нет сообщения 'книга такая-то добавлена в корзину' с помощью is_not_element_present
    page.should_not_be_success_message()

#негативная проверка: сообщение формата 'Coders at Work был добавлен в вашу корзину' НЕ появляется на странице ДО добавления в корзину
def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()

#негативная проверка: сообщение формата 'Coders at Work был добавлен в вашу корзину' пропадает через время (видимо по логике НЕ должно)
@pytest.mark.xfail(reason="В задании 4.3 урок 6 сказано отметить ожидаемо упавшие тесты как XFail или skip ")
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()

    page.adding_product_to_the_cart()
    page.should_disappear()