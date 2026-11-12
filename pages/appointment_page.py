from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AppointmentPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

        self.appointment_header = (By.TAG_NAME, "h2")

    def get_header_text(self):
        header = self.wait.until(
            EC.visibility_of_element_located(self.appointment_header)
        )
        return header.text