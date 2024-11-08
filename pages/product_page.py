import math
import re
from .base_page import BasePage
from .locators import ProductPageLocator
from selenium.common.exceptions import NoAlertPresentException # в начале файла

class ProductPage(BasePage): 
    def add_to_basket(self):
        bskt_btn = self.browser.find_element(*ProductPageLocator.ADD_TO_BSKT)
        bskt_btn.click() 
        self.solve_quiz_and_get_code()
        self.check_item_in_basket()
        self.check_price_in_basket()

    def check_price_in_basket(self):
        price_prdct = self.browser.find_element(*ProductPageLocator.PRICE_PRDTCT)
        ttl_price_prdct = self.browser.find_element(*ProductPageLocator.TOTAL_PRICE_PRDTCT)
        assert price_prdct.text in ttl_price_prdct.text, 'Цена в корзине не совпадает с заявленной'

    def check_item_in_basket(self):
        product_name = self.browser.find_element(*ProductPageLocator.PRODUCT_NAME)
        result_product_name = self.browser.find_element(*ProductPageLocator.RESULT_PRODUCT_NAME)
        assert product_name.text in result_product_name.text, "Наименование товара не совпадает с заявленным"

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")