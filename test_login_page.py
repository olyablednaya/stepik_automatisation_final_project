#тесты для стрница логина и регистрации

from selenium.webdriver.common.by import By
import time
from .pages.login_page import LoginPage

#тест для проверки существования формы логина (проверяется существования полей и кнопки)
def test_login_form_exist(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_form()

#тест для проверки существования формы регистрации (проверяется существования полей и кнопки)
def test_registration_form_exist(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
    page = LoginPage(browser, link)
    page.open()
    page.should_be_register_form()

#тест строка login есть в текущем url браузера
def test_str_login_exist_in_current_url(browser):
    link  = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_url()
    




    
    
    
    
