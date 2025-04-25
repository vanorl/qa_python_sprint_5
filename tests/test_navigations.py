from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators
from urls import *


class TestHeaderNavigation:

    def test_click_personal_account_navigates_to_profile(self, login): #переход по клику на «Личный кабинет»
        login.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(login, 1).until(EC.element_to_be_clickable(Locators.LOGOUT_BUTTON))
        assert login.current_url == personal_account_url


    def test_click_constructor_from_personal_account_navigates_to_constructor(self, login): #переход по клику на «Конструктор» из Личного кабинета
        login.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(login, 1).until(EC.element_to_be_clickable(Locators.CONSTRUCTOR_BUTTON)).click()
        assert login.current_url == main_site

    def test_click_logo_from_personal_account_navigates_to_constructor(self, login): #переход в конструктор по клику на логотип из Личного кабинета
        login.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(login, 1).until(EC.element_to_be_clickable(Locators.LOGO_BUTTON)).click()
        assert login.current_url == main_site
