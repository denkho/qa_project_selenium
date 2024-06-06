from dotenv import load_dotenv
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    timeout = 10
    load_dotenv()

    def __init__(self, driver:WebDriver, url):
        self.driver = driver
        self.url = url

    
    def open(self):
        self.driver.get(self.url)


    def element_is_present(self, locator_str):
        try:
            self.driver.find_element(By.XPATH, locator_str[1])
            return True
        except NoSuchElementException:
            return False


    def element_is_visible(self, locator, timeout=timeout):
        return wait(self.driver, timeout).until(EC.element_to_be_clickable(locator))
    

    def elements_are_visible(self, locator, timeout=timeout):
        return wait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator))
    

    def click_to_element(self, locator):
        self.element_is_visible(locator).click()


    def get_number_of_elements(self, locator):
        return len(self.elements_are_visible(locator))
    

    def get_text(self, locator):
        return self.element_is_visible(locator).text
    

    def get_list(self, locator):
        lst = [x.text for x in self.elements_are_visible(locator)]
        return lst
    

    def fill_in_input_field(self, locator, data):
        self.element_is_visible(locator).send_keys(data)
        