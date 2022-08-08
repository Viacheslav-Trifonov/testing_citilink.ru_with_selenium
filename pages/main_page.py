from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from base.base_class import Base


class MainPage(Base):

    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser

    # Локаторы

    select_location = "//button[@class='js--CitiesSearch-trigger MainHeader__open-text TextWithIcon']"
    input_city = "//input[@placeholder='Введите название города']"
    choose_city = "//span[@class='CitiesSearch__highlight']"
    product_catalog = "//button[@data-label='Каталог товаров']"
    cat_mobile = "//a[@data-category-alias='mobile']"

    # Геттеры

    def get_select_location(self):
        return WebDriverWait(self.browser, 15).until(EC.element_to_be_clickable((By.XPATH, self.select_location)))

    def get_input_city(self):
        return WebDriverWait(self.browser, 15).until(EC.element_to_be_clickable((By.XPATH, self.input_city)))

    def get_choose_city(self):
        return WebDriverWait(self.browser, 15).until(EC.element_to_be_clickable((By.XPATH, self.choose_city)))

    def get_product_catalog(self):
        return WebDriverWait(self.browser, 15).until(EC.element_to_be_clickable((By.XPATH, self.product_catalog)))

    def get_cat_smartphones(self):
        return WebDriverWait(self.browser, 15).until(EC.element_to_be_clickable((By.XPATH, self.cat_mobile)))

    # Действия

    def click_select_location(self):
        self.get_select_location().click()
        print('Нажата кнопка выбора города')

    def click_input_city(self, city):
        self.get_input_city().send_keys(city)
        print('Ввод названия города')

    def click_choose_city(self):
        self.get_choose_city().click()
        print('Нажата кнопка подтверждения выбранного города')

    def click_product_catalog(self):
        self.get_product_catalog().click()
        print('Нажата кнопка открытия каталога товаров')

    def click_cat_smartphones(self):
        self.get_cat_smartphones().click()
        print('Нажата кнопка выбора категории "Смартфоны и гаджеты"')

    # Methods

    def select_city_location(self):
        self.click_select_location()
        self.click_input_city('Казань')
        self.click_choose_city()

    def select_category_smartphones(self):
        self.click_product_catalog()
        self.click_cat_smartphones()
