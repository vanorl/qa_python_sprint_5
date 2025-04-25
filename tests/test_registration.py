from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from helper import generate_registration_data
from locators import Locators
from urls import *


class TestRegistrationWithNewCredentials:

    def test_registration_success(self, driver):
        name, email, password = generate_registration_data()
        driver.find_element(*Locators.LOGIN_MAIN_BUTTON).click()
        driver.find_element(*Locators.REG_BUTTON).click()
        driver.find_element(*Locators.NAME_FIELD).send_keys(name)
        driver.find_element(*Locators.EMAIL_FIELD).send_keys(email)
        driver.find_element(*Locators.PASSWORD_FIELD).send_keys(password)
        driver.find_element(*Locators.CONTINUE_REG_BUTTON).click()
        WebDriverWait(driver, 1).until(EC.element_to_be_clickable(Locators.LOGIN))

        assert driver.current_url == login_url


    def test_registration_short_password_invalid_password_message_given(self, driver):
        short_pass = True
        name, email, password = generate_registration_data(short_pass)
        driver.find_element(*Locators.LOGIN_MAIN_BUTTON).click()
        driver.find_element(*Locators.REG_BUTTON).click()
        driver.find_element(*Locators.NAME_FIELD).send_keys(name)
        driver.find_element(*Locators.EMAIL_FIELD).send_keys(email)
        driver.find_element(*Locators.PASSWORD_FIELD).send_keys(password)
        driver.find_element(*Locators.CONTINUE_REG_BUTTON).click()

        assert WebDriverWait(driver, 1).until(EC.visibility_of_element_located(Locators.INVALID_PASSWORD_MESSAGE)).text == 'Некорректный пароль'
        assert driver.current_url == register_url
