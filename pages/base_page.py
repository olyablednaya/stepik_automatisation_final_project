#base page
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException # в начале файла

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import math


class BasePage():
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self): 
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True
    
    #код для получения проверочного кода к заданию 4.3 урок 2
    def solve_quiz_and_get_code(self):
        try:
            # Ожидаем появления alert
            alert = WebDriverWait(self.browser, 10).until(EC.alert_is_present())
        
            # Получаем текст alert
            x = alert.text.split(" ")[2]
        
            # Вычисляем ответ
            answer = str(math.log(abs((12 * math.sin(float(x))))))

            # Отправляем ответ в alert и принимаем его
            alert.send_keys(answer)
            alert.accept()

        # Ожидаем появления второго alert (если он существует)
            try:
                alert = WebDriverWait(self.browser, 10).until(EC.alert_is_present())
                alert_text = alert.text
                print(f"Your code: {alert_text}")
                alert.accept()

            except NoAlertPresentException:
                print("No second alert presented")

        except NoAlertPresentException:
            print("No alert presented to solve the quiz")
