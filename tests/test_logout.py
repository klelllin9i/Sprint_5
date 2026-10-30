from selenium.webdriver.support import expected_conditions as EC

import data
from locators import LoginPageLocators, MainPageLocators, ProfilePageLocators


class TestLogout:
    def test_logout_from_personal_account(self, logged_in_driver, wait):
        logged_in_driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_LINK).click()
        wait.until(EC.element_to_be_clickable(ProfilePageLocators.LOGOUT_BUTTON)).click()

        wait.until(EC.url_to_be(data.LOGIN_URL))
        assert wait.until(EC.visibility_of_element_located(LoginPageLocators.HEADING)).is_displayed()
