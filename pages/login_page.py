from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()


    #В методе should_be_login_url реализуйте проверку, что подстрока "login" есть в текущем url браузера.
    #Для этого используйте соответствующее свойство Webdriver (driver.current_url)  

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "Login substring is not present in the current URL"

    def should_be_login_form(self):
        #пример синтаксиса assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"
        #реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_EMAIL), "Login email field is not presented"
        assert self.is_element_present(*LoginPageLocators.LOGIN_PASSWORD), "Login password field is not presented"
        assert self.is_element_present(*LoginPageLocators.LOGIN_BUTTON), "Login button is not presented"

    def should_be_register_form(self):
        #реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_EMAIL), "Registration email field is not presented"
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_PASSWORD), "Registration password field is not presented"
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_PASSWORD_REPEAT), "Registration password repeat field is not presented"
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_BUTTON), "Registration button is not presented"
