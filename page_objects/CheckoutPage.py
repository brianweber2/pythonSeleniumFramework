from selenium.webdriver.common.by import By


class CheckoutPage:
    checkout_button = (By.XPATH, "//button[@class='btn btn-success']")

    def __init__(self, driver):
        self.driver = driver

    def checkout_items(self):
        return self.driver.find_element(*CheckoutPage.checkout_button)