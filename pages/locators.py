from selenium.webdriver.common.by import By

# каждый селектор — это пара: как искать и что искать
class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    
#1. В файле locators.py создайте класс LoginPageLocators 
class LoginPageLocators():
    #локаторы для Войти
    LOGIN_EMAIL = (By.CSS_SELECTOR, "#id_login-username")
    LOGIN_PASSWORD = ((By.CSS_SELECTOR, "#id_login-password"))
    
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[name='login_submit']")

    #локаторы для Зарегистрироваться
    REGISTRATION_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTRATION_PASSWORD = (By.CSS_SELECTOR, "input[name='registration-password1'].form-control")
    REGISTRATION_PASSWORD_REPEAT = (By.CSS_SELECTOR, "input[name='registration-password2'].form-control")

    REGISTRATION_BUTTON = (By.CSS_SELECTOR, "button[name='registration_submit']")
    
    
    


    
