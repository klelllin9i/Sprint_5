from selenium.webdriver.support import expected_conditions as EC

import data
from locators import LoginPageLocators, RegistrationPageLocators


class TestRegistration:
    def test_successful_registration(self, driver, wait):
        driver.get(data.REGISTER_URL)
        wait.until(EC.visibility_of_element_located(RegistrationPageLocators.NAME_INPUT)).send_keys(data.USER_NAME)
        driver.find_element(*RegistrationPageLocators.EMAIL_INPUT).send_keys(data.generate_email())
        driver.find_element(*RegistrationPageLocators.PASSWORD_INPUT).send_keys(data.generate_password(6))
        driver.find_element(*RegistrationPageLocators.REGISTER_BUTTON).click()

        assert wait.until(EC.url_to_be(data.LOGIN_URL))
        assert wait.until(EC.visibility_of_element_located(LoginPageLocators.HEADING)).is_displayed()

    def test_registration_with_short_password_shows_error(self, driver, wait):
        driver.get(data.REGISTER_URL)
        wait.until(EC.visibility_of_element_located(RegistrationPageLocators.NAME_INPUT)).send_keys(data.USER_NAME)
        driver.find_element(*RegistrationPageLocators.EMAIL_INPUT).send_keys(data.generate_email())
        driver.find_element(*RegistrationPageLocators.PASSWORD_INPUT).send_keys(data.generate_password(5))
        driver.find_element(*RegistrationPageLocators.REGISTER_BUTTON).click()

        assert wait.until(EC.visibility_of_element_located(RegistrationPageLocators.PASSWORD_ERROR)).is_displayed()
        assert driver.current_url == data.REGISTER_URL