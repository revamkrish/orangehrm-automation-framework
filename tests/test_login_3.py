from pages.login_page import LoginPage
from pages.appointment_page import AppointmentPage


def test_valid_login(driver):

    driver.get("https://katalon-demo-cura.herokuapp.com/")

    login_page = LoginPage(driver)
    appointment_page = AppointmentPage(driver)

    login_page.click_make_appointment()
    login_page.enter_username("John Doe")
    login_page.enter_password("ThisIsNotAPassword")
    login_page.click_login()

    assert appointment_page.get_header_text() == "Make Appointment"