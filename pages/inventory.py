from selenium.webdriver.chrome.webdriver import WebDriver
from functions.functions import create_add_to_cart_button_locator, create_image_locator
from pages.locators import InventoryPage, ItemCard
from pages.login import LoginPage


class Inventory(LoginPage):
    def __init__(self, driver: WebDriver, url):
        super().__init__(driver, url)

    inventory_locators = InventoryPage()
    card_locators = ItemCard()


    def click_on_item_title(self):
        super().click_to_element(self.inventory_locators.item_name)


    def click_on_item_image(self, item_name):
        item_image_locator = create_image_locator(item_name)
        super().click_to_element(item_image_locator)


    def get_item_name(self) -> str:
        return super().get_text(self.inventory_locators.item_name)
    

    def get_list_of_items(self) -> list:
        return super().get_list(self.inventory_locators.item_name)
    

    def get_list_of_prices_of_items(self) -> list:
        lst = [float(x[1:]) for x in super().get_list(self.inventory_locators.item_price)]
        return lst
        

    def click_add_to_cart_button(self, item_name):
        add_item_to_cart_locator = create_add_to_cart_button_locator(item_name)
        super().click_to_element(add_item_to_cart_locator)

    
    def click_add_to_cart_button_on_item_card(self):
        super().click_to_element(self.card_locators.button_add_to_cart)

    
    def click_remove_button_on_item_card(self):
        super().click_to_element(self.card_locators.button_remove_from_cart)
    

    def click_to_cart_icon(self):
        super().click_to_element(self.inventory_locators.cart_icon)

    
    def item_description_on_card_is_available(self):
        return super().element_is_present(self.card_locators.item_description)
    

    def item_image_on_card_is_available(self):
        return super().element_is_present(self.card_locators.item_img)
    

    def item_price_on_card_is_available(self):
        return super().element_is_present(self.card_locators.item_price)
    

    def inventory_filter(self, value: str):
        match value:
            case "az":
                super().click_to_element(self.inventory_locators.filter_az)
            case "za":
                super().click_to_element(self.inventory_locators.filter_za)
            case "lohi":
                super().click_to_element(self.inventory_locators.filter_lohi)
            case "hilo":
                super().click_to_element(self.inventory_locators.filter_hilo)


    def click_burger_menu(self):
        super().click_to_element(self.inventory_locators.burger_menu_icon)

    
    def click_logout_link(self):
        super().click_to_element(self.inventory_locators.logout_menu_item)

    
    def click_about_link(self):
        super().click_to_element(self.inventory_locators.about_menu_item)

    
    def click_reset_app_state_link(self):
        super().click_to_element(self.inventory_locators.reset_app_menu_item)
        