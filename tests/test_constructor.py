import pytest
from selenium.webdriver.support import expected_conditions as EC

from locators import MainPageLocators


class TestConstructorSections:
    @pytest.mark.parametrize(
        "tab_locator, other_tab_locator",
        [
            pytest.param(MainPageLocators.SAUCES_TAB, MainPageLocators.BUNS_TAB, id="sauces"),
            pytest.param(MainPageLocators.FILLINGS_TAB, MainPageLocators.BUNS_TAB, id="fillings"),
        ],
    )
    def test_go_to_section(self, driver, wait, tab_locator, other_tab_locator):
        wait.until(EC.element_to_be_clickable(tab_locator)).click()

        wait.until(lambda d: MainPageLocators.ACTIVE_TAB_CLASS in d.find_element(*tab_locator).get_attribute("class"))
        assert MainPageLocators.ACTIVE_TAB_CLASS not in driver.find_element(*other_tab_locator).get_attribute("class")

    def test_go_to_buns_section(self, driver, wait):
        # «Булки» активны по умолчанию, поэтому сначала уходим в другой раздел
        wait.until(EC.element_to_be_clickable(MainPageLocators.SAUCES_TAB)).click()
        wait.until(lambda d: MainPageLocators.ACTIVE_TAB_CLASS in d.find_element(*MainPageLocators.SAUCES_TAB).get_attribute("class"))

        driver.find_element(*MainPageLocators.BUNS_TAB).click()

        wait.until(lambda d: MainPageLocators.ACTIVE_TAB_CLASS in d.find_element(*MainPageLocators.BUNS_TAB).get_attribute("class"))
        assert MainPageLocators.ACTIVE_TAB_CLASS not in driver.find_element(*MainPageLocators.SAUCES_TAB).get_attribute("class")
