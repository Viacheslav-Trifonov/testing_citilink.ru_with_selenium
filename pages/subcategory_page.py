from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from base.base_class import Base


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
        self.click_select_category_smartphones()
