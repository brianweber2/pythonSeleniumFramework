from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions


class PurchasePage:
    country_input = (By.ID, 'country')
    terms_checkbox = (By.XPATH, "//div[@class='checkbox checkbox-primary']")
    purchase_button = (By.CSS_SELECTOR, "[type='submit']")
    alert = (By.CLASS_NAME, 'alert-success')

    def __init__(self, driver):
        self.driver = driver

    def get_country_input(self):
        return self.driver.find_element(*PurchasePage.country_input)

    def get_country(self, country):
        return self.driver.find_element(By.LINK_TEXT, country)

    def get_terms_checkbox(self):
        return self.driver.find_element(*PurchasePage.terms_checkbox)

    def get_purchase_button(self):
        return self.driver.find_element(*PurchasePage.purchase_button)

    def get_alert(self):
        return self.driver.find_element(*PurchasePage.alert)

    @staticmethod
    def is_country_present(country):
        return expected_conditions.presence_of_element_located((By.LINK_TEXT, country))
