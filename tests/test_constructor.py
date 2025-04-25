from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators


class TestConstructorSections:

    def test_click_sauces_section_sauces_selected(self, driver): #проверка перехода к разделу соусы
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.SAUCES)).click()
        selected_section = WebDriverWait(driver, 5).until(EC.presence_of_element_located(Locators.BUNS))
        assert selected_section.is_displayed()


    def test_click_fillings_section_fillings_selected(self, driver): #проверка перехода к разделу соусы
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.FILLINGS)).click()
        selected_section = WebDriverWait(driver, 5).until(EC.presence_of_element_located(Locators.FILLINGS))
        assert selected_section.is_displayed()


    def test_click_buns_section_buns_selected(self, driver): #проверка перехода к разделу булки (
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.SAUCES)).click()
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.BUNS)).click()
        selected_section = WebDriverWait(driver, 5).until(EC.presence_of_element_located(Locators.BUNS))
        assert selected_section.is_displayed()