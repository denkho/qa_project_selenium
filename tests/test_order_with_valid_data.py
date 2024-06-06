from pages.cart import Cart
from pages.inventory import Inventory
from src.urls import Urls


def test_order_with_valid_data(driver):
    """Test of order placing with valid data"""

    # Test data

    first_name = 'David'
    last_name = 'Jacobson'
    zip = '123456'

    complete_title_text = 'Checkout: Complete!'
    complete_text = 'Thank you for your order!'
    

    # Test Preconditions
    # Add item to the cart

    page = Inventory(driver, Urls.base)
    page.open()
    page.login()

    item_name = page.get_item_name()
    page.click_add_to_cart_button(item_name)

    page.click_to_cart_icon()

    # Test steps

    cart_page = Cart(driver, Urls.cart)
    cart_page.click_checkout_button()

    cart_page.add_user_data(first_name, last_name, zip)
    cart_page.click_continue_button()
    cart_page.click_finish_button()

    title_text = cart_page.get_title()
    complete_text_actual = cart_page.get_complete_text()

    assert title_text == complete_title_text, f"Checkout complete title is {title_text}, but has to be - {complete_title_text}"
    assert complete_text_actual == complete_text, f"Checkout complete title is {complete_text_actual}, \
                                                    but has to be - {complete_text}"
