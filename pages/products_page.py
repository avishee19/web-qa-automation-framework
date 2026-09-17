from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ProductsPage:

    ADD_BACKPACK = (By.ID, "add-to-cart-sauce-labs-backpack")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    CART_BUTTON = (By.CLASS_NAME, "shopping_cart_link")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def add_backpack_to_cart(self):

        button = self.wait.until(
            EC.element_to_be_clickable(self.ADD_BACKPACK)
        )

        button.click()

    def get_cart_count(self):

        badge = self.wait.until(
            EC.visibility_of_element_located(self.CART_BADGE)
        )

        return badge.text

    def open_cart(self):

        button = self.wait.until(
            EC.element_to_be_clickable(self.CART_BUTTON)
        )

        button.click()