from pages.login_page import LoginPage


def test_valid_login(driver):

    login_page = LoginPage(driver)

    login_page.enter_username("standard_user")
    login_page.enter_password("secret_sauce")
    login_page.click_login()

    assert "inventory" in driver.current_url


def test_locked_out_user(driver):

    login_page = LoginPage(driver)

    login_page.enter_username("locked_out_user")
    login_page.enter_password("secret_sauce")
    login_page.click_login()

    error_message = login_page.get_error_message()

    assert "locked out" in error_message.lower()