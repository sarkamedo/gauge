from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait as WDW
from selenium.webdriver.support import expected_conditions as EC
from browser import Browser
import time


class BasePage(Browser):
    # ============================== Locators ==============================
    _contact_us_header_btn = (By.CSS_SELECTOR, "[title='Contact Us']")
    _sign_in_header_btn = (By.CSS_SELECTOR, "a.login")
    _navigation_tab = (By.CSS_SELECTOR, "#block_top_menu > ul")

# ============================== Elements ==============================
    @property
    def get_contact_us_header_btn(self):
        return WDW(self.driver, 15).until(EC.element_to_be_clickable((self._contact_us_header_btn)))

    @property
    def get_sign_in_header_btn(self):
        return WDW(self.driver, 15).until(EC.element_to_be_clickable((self._sign_in_header_btn)))

    @property
    def get_navigation_tab(self, button=None):
        """This method returns elements of navigation tab by default. If specific button needs to be returned pass the button name as argument in button parameter"""
        if button is not None and type(button) != str:
            raise TypeError("button name must be of string value")

        tab_buttons = WDW(self.driver, 15).until(EC.presence_of_all_elements_located((self._navigation_tab)))
        if button is not None:
            button = button.lower()
            button_dict = {0: "women",
                          1: "dresses",
                          2: "t-shirts"}
            for key in button_dict:
                if button in button_dict[key]:
                    single_btn = tab_buttons[key]
                    return single_btn
            else:
                print("Given button doesn't exist. Please check your value")
        else:
            return tab_buttons

# ============================== Methods ==============================
    def click_on(self, element):
        element.click()
