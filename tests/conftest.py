import pytest
from selenium import webdriver


@pytest.fixture
def driver():
    browser = webdriver.Chrome()
    browser.get("https://www.saucedemo.com/")

    yield browser

    browser.quit()