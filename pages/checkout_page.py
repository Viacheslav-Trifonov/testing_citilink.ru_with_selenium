import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import allure
from base.base_class import Base
from utilities.logger import Logger


class CheckoutPage(Base):

    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser

    # Локаторы

    firstname = "//input[@name='firstName']"
    lastname = "//input[@name='lastName']"
    phone = "//input[@name='phone']"
    pickup = "//button[@class='ChoiceDeliveryCard__button buttonStyleDecorator buttonStyleDecorator_theme_ghostGray buttonStyleDecorator_size_m buttonStyleDecorator_outlined Button']"
    pickup_point = "//button[@class='OrderDeliveryCard__btn-change buttonStyleDecorator buttonStyleDecorator_theme_ghostGray buttonStyleDecorator_size_s Button']"
    order_confirmation_true = "//button[@class='B2CPaymentLayout__submit-element SubmitButton buttonStyleDecorator buttonStyleDecorator_theme_primary buttonStyleDecorator_size_l Button']"

    # Геттеры

    def get_firstname(self):
        return WebDriverWait(self.browser, 15).until(EC.element_to_be_clickable((By.XPATH, self.firstname)))

    def get_lastname(self):
        return WebDriverWait(self.browser, 15).until(EC.element_to_be_clickable((By.XPATH, self.lastname)))

    def get_phone(self):
        return WebDriverWait(self.browser, 15).until(EC.element_to_be_clickable((By.XPATH, self.phone)))

    def get_pickup(self):
        return self.browser.find_element(By.XPATH, self.pickup)

    def get_pickup_point(self):
        return self.browser.find_elements(By.XPATH, self.pickup_point)[0]

    def get_order_confirmation(self):
        return WebDriverWait(self.browser, 15).until(
            EC.element_to_be_clickable((By.XPATH, self.order_confirmation_true)))

    # Действия

    def input_firstname(self, fname):
        self.get_firstname().send_keys(fname)
        print('Имя заполнено')

    def input_lastname(self, lname):
        self.get_lastname().send_keys(lname)
        print('Фамилия заполнена')

    def input_phone(self, number):
        self.get_phone().send_keys(number)
        print('Номер телефона заполнен')

    def click_get_pickup(self):
        self.get_pickup().click()
        print('Нажата кнопка выбора пунктов самовывоза')

    def select_pickup_point(self):
        self.get_pickup_point().click()
        time.sleep(2)
        self.browser.execute_script("window.scrollBy(0, 10000)")
        print('Выбран пункт самовывоза')

    # Methods

    def input_making_order(self):
        with allure.step('Input making order'):
            Logger.add_start_step(method='input_making_order')
            time.sleep(3)
            self.input_firstname('Иван')
            self.input_lastname('Иванов')
            self.input_phone('89199998877')
            self.click_get_pickup()
            self.select_pickup_point()
            self.assert_url('https://www.citilink.ru/order/checkout/')
            self.precense_button(self.order_confirmation_true)
            self.get_screenshot()
            Logger.add_end_step(url=self.browser.current_url, method='input_making_order')
