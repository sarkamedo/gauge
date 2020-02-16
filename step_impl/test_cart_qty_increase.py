import sys
sys.path.insert(0, "/mnt/c/projects/gauge_framework")
from getgauge.python import step, continue_on_failure
from pages.login_page import LoginPage
from browser import Browser
import strings
import time

browser = Browser()
login_page = LoginPage()


@continue_on_failure
@step("Login as a user")
def login_as_a_user():
    browser.go_to("http://automationpractice.com/index.php")
    time.sleep(2)
    #assert login_page.get_contact_us_header_btn(
    #).text == strings.contact_us_text, f"Exepected: {strings.contact_us_text}\n Actual: {login_page.get_contact_us_header_btn().text}"
    login_page.click_on(login_page.get_sign_in_header_btn)
    login_page.enter_email(strings.username)
    login_page.enter_password(strings.password)
    login_page.click_on(login_page.get_sign_in_btn)


@continue_on_failure
@step("Add 1 item to cart with quantity of 1")
def add_1_item_to_cart_with_quantity_of_1():
    login_page.click_on(login_page.get_navigation_tab("dress"))


@continue_on_failure
@step("Verify quantity is 1")
def verify_quantity_is_1():
    pass


@continue_on_failure
@step("Increase quantity to 5")
def increase_quantity_to_5():
    pass


@continue_on_failure
@step("Verify that quantity is updated to 5")
def verify_that_quantity_is_updated_to_5():
    pass


@continue_on_failure
@step("And total price is updated accordingly")
def and_total_price_is_updated_accordingly():
    pass
