from pages.login_page import LoginPage
from pages.appointment_page import AppointmentPage
from config import BASE_URL, USERNAME, PASSWORD

def test_valid_login(driver):

    driver.get(BASE_URL)

    login_page = LoginPage(driver)
    appointment_page = AppointmentPage(driver)

    login_page.click_make_appointment()
    login_page.enter_username(USERNAME)
    login_page.enter_password(PASSWORD)
    login_page.click_login()

    assert appointment_page.get_header_text() == "Make Appointment"

    # TEST_ENV=dev pytest tests/test_login.py -v - to specify the env during runtime