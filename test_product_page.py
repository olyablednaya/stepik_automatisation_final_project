# файл для тест-кейсов, связанных со страницей товара

from .pages.main_page import MainPage
from .pages.product_page import ProductPage
import time
from .pages.base_page import BasePage
from .pages.login_page import LoginPage
import pytest

@pytest.mark.skip(reason="Временно отключено")
@pytest.mark.parametrize('link', [
    pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"),
    pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1"),
    pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2"),
    pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3"),
    pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4"),
    pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5"),
    pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6"),
    pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail(reason="Ссылка 7 не проходит по условию задания")),
    pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8"),
    pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9")
])


def test_guest_can_add_product_to_basket(browser, link):
    
    #link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    #link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    
    page = ProductPage(browser, link)
    page.open()

    
    #Нажимаем на кнопку "Добавить в корзину"
    
    
    page.adding_product_to_the_cart()

    #Посчитать результат математического выражения и ввести ответ
    page.solve_quiz_and_get_code_orig()
    

    # debug sleep to see what's happening on the page after adding to cart
    #time.sleep(10)

    
    #цена товара на карточке и в алерте одинаковые 
    page.product_price_in_alert_same_as_on_product_card()

    #имя товара на карточке и в алерте одинаковые
    page.product_name_in_alert_same_as_on_product_card()

    
    #time.sleep(10)

    
def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()

    #дальше не понимаю что с чем сравнивать
    #переходим на страницу логина используя go_to_login_page из base_page.py
    page.go_to_login_page()

    #как бы говорим что это - страница логина
    login_page = LoginPage(browser, browser.current_url)


    #сверям с проверками страница логина из login_page.py
    login_page.should_be_login_page()
    
    


    

    
    
    
