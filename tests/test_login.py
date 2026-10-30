from selenium.webdriver.support import expected_conditions as EC

import data
from helpers import fill_login_form_and_submit
from locators import (ForgotPasswordPageLocators, MainPageLocators,
                      RegistrationPageLocators)


class TestLogin:
    def test_login_via_login_to_account_button_on_main(self, driver, wait, user):
        wait.until(EC.element_to_be_clickable(MainPageLocators.LOGIN_TO_ACCOUNT_BUTTON)).click()
        fill_login_form_and_submit(driver, wait, user)
        assert wait.until(EC.visibility_of_element_located(MainPageLocators.PLACE_ORDER_BUTTON)).is_displayed()

    def test_login_via_personal_account_button(self, driver, wait, user):
        wait.until(EC.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT_LINK)).click()
        fill_login_form_and_submit(driver, wait, user)
        assert wait.until(EC.visibility_of_element_located(MainPageLocators.PLACE_ORDER_BUTTON)).is_displayed()

    def test_login_via_button_in_registration_form(self, driver, wait, user):
        driver.get(data.REGISTER_URL)
        wait.until(EC.element_to_be_clickable(RegistrationPageLocators.LOGIN_LINK)).click()
        fill_login_form_and_submit(driver, wait, user)
        assert wait.until(EC.visibility_of_element_located(MainPageLocators.PLACE_ORDER_BUTTON)).is_displayed()

    def test_login_via_button_in_forgot_password_form(self, driver, wait, user):
        driver.get(data.FORGOT_PASSWORD_URL)
        wait.until(EC.element_to_be_clickable(ForgotPasswordPageLocators.LOGIN_LINK)).click()
        fill_login_form_and_submit(driver, wait, user)
        assert wait.until(EC.visibility_of_element_located(MainPageLocators.PLACE_ORDER_BUTTON)).is_displayed()