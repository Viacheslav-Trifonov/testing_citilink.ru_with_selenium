import time

from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from base.base_class import Base


class SmartphonesPage(Base):

    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser

    # Локаторы

    price_min = "//input[@class='e10fhmjh0 css-a7ozb0 e1rnnvis0']"
    price_max = "//input[@class='epja35w0 css-a7ozb0 e1rnnvis0']"
    all_product_in_basket = "//button[@data-label='В корзину']"
    dont_show = "//label[@class='Checkbox UpsaleBasket__checkbox js--UpsaleBasket__checkbox ']"
    continue_purchases = "//button[@data-label='Продолжить покупки']"
    basket = "//div[@data-name='basket']"

    # Геттеры

    def get_price_min(self):
        return self.browser.find_elements(By.XPATH, self.price_min)[1]

    def get_price_max(self):
        return self.browser.find_elements(By.XPATH, self.price_max)[1]

    def get_product_1_add_basket(self):
        return self.browser.find_elements(By.XPATH, self.all_product_in_basket)[0]

    def get_product_2_add_basket(self):
        return self.browser.find_elements(By.XPATH, self.all_product_in_basket)[2]

    def get_dont_show(self):
        return WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable(
            (By.XPATH, self.dont_show)))

    def get_continue_purchases(self):
        return WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable(
            (By.XPATH, self.continue_purchases)))

    def move_to_basket(self):
        return WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable((By.XPATH, self.basket)))

    # Действия

    def clear_price_min(self):
        self.get_price_min().clear()
        print('Удалён порог дефолтной минимальной цены')

    def clear_price_max(self):
        self.get_price_max().clear()
        print('Удалён порог дефолтной максимальной цены')

    def input_price_min(self, minprice):
        action = ActionChains(self.browser)
        self.get_price_min().send_keys(minprice)
        action.send_keys(Keys.RETURN).perform()
        time.sleep(2)
        print('Введен порог минимальной цены')

    def input_price_max(self, maxprice):
        action = ActionChains(self.browser)
        self.get_price_max().send_keys(maxprice)
        action.send_keys(Keys.RETURN).perform()
        time.sleep(2)
        print('Введен порог максимальной цены')

    def add_prod_1_in_basket(self):
        self.get_product_1_add_basket().click()
        print('Товар №1 добавлен в козину')

    def add_prod_2_in_basket(self):
        self.browser.execute_script("window.scrollBy(0, 500)")
        self.get_product_2_add_basket().click()
        print('Товар №2 добавлен в козину')

    def disable_option_menu(self):
        self.get_dont_show().click()
        self.get_continue_purchases().click()
        print('Меню выбора доп. опций отключено')

    def click_move_to_basket(self):
        self.move_to_basket().click()
        print('Нажата кнопка перехода в корзину')

    # Методы

    def select_input_min_and_max_price(self):
        self.clear_price_min()
        self.input_price_min('12000')
        self.clear_price_max()
        self.input_price_max('45000')

    def add_product_in_basket(self):
        self.add_prod_1_in_basket()
        self.disable_option_menu()

        self.add_prod_2_in_basket()
        self.click_move_to_basket()
