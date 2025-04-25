import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from urls import *
from data import Credentials
from locators import Locators


@pytest.fixture(scope="function")
def driver():
    options = Options()
    options.add_argument("--window-size=1920,1080")
    browser = webdriver.Chrome(options=options)
    browser.get(main_site)
    yield browser
    browser.quit()


@pytest.fixture(scope='function')
def login(driver):
    driver.get(login_url)
    driver.find_element(*Locators.EMAIL_INPUT).send_keys(Credentials.email)
    driver.find_element(*Locators.PASSWORD_INPUT).send_keys(Credentials.password)
    driver.find_element(*Locators.LOGIN).click()

    return driver
