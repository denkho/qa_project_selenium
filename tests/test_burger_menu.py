from pages.cart import Cart
from pages.inventory import Inventory
from pages.locators import Login
from src.urls import Urls


def test_logout(driver):
    """Test of burger menu logout item click"""

    # Test Preconditionsf
    page = Inventory(driver, Urls.base)
    page.open()
    page.login()

    login_locators = Login()

    # Test steps
    page.click_burger_menu()
    page.click_logout_link()

    assert page.element_is_present(login_locators.user_name)
    assert page.element_is_present(login_locators.user_password)
    assert page.element_is_present(login_locators.login_button)


def test_about_button(driver):
    """Test of burger menu about button click"""

    # Test Preconditionsf
    page = Inventory(driver, Urls.base)
    page.open()
    page.login()

    # Test steps
    page.click_burger_menu()
    page.click_about_link()

    assert driver.current_url == Urls.about, f"The About button should open {Urls.about} website, \
                                but current webpage is - {driver.current_url}"


def test_reset_button(driver):
    """Test of burger menu reset button click
    Reset App State - clears the Cart from all items"""

    # Test Preconditionsf
    page = Inventory(driver, Urls.base)
    page.open()
    page.login()
    item_name = page.get_item_name()
    page.click_add_to_cart_button(item_name)

    # Test steps
    page.click_burger_menu()
    page.click_reset_app_state_link()

    cart_page = Cart(driver, Urls.cart)
    cart_page.open()
    
    assert cart_page.cart_is_empty(), "The cart is not empty"
