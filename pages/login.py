import os
from selenium.webdriver.chrome.webdriver import WebDriver
from pages.base import BasePage
from pages import locators



class LoginPage(BasePage):

    def __init__(self, driver: WebDriver, url):
        super().__init__(driver, url)

    def login(self, user=os.getenv("STANDARD_USER"), password=os.getenv("PASSWORD")):
        self.element_is_visible(locators.Login.user_name).send_keys(user)
        self.element_is_visible(locators.Login.user_password).send_keys(password)
        self.click_to_element(locators.Login.login_button)
