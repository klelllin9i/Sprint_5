from selenium.webdriver.support import expected_conditions as EC

import data
from locators import MainPageLocators, ProfilePageLocators


class TestPersonalAccount:
    def test_go_to_personal_account(self, logged_in_driver, wait):
        logged_in_driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_LINK).click()

        wait.until(EC.url_to_be(data.PROFILE_URL))
        assert wait.until(EC.visibility_of_element_located(ProfilePageLocators.LOGOUT_BUTTON)).is_displayed()

    def test_go_to_constructor_from_personal_account_by_constructor_link(self, logged_in_driver, wait):
        logged_in_driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_LINK).click()
        wait.until(EC.url_to_be(data.PROFILE_URL))

        logged_in_driver.find_element(*MainPageLocators.CONSTRUCTOR_LINK).click()

        assert wait.until(EC.visibility_of_element_located(MainPageLocators.MAKE_BURGER_HEADING)).is_displayed()
        assert logged_in_driver.current_url == data.BASE_URL

    def test_go_to_constructor_from_personal_account_by_logo(self, logged_in_driver, wait):
        logged_in_driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_LINK).click()
        wait.until(EC.url_to_be(data.PROFILE_URL))

        logged_in_driver.find_element(*MainPageLocators.LOGO).click()

        assert wait.until(EC.visibility_of_element_located(MainPageLocators.MAKE_BURGER_HEADING)).is_displayed()
        assert logged_in_driver.current_url == data.BASE_URL
