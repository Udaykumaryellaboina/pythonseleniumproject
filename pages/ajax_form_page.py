from selenium.webdriver.common.by import By

class AjaxFormPage:
    NAME_INPUT = (By.ID, "name")
    COMMENT_INPUT = (By.ID, "comment")
    SUBMIT_BUTTON = (By.ID, "submitBtn")
    SUCCESS_MESSAGE = (By.ID, "successMsg")

    def __init__(self, driver):
        self.driver = driver

    def enter_name(self, name):
        self.driver.find_element(*self.NAME_INPUT).send_keys(name)

    def enter_comment(self, comment):
        self.driver.find_element(*self.COMMENT_INPUT).send_keys(comment)

    def click_submit(self):
        self.driver.find_element(*self.SUBMIT_BUTTON).click()

    def get_success_message(self):
        return self.driver.find_element(*self.SUCCESS_MESSAGE).text
