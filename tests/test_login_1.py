
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_valid_login():

    driver = webdriver.Chrome()

    try:
        driver.get("https://katalon-demo-cura.herokuapp.com/")

        # Click Make Appointment
        driver.find_element(By.ID, "btn-make-appointment").click()

        # Enter username
        driver.find_element(By.ID, "txt-username").send_keys("John Doe")

        # Enter password
        driver.find_element(By.ID, "txt-password").send_keys("ThisIsNotAPassword")

        # Click Login
        driver.find_element(By.ID, "btn-login").click()

        # Verify appointment page is displayed
        wait = WebDriverWait(driver, 10)

        appointment_header = wait.until(
            EC.visibility_of_element_located((By.TAG_NAME, "h2"))
        )

        assert appointment_header.text == "Make Appointment"

    finally:
        driver.quit()
