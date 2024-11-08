import time
from .pages.main_page import MainPage
from .pages.product_page import ProductPage

def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = MainPage(browser, link)
    page.open()
    product_page = ProductPage(browser, browser.current_url)
    # product_page = ProductPage(browser, link)
    product_page.add_to_basket()
    # time.sleep(3000)

#messages > div:nth-child(1) > div.alertinner  > strong
# $('.alertinner')