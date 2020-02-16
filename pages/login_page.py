# if you experience issues with importing local modules try commenting following two lines...
import sys
sys.path.append(".")

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait as WDW
from selenium.webdriver.support import expected_conditions as EC
from browser import Browser
from pages.base_page import BasePage
import time


class LoginPage(BasePage):

    # ============================== Locators ==============================
    _email_field = (By.CSS_SELECTOR, "#email")
    _pwd_field = (By.CSS_SELECTOR, "#passwd")
    _sign_in_btn = (By.CSS_SELECTOR, "#SubmitLogin")

    # ============================== Elements ==============================
    @property
    def get_email_field(self):
        return WDW(self.driver, 15).until(EC.visibility_of_element_located((self._email_field)))
    @property
    def get_pwd_field(self):
        return WDW(self.driver, 15).until(EC.visibility_of_element_located((self._pwd_field)))
    @property
    def get_sign_in_btn(self):
        return WDW(self.driver, 15).until(EC.element_to_be_clickable((self._sign_in_btn)))

    # ============================== Methods ==============================
    def enter_email(self, email):
        self.get_email_field.send_keys(email)

    def enter_password(self, password):
        self.get_pwd_field.send_keys(password)

    def click_sign_in(self):
        self.get_sign_in_btn.click()
