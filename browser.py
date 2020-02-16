from selenium import webdriver
import datetime
import time

_chromedriver_path = "/home/sakhmedo/miniconda3/bin/chromedriver.exe"


class Browser():
        
    driver = webdriver.Chrome("/home/sakhmedo/miniconda3/bin/chromedriver.exe")

    def close_current_tab_or_window(self):
        self.driver.close()

    def quit_browser(self):
        self.driver.quit()

    def go_to(self, link):
        self.driver.get(link)

    @property
    def get_window_handles(self):
        return self.driver.window_handles

    def get_current_window_handle(self):
        return self.driver.current_window_handle

    def switch_to_window(self, window_index):
        self.driver.switch_to.window(
            self.driver.window_handles[window_index])

    def js_scroll_into_view(self, target):
        self.driver.execute_script(
            'arguments[0].scrollIntoView(true);', target)

    def take_screenshot(self, filename):
        time_stamp = datetime.datetime\
            .fromtimestamp(time.time()).strftime('%Y%m%d_%H%M%S')
        file_path = f"features/screenshots/{filename}-{time_stamp}.png"
        self.driver.save_screenshot(file_path)
        return print(f"Screenshot was saved as {file_path}")

    def close_pop_up_ad_window(self):
        """changes focus to newly opened tab then closes it and switches focus back to main window"""
        if len(self.get_window_handles) > 1:
            self.switch_to_window(1)
            time.sleep(1)
            self.close_current_tab_or_window()
            self.switch_to_window(0)
            time.sleep(4)
        else:
            pass
