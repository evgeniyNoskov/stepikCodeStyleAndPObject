from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LGN_FRM = (By.CSS_SELECTOR, "#login_form")
    REG_FRM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocator():
    ADD_TO_BSKT = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRICE_PRDTCT = (By.CSS_SELECTOR, ".product_main .price_color")
    TOTAL_PRICE_PRDTCT = (By.CSS_SELECTOR, '.basket-mini')
    PRODUCT_NAME = (By.CSS_SELECTOR, "h1")
    RESULT_PRODUCT_NAME = (By.CSS_SELECTOR, ".alertinner strong")