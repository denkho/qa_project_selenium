from pages.inventory import Inventory
from src.urls import Urls


def test_transition_item_cart_after_click_item_image(driver):
    """Tests transition to the Item Card upon click
    on item image in Inventory"""
    # Test steps

    page = Inventory(driver, Urls.base)

    page.open()
    page.login()
    
    item_name = page.get_item_name()

    page.click_on_item_title()
    card_item_name = page.get_item_name()
    
    assert item_name == card_item_name,  f"Item in Inventory was - {item_name}, but Item in the card is - {card_item_name}"
    assert page.item_description_on_card_is_available(), "There is no Item description on Item Card Page"
    assert page.item_image_on_card_is_available(), "There is no Item image on Item Card Page"
    assert page.item_price_on_card_is_available(), "There is no Item price on Item Card Page"



def test_transition_item_cart_after_click_item_name(driver):
    """Tests transition to the Item Card upon click
    on item name in Inventory"""
    
    # Test steps

    page = Inventory(driver, Urls.base)

    page.open()
    page.login()
    
    item_name = page.get_item_name()

    page.click_on_item_image(item_name)
    
    card_item_name = page.get_item_name()
    
    assert item_name == card_item_name,  f"Item in Inventory was - {item_name}, but Item in the card is - {card_item_name}"
    assert page.item_description_on_card_is_available(), "There is no Item description on Item Card Page"
    assert page.item_image_on_card_is_available(), "There is no Item image on Item Card Page"
    assert page.item_price_on_card_is_available(), "There is no Item price on Item Card Page"
