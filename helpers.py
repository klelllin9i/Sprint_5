from selenium.webdriver.support import expected_conditions as EC

from locators import LoginPageLocators


def fill_login_form_and_submit(driver, wait, user):
    wait.until(EC.visibility_of_element_located(LoginPageLocators.EMAIL_INPUT)).send_keys(user["email"])
    driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(user["password"])
    driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()