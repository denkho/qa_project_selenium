import os

from dotenv import load_dotenv
from pages.login import LoginPage
from pages import locators
from src.responces_data import LoginTexts
from src.urls import Urls


def test_authorization_with_valid_credentials(driver):
    """Tests the authorization with valid credentials
    """
    # Test data - Expected results

    page_title = 'Products'
    number_of_items_on_page = 6
    load_dotenv()
    user = os.getenv("STANDARD_USER")
    password = os.getenv("PASSWORD")
    

    # Test steps

    page = LoginPage(driver, Urls.base)
    page.open()
    page.login(user, password)
    assert page.get_text(locators.InventoryPage.title) == page_title, f"Page title is {page.get_text(locators.InventoryPage.title)}, \
                                                                        but had to be {page_title}"
    assert page.element_is_visible(locators.InventoryPage.items_list), "There are not items in the Inventory"
    assert page.get_number_of_elements(locators.InventoryPage.item) == number_of_items_on_page, \
                                                        f"There should be {number_of_items_on_page} of items, \
                                                            but there are {page.get_number_of_elements(locators.InventoryPage.item)}"


def test_authorization_with_incorrect_credentials(driver):
    """Tests the authorization with incorrect credentials
    """

    #Test data
    user = 'user'
    password = 'user'

    # Test steps
    page = LoginPage(driver, Urls.base)
    page.open()
    page.login(user, password)
    assert page.get_text(locators.Login.login_error) == LoginTexts.login_error, f"There is no login error text or it differs \
                                                                                from '{LoginTexts.login_error}'"
    