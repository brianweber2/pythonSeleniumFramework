import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from utilities.logger import logger


@pytest.mark.usefixtures('setup')
class BaseClass:
    def verify_link_presence(self, link_text, wait=7):
        wait = WebDriverWait(self.driver, wait)
        wait.until(
            expected_conditions.presence_of_element_located((By.LINK_TEXT, link_text))
        )

    def select_option_by_text(self, locator, text):
        sel = Select(locator)
        sel.select_by_visible_text(text)

    def get_logger(self):
        return logger
