from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


def test_add_product_to_cart(driver):

    # Login
    login_page = LoginPage(driver)

    login_page.enter_username("standard_user")
    login_page.enter_password("secret_sauce")
    login_page.click_login()

    # Products page
    products_page = ProductsPage(driver)

    products_page.add_backpack_to_cart()

    assert products_page.get_cart_count() == "1"

    # Cart
    products_page.open_cart()

    cart_page = CartPage(driver)

    assert cart_page.get_product_name() == "Sauce Labs Backpack"

    # Checkout
    cart_page.click_checkout()

    checkout_page = CheckoutPage(driver)

    checkout_page.enter_customer_details(
        "Avishee",
        "A",
        "751001"
    )

    checkout_page.click_continue()

    # Verify checkout overview
    assert checkout_page.verify_checkout_overview()

    # Finish order
    checkout_page.click_finish()

    # Verify successful order
    assert "Thank you for your order" in checkout_page.get_success_message()


def test_checkout_missing_postal_code(driver):

    # Login
    login_page = LoginPage(driver)

    login_page.enter_username("standard_user")
    login_page.enter_password("secret_sauce")
    login_page.click_login()

    # Add product
    products_page = ProductsPage(driver)

    products_page.add_backpack_to_cart()

    # Open cart
    products_page.open_cart()

    # Go to checkout
    cart_page = CartPage(driver)

    cart_page.click_checkout()

    # Enter incomplete customer details
    checkout_page = CheckoutPage(driver)

    checkout_page.enter_customer_details(
        "Avishee",
        "A",
        ""
    )

    # Try to continue
    checkout_page.click_continue()

    # Verify validation error
    error_message = checkout_page.get_error_message()

    assert "postal code" in error_message.lower()