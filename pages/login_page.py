from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        current_url = self.driver.current_url
        assert 'url' in current_url 

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LGN_FRM), "Login form is not presented"        

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REG_FRM), "Register form is not presented"        