from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage:

    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    POSTAL_CODE = (By.ID, "postal-code")

    CONTINUE_BUTTON = (By.ID, "continue")
    FINISH_BUTTON = (By.ID, "finish")

    OVERVIEW_TITLE = (By.CLASS_NAME, "title")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "[data-test='error']")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "[data-test='complete-header']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def enter_customer_details(self, first_name, last_name, postal_code):

        first_name_field = self.wait.until(
            EC.visibility_of_element_located(self.FIRST_NAME)
        )

        last_name_field = self.wait.until(
            EC.visibility_of_element_located(self.LAST_NAME)
        )

        postal_code_field = self.wait.until(
            EC.visibility_of_element_located(self.POSTAL_CODE)
        )

        first_name_field.clear()
        first_name_field.send_keys(first_name)

        last_name_field.clear()
        last_name_field.send_keys(last_name)

        postal_code_field.clear()
        postal_code_field.send_keys(postal_code)

    def click_continue(self):

        button = self.wait.until(
            EC.element_to_be_clickable(self.CONTINUE_BUTTON)
        )

        button.click()

    def verify_checkout_overview(self):

        overview = self.wait.until(
            EC.visibility_of_element_located(self.OVERVIEW_TITLE)
        )

        return overview.text == "Checkout: Overview"

    def get_error_message(self):

        return self.wait.until(
            EC.visibility_of_element_located(self.ERROR_MESSAGE)
        ).text

    def click_finish(self):

        button = self.wait.until(
            EC.element_to_be_clickable(self.FINISH_BUTTON)
        )

        button.click()

    def get_success_message(self):

        return self.wait.until(
            EC.visibility_of_element_located(self.SUCCESS_MESSAGE)
        ).text