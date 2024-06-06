from selenium.webdriver.chrome.webdriver import WebDriver
from functions.functions import create_remove_from_cart_button_locator
from pages.locators import CartPage, Checkout
from pages.login import LoginPage


class Cart(LoginPage):
    def __init__(self, driver: WebDriver, url):
        super().__init__(driver, url)

    cart_locators = CartPage()
    checkout_locators = Checkout()


    def get_item_in_cart_name(self):
        return super().get_text(self.cart_locators.item_name)
    
    
    def click_checkout_button(self):
        super().click_to_element(self.cart_locators.checkout_button)


    def click_remove_button_of_item(self, item_name):
        remove_item_from_cart_locator = create_remove_from_cart_button_locator(item_name)
        super().click_to_element(remove_item_from_cart_locator)

    
    def cart_is_empty(self):
        return not super().element_is_present(self.cart_locators.cart_item)
    

    # Checkout
    def add_user_data(self, first_name, last_name, zip):
        super().fill_in_input_field(self.checkout_locators.first_name, first_name)
        super().fill_in_input_field(self.checkout_locators.last_name, last_name)
        super().fill_in_input_field(self.checkout_locators.zip, zip)

    
    def click_continue_button(self):
        super().click_to_element(self.checkout_locators.continue_button)


    def click_finish_button(self):
        super().click_to_element(self.checkout_locators.finish_button)
    

    def get_title(self):
        return super().get_text(self.checkout_locators.title)
    

    def get_complete_text(self):
        return super().get_text(self.checkout_locators.complete_order)
    