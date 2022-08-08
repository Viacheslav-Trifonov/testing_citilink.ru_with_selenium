import datetime

from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class Base:

    def __init__(self, browser):
        self.browser = browser

    """Получение текущего URL"""

    def get_current_url(self):
        get_url = self.browser.current_url
        print(f'Текущий URL: {get_url}')

    """Проверка наличия надписи на странице"""

    def assert_word(self, word, result):
        value_word = word.text
        assert value_word == result
        print('Проверка по слову: Совпадает')

    """Совпадение URL"""

    def assert_url(self, result):
        get_url = self.browser.current_url
        assert result == get_url
        print('URL совпадает')

    """Создание скриншота"""

    def get_screenshot(self):
        now_date = datetime.datetime.utcnow().strftime('%Y.%m.%d.%H.%M.%S')
        name_screenshot = 'screenshot' + now_date + '.png'
        self.browser.save_screenshot('D:\\' + name_screenshot)
        print('Скриншот сделан')

    """Наличие кнопки на странице"""

    def precense_button(self, button):
        try:
            WebDriverWait(self.browser, 3).until(EC.element_to_be_clickable((By.XPATH, button)))
            print('Кнопка активна')
        except TimeoutException:
            print('Такой кнопки нет на странице')
