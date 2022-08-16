from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import allure
from base.base_class import Base
from utilities.logger import Logger


class BasketPage(Base):

    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser

    # Локаторы

    making_order = "//button[@data-label='Перейти к оформлению']"

    # Геттеры

    def move_to_making_order(self):
        return WebDriverWait(self.browser, 15).until(EC.element_to_be_clickable((By.XPATH, self.making_order)))

    # Actions

    def click_move_to_making_order(self):
        self.move_to_making_order().click()
        print('Нажата кнопка "Перейти к оформлению"')

    # Методы

    def go_to_checkout(self):
        with allure.step('Go to checkout'):
            Logger.add_start_step(method='go_to_checkout')
            self.click_move_to_making_order()
            Logger.add_end_step(url=self.browser.current_url, method='go_to_checkout')
