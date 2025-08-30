import logging
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By

logger = logging.getLogger(__name__)

class HomePage:
    SEARCH_BOX = (By.ID, "search")
    SEARCH_BUTTON = (By.ID, "searchBtn")
    LOGIN_LINK = (By.LINK_TEXT, "Login")

    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver

    def enter_search(self, text: str) -> None:
        logger.info(f"Entering search text: {text}")
        self.driver.find_element(*self.SEARCH_BOX).send_keys(text)

    def click_search(self) -> None:
        logger.info("Clicking search button")
        self.driver.find_element(*self.SEARCH_BUTTON).click()

    def click_login(self) -> None:
        logger.info("Clicking login link")
        self.driver.find_element(*self.LOGIN_LINK).click()
