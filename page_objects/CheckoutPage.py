from selenium.webdriver.common.by import By

from page_objects.PurchasePage import PurchasePage


class CheckoutPage:
    checkout_button = (By.XPATH, "//button[@class='btn btn-success']")

    def __init__(self, driver):
        self.driver = driver

    def checkout_items(self):
        self.driver.find_element(*CheckoutPage.checkout_button).click()
        return PurchasePage(self.driver)
