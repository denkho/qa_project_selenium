from pages.cart import Cart
from pages.inventory import Inventory
from pages.locators import CartPage
from src.urls import Urls


def test_add_item_to_cart_from_inventory(driver):
    """Test verifies the function of item add to cart from inventory.
    """

    # Test steps

    page = Inventory(driver, Urls.base)

    page.open()
    page.login()
    
    item_name = page.get_item_name()
    page.click_add_to_cart_button(item_name)

    page.click_to_cart_icon()

    cart_page = Cart(driver, Urls.base)
    item_in_cart = cart_page.get_item_in_cart_name()
    
    assert page.element_is_visible(CartPage.cart_item), "There is nothing in the cart"
    assert item_in_cart == item_name, f"Item added to cart is {item_name}, but cart has {item_in_cart}"


def test_delete_item_from_cart(driver):
    """Tests the function of deleting item added to cart
    from the cart"""

    # Test preconditions
    # Login & add item to the cart
    page = Inventory(driver, Urls.base)
    page.open()
    page.login()
    item_name = page.get_item_name()
    page.click_add_to_cart_button(item_name)

    # Test steps
    cart_page = Cart(driver, Urls.cart)
    cart_page.open()
    
    cart_page.click_remove_button_of_item(item_name)
    
    assert cart_page.cart_is_empty(), "The cart is not empty"


def test_add_item_to_cart_from_item_card(driver):
    """Tests the function of adding item to the cart from Item Card"""

    # Test steps

    page = Inventory(driver, Urls.base)
    page.open()
    page.login()
    page.click_on_item_title()

    item_name = page.get_item_name()
    page.click_add_to_cart_button_on_item_card()

    page.click_to_cart_icon()

    cart_page = Cart(driver, Urls.base)
    item_in_cart = cart_page.get_item_in_cart_name()
    
    assert page.element_is_visible(CartPage.cart_item), "There is nothing in the cart"
    assert item_in_cart == item_name, f"Item added to cart is {item_name}, but cart has {item_in_cart}"


def test_delete_item_from_cart_through_item_card(driver):
    """Tests the function of deleting item added to cart
    from the item card"""

    # Test preconditions
    # Login & add item to the cart
    page = Inventory(driver, Urls.base)
    page.open()
    page.login()
    item_name = page.get_item_name()
    page.click_add_to_cart_button(item_name)
    page.click_on_item_title()

    # Test steps

    page.click_remove_button_on_item_card()

    cart_page = Cart(driver, Urls.cart)
    cart_page.open()
    
    assert cart_page.cart_is_empty(), "The cart is not empty"