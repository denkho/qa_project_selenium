from pages.inventory import Inventory
from src.urls import Urls


def test_filter_AZ(driver):
    """Test of filter in inventory which sorts items alphabetically"""

    # Test Preconditions
    page = Inventory(driver, Urls.base)
    page.open()
    page.login()
    page.inventory_filter('za')

    # Test steps
    
    page.inventory_filter('az')
    list_of_items = page.get_list_of_items()
    assert list_of_items == sorted(list_of_items), "The items are not sorted alphabetically (from A to Z)"


def test_filter_ZA(driver):
    """Test of filter in inventory which sorts items reversed alphabetically"""

    # Test Preconditions
    page = Inventory(driver, Urls.base)
    page.open()
    page.login()
    page.inventory_filter('az')

    # Test steps
    
    page.inventory_filter('za')
    list_of_items = page.get_list_of_items()
    assert list_of_items == sorted(list_of_items, reverse=True), "The items are not sorted reversed alphabetically (from Z to A)"


def test_filter_LowHi(driver):
    """Test of filter in inventory which sorts items by their prices from low to high"""

    # Test Preconditions
    page = Inventory(driver, Urls.base)
    page.open()
    page.login()
    page.inventory_filter('hilo')

    # Test steps
    
    page.inventory_filter('lohi')
    list_of_items = page.get_list_of_prices_of_items()
    assert list_of_items == sorted(list_of_items), "The items are not sorted by price from Low to High)"



def test_filter_HiLow(driver):
    """Test of filter in inventory which sorts items by their prices from high to low"""

    # Test Preconditions
    page = Inventory(driver, Urls.base)
    page.open()
    page.login()
    page.inventory_filter('lohi')

    # Test steps
    
    page.inventory_filter('hilo')
    list_of_items = page.get_list_of_prices_of_items()
    assert list_of_items == sorted(list_of_items, reverse=True), "The items are not sorted by price from High to Low)"
