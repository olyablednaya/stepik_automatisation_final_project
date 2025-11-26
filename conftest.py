import pytest
from selenium import webdriver

#Считывает значение новой опции командной строки и передаёт его тестам
@pytest.fixture
def language(request):
    return request.config.getoption("--language")

# Фикстура для браузера
#строка ниже идентична @pytest.fixture(scope="function")
@pytest.fixture
def browser(language):
    options = webdriver.ChromeOptions()
    options.add_argument(f"--lang={language}")
    browser = webdriver.Chrome(options=options)
    yield browser
    browser.quit()

#Добавляет новую опцию командной строки (например, --language)
def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en', help="Choose language")