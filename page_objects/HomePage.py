from selenium.webdriver.common.by import By

from page_objects.ShopPage import ShopPage


class HomePage:
    shop = (By.CSS_SELECTOR, "a[href*='shop']")

    def __init__(self, driver):
        self.driver = driver

    def shop_items(self):
        self.driver.find_element(*HomePage.shop).click()
        return ShopPage(self.driver)
