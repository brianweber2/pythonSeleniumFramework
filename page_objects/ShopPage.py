from selenium.webdriver.common.by import By

from page_objects.CheckoutPage import CheckoutPage


class ShopPage:
    products = (By.XPATH, "//div[@class='card h-100']")
    product = (By.XPATH, "div/h4/a")
    product_button = (By.XPATH, 'div/button')
    checkout_button = (By.CSS_SELECTOR, "a[class*='btn-primary']")

    def __init__(self, driver):
        self.driver = driver

    def get_products(self):
        return self.driver.find_elements(*ShopPage.products)

    @staticmethod
    def get_product_name(product):
        return product.find_element(*ShopPage.product).text

    @staticmethod
    def get_product_button(product):
        return product.find_element(*ShopPage.product_button)

    def get_checkout_button(self):
        self.driver.find_element(*ShopPage.checkout_button).click()
        return CheckoutPage(self.driver)
