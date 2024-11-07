from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LGN_FRM = (By.CSS_SELECTOR, "#login_form")
    REG_FRM = (By.CSS_SELECTOR, "#register_form")
