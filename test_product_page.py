
# файл для тест-кейсов, связанных со страницей товара


from .pages.main_page import MainPage
from .pages.product_page import ProductPage

def test_guest_can_add_product_to_basket(browser):

    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    #Нажимаем на кнопку "Добавить в корзину"
    page.adding_product_to_the_cart()

    #Посчитать результат математического выражения и ввести ответ
