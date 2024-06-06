class Login:
    user_name = ('xpath', '//input[@data-test="username"]')
    user_password = ('xpath', '//input[@data-test="password"]')
    login_button = ('xpath', '//input[@data-test="login-button"]')
    login_error = ('xpath', '//h3[@data-test="error"]')


class InventoryPage:
    title = ('xpath', '//span[@data-test="title"]')
    inventory = ('xpath', '//div[@data-test="inventory-container"]')

    items_list = ('xpath', '//div[@data-test="inventory-list"]')

    item = ('xpath', '//div[@data-test="inventory-item"]')
    item_name = ('xpath', '//div[@data-test="inventory-item-name"]')
    item_price = ('xpath', '//div[@data-test="inventory-item-price"]')
    
    cart_icon = ('xpath', '//a[@data-test="shopping-cart-link"]')

    # Filter
    filter_az = ('xpath', '//select[@data-test="product-sort-container"]/option[@value="az"]')
    filter_za = ('xpath', '//select[@data-test="product-sort-container"]/option[@value="za"]')
    filter_lohi = ('xpath', '//select[@data-test="product-sort-container"]/option[@value="lohi"]')
    filter_hilo = ('xpath', '//select[@data-test="product-sort-container"]/option[@value="hilo"]')

    # Burger menu
    burger_menu_icon = ('xpath', '//button[@id="react-burger-menu-btn"]')
    logout_menu_item = ('xpath', '//a[@data-test="logout-sidebar-link"]')
    about_menu_item = ('xpath', '//a[@data-test="about-sidebar-link"]')
    reset_app_menu_item = ('xpath', '//a[@data-test="reset-sidebar-link"]')
    

class CartPage:
    cart_item = ('xpath', '//div[@class="cart_item"]')
    item_name = ('xpath', '//div[@data-test="inventory-item-name"]')
    checkout_button = ('xpath', '//button[@data-test="checkout"]')


class ItemCard:
    button_add_to_cart = ('xpath', '//button[@data-test="add-to-cart"]')
    button_remove_from_cart = ('xpath', '//button[@data-test="remove"]')   
    item_description = ('xpath', '//div[@data-test="inventory-item-desc"]')
    item_price = ('xpath', '//div[@data-test="inventory-item-price"]')
    item_img = ('xpath', '//div[@class="inventory_details_img_container"]')


class Checkout:
    first_name = ('xpath', '//input[@data-test="firstName"]')
    last_name = ('xpath', '//input[@data-test="lastName"]')
    zip = ('xpath', '//input[@data-test="postalCode"]')

    continue_button = ('xpath', '//input[@data-test="continue"]')
    finish_button = ('xpath', '//button[@data-test="finish"]')

    complete_order = ('xpath', '//h2[@data-test="complete-header"]')
    title = ('xpath', '//span[@data-test="title"]')
