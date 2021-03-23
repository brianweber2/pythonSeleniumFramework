from selenium.webdriver.common.by import By


class HomePage:
    shop = (By.CSS_SELECTOR, "a[href*='shop']")

    def __init__(self, driver):
        self.driver = driver

    def shop_items(self):
        return self.driver.find_element(*HomePage.shop)
