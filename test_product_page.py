# файл для тест-кейсов, связанных со страницей товара

from .pages.main_page import MainPage
from .pages.product_page import ProductPage
import time
from .pages.base_page import BasePage
from .pages.login_page import LoginPage

from .pages.basket_page import BasketPage
import pytest

class TestUserAddToBasketFromProductPage():

    @pytest.fixture(scope="function", autouse=True) #фикстура запускается перед каждым тестом данного класса. автоматическая, не нужно передавать аргументом в тест
    def setup(self, browser):
        #открываем стр регистрации
        link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
        page = LoginPage(browser, link)
        page.open()

        page.should_be_login_link()
        page.go_to_login_page()
        
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()

        #регистрируем
        email = str(time.time()) + "@fakemail.org" #для генирации уникального адреса
        password = "passwordpassword333"

        page.register_new_user(email, password)

        #проверяем что пользователь залогинен
        page.check_that_user_logged_in_user_icon()

    #дубликаты уже существующих тестов которые для сдачи финального задания попросили перенести в класс
    
    
    def test_user_can_add_product_to_basket(self, browser):
        #link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    
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

    
    def test_user_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()



#тесты с параметризацией отключены так как отнимают много времени, можно снова их запускать закоментив строку ниже
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

@pytest.mark.skip(reason="Временно отключено")
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

@pytest.mark.skip(reason="Временно отключено") 
def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()
@pytest.mark.skip(reason="Временно отключено")
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


@pytest.mark.skip(reason="Временно отключено")
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()

    #переходим в корзину по по кнопке в шапке
    page.goes_to_сart_by_header_on_page()

     # ТЕПЕРЬ создаём объект BasketPage
    basket_page = BasketPage(browser, browser.current_url)

    # Проверяем отсутствие товаров
    basket_page.check_there_no_products_in_cart()

    # Проверяем сообщение о пустой корзине
    basket_page.check_message_about_empty_string_in_page()




    


    
    


    

    
    
    
