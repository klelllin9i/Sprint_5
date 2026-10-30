from selenium.webdriver.support import expected_conditions as EC

import data
from locators import (ForgotPasswordPageLocators, LoginPageLocators, MainPageLocators,
                      RegistrationPageLocators)


def fill_login_form_and_submit(driver, wait, user):
    wait.until(EC.visibility_of_element_located(LoginPageLocators.EMAIL_INPUT)).send_keys(user["email"])
    driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(user["password"])
    driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()


def assert_logged_in(wait):
    assert wait.until(EC.visibility_of_element_located(MainPageLocators.PLACE_ORDER_BUTTON)).is_displayed()


class TestLogin:
    def test_login_via_login_to_account_button_on_main(self, driver, wait, user):
        wait.until(EC.element_to_be_clickable(MainPageLocators.LOGIN_TO_ACCOUNT_BUTTON)).click()
        fill_login_form_and_submit(driver, wait, user)
        assert_logged_in(wait)

    def test_login_via_personal_account_button(self, driver, wait, user):
        wait.until(EC.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT_LINK)).click()
        fill_login_form_and_submit(driver, wait, user)
        assert_logged_in(wait)

    def test_login_via_button_in_registration_form(self, driver, wait, user):
        driver.get(data.REGISTER_URL)
        wait.until(EC.element_to_be_clickable(RegistrationPageLocators.LOGIN_LINK)).click()
        fill_login_form_and_submit(driver, wait, user)
        assert_logged_in(wait)

    def test_login_via_button_in_forgot_password_form(self, driver, wait, user):
        driver.get(data.FORGOT_PASSWORD_URL)
        wait.until(EC.element_to_be_clickable(ForgotPasswordPageLocators.LOGIN_LINK)).click()
        fill_login_form_and_submit(driver, wait, user)
        assert_logged_in(wait)
