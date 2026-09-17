from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage:

    BACKPACK_ITEM = (
        By.CLASS_NAME,
        "inventory_item_name"
    )

    CHECKOUT_BUTTON = (
        By.ID,
        "checkout"
    )

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def get_product_name(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.BACKPACK_ITEM)
        ).text

    def click_checkout(self):
        self.wait.until(
            EC.element_to_be_clickable(self.CHECKOUT_BUTTON)
        ).click()

        # Wait until checkout page loads
        self.wait.until(
            EC.url_contains("checkout-step-one")
        )