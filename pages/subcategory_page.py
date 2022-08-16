from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import allure
from base.base_class import Base
from utilities.logger import Logger


class SubcategoryPage(Base):

    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser

    # Локаторы

    select_smartphones = "//a[@href='https://www.citilink.ru/catalog/smartfony/']"

    # Геттеры

    def get_select_category_smartphones(self):
        return WebDriverWait(self.browser, 15).until(EC.element_to_be_clickable((By.XPATH, self.select_smartphones)))

    # Действия

    def click_select_category_smartphones(self):
        self.get_select_category_smartphones().click()
        print('Нажата кнопка выбора подкатегории "Смартфоны"')

    # Методы

    def select_category_smartphones(self):
        with allure.step('Select category smartphones'):
            Logger.add_start_step(method='select_category_smartphones')
            self.click_select_category_smartphones()
            Logger.add_end_step(url=self.browser.current_url, method='select_category_smartphones')
