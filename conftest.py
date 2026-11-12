import pytest
from selenium import webdriver


@pytest.fixture
def driver():

    # Setup: Launch browser
    driver = webdriver.Chrome()
    driver.maximize_window()

    yield driver

    # Teardown: Close browser
    driver.quit()