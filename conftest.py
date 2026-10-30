import pytest
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

import data
from locators import LoginPageLocators, MainPageLocators


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
    response = requests.post(data.API_REGISTER_URL, json=credentials, timeout=10)
    assert response.status_code == 200, f"Не удалось создать пользователя: {response.text}"
    return credentials


@pytest.fixture
def logged_in_driver(driver, wait, user):
    """Драйвер с авторизованным пользователем, открыта главная страница."""
    driver.get(data.LOGIN_URL)
    wait.until(EC.visibility_of_element_located(LoginPageLocators.EMAIL_INPUT)).send_keys(user["email"])
    driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(user["password"])
    driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
    wait.until(EC.visibility_of_element_located(MainPageLocators.PLACE_ORDER_BUTTON))
    return driver