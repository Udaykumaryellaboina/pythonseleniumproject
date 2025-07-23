from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, by, value):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((by, value)))

    def click(self, by, value):
        element = self.find_element(by, value)
        element.click()

    def enter_text(self, by, value, text):
        element = self.find_element(by, value)
        element.clear()
        element.send_keys(text)

    def get_title(self):
        return self.driver.title

    def close(self):
        self.driver.quit()