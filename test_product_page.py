# файл для тест-кейсов, связанных со страницей товара

from .pages.main_page import MainPage
from .pages.product_page import ProductPage
import time
from .pages.base_page import BasePage



def test_guest_can_add_product_to_basket(browser):
    
    #link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    
    page = ProductPage(browser, link)
    page.open()

    
    #Нажимаем на кнопку "Добавить в корзину"
    
    
    page.adding_product_to_the_cart()

    #Посчитать результат математического выражения и ввести ответ
    page.solve_quiz_and_get_code_orig()
    

    # debug sleep to see what's happening on the page after adding to cart
    time.sleep(15)

    
    #цена товара на карточке и в алерте одинаковые 
    page.product_price_in_alert_same_as_on_product_card()

    #имя товара на карточке и в алерте одинаковые
    page.product_name_in_alert_same_as_on_product_card()

    
    time.sleep(15)
    
