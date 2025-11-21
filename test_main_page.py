from selenium.webdriver.common.by import By
import time
from .pages.main_page import MainPage
from .pages.base_page import BasePage
from .pages.basket_page import BasketPage

def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                      # открываем страницу
    page.go_to_login_page()          # выполняем метод страницы — переходим на страницу логина

#тест для проверки существования кнопки логина
def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()

"""def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()

    #находим линк на корзину и тыкаем его (метод в бейс пейдж пай)
    page.goes_to_сart_by_header_on_page()

    #ОР что в корзине нет товаров
    page.check_message_about_empty_string_in_page()

    #ОР есть строка о пустой корзине
    page.check_message_about_empty_string_in_page()"""

def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()

    # Переход в корзину
    page.goes_to_сart_by_header_on_page()

    # ТЕПЕРЬ создаём объект BasketPage
    basket_page = BasketPage(browser, browser.current_url)

    # Проверяем отсутствие товаров
    basket_page.check_there_no_products_in_cart()

    # Проверяем сообщение о пустой корзине
    basket_page.check_message_about_empty_string_in_page()

    
    

    
