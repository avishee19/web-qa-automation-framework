from selenium.webdriver.common.by import By


class ProductsPage:

    ADD_BACKPACK = (
        By.ID,
        "add-to-cart-sauce-labs-backpack"
    )

    CART_BADGE = (
        By.CLASS_NAME,
        "shopping_cart_badge"
    )

    CART_BUTTON = (
        By.CLASS_NAME,
        "shopping_cart_link"
    )

    def __init__(self, driver):
        self.driver = driver

    def add_backpack_to_cart(self):
        self.driver.find_element(*self.ADD_BACKPACK).click()

    def get_cart_count(self):
        return self.driver.find_element(*self.CART_BADGE).text

    def open_cart(self):
        self.driver.find_element(*self.CART_BUTTON).click()