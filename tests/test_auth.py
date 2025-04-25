from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from conftest import driver
from locators import Locators
from urls import *


class TestAuthWithExistCreds:

    def test_login_on_main_site(self, driver): #вход по кнопке «Войти в аккаунт» на главной
        driver.find_element(*Locators.LOGIN_MAIN_BUTTON).click()
        assert driver.current_url == login_url


    def test_login_from_personal_account(self, driver): #вход через кнопку «Личный кабинет
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        assert driver.current_url == login_url


    def test_login_from_registration_form(self, driver): #вход через кнопку в форме регистрации
        driver.get(register_url)
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        assert driver.current_url == login_url


    def test_login_from_password_remember_form(self, driver): #вход через кнопку в форме восстановления пароля
        driver.get(forgot_password_url)
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        assert driver.current_url == login_url

class TestLogout:

    def test_logout(self, login): #выход по кнопке «Выйти» в личном кабинете
        login.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(login, 3).until(EC.element_to_be_clickable(Locators.LOGOUT_BUTTON)).click()
        WebDriverWait(login, 3).until(EC.element_to_be_clickable(Locators.LOGIN))
        assert login.current_url == login_url
