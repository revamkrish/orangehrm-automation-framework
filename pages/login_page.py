from selenium.webdriver.common.by import By


class LoginPage:

    # Locators
    USERNAME = (By.ID, "txt-username")
    PASSWORD = (By.ID, "txt-password")
    LOGIN_BUTTON = (By.ID, "btn-login")

    def __init__(self, driver):
        self.driver = driver

    def click_make_appointment(self):
        self.driver.find_element(By.ID, "btn-make-appointment").click()

    def enter_username(self, username):
        self.driver.find_element(*self.USERNAME).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*self.PASSWORD).send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.LOGIN_BUTTON).click()
