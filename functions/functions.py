def create_add_to_cart_button_locator(item_name):
    locator = "-".join(item_name.lower().split())
    return ('xpath', f'//button[@data-test="add-to-cart-{locator}"]')


def create_remove_from_cart_button_locator(item_name):
    locator = "-".join(item_name.lower().split())
    return ('xpath', f'//button[@data-test="remove-{locator}"]')


def create_image_locator(item_name):
    locator = "-".join(item_name.lower().split())
    return ('xpath', f'//img[@data-test="inventory-item-{locator}-img"]')
