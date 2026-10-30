import pytest
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

import data
from helpers import fill_login_form_and_submit
from locators import MainPageLocators


@pytest.fixture
def driver():
    """Открывает Chrome на главной странице; закрывает браузер после теста."""
    options = Options()
    options.add_argument("--window-size=1920,1080")
    service = Service(ChromeDriverManager().install())
    browser = webdriver.Chrome(service=service, options=options)
    browser.get(data.BASE_URL)
    yield browser
    browser.quit()


@pytest.fixture
def wait(driver):
    """Явное ожидание (10 секунд) для текущего драйвера."""
    return WebDriverWait(driver, 10)


@pytest.fixture
def user():
    """Регистрирует нового пользователя через API и возвращает его данные."""
    credentials = {
        "email": data.generate_email(),
        "password": data.generate_password(),
        "name": data.USER_NAME,
    }
    requests.post(data.API_REGISTER_URL, json=credentials, timeout=10)
    return credentials


@pytest.fixture
def logged_in_driver(driver, wait, user):
    """Драйвер с авторизованным пользователем, открыта главная страница."""
    driver.get(data.LOGIN_URL)
    fill_login_form_and_submit(driver, wait, user)
    wait.until(EC.visibility_of_element_located(MainPageLocators.PLACE_ORDER_BUTTON))
    return driver