from pages.basket_page import BasketPage
from pages.checkout_page import CheckoutPage
from pages.main_page import MainPage
from pages.smartphones_page import SmartphonesPage
from pages.subcategory_page import SubcategoryPage
import allure

@allure.description('Test business path')
def test_business_path(browser):
    print('Старт тест 1')
    mp = MainPage(browser)
    mp.select_city_location()
    mp.select_category_smartphones()
    subp = SubcategoryPage(browser)
    subp.select_category_smartphones()
    smartp = SmartphonesPage(browser)
    smartp.select_input_min_and_max_price()
    smartp.add_product_in_basket()
    bp = BasketPage(browser)
    bp.go_to_checkout()
    cp = CheckoutPage(browser)
    cp.input_making_order()
    browser.quit()
    print('Финиш тест 1')
