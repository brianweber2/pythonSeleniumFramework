import pytest

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from page_objects.HomePage import HomePage
from page_objects.ShopPage import ShopPage
from page_objects.CheckoutPage import CheckoutPage
from page_objects.PurchasePage import PurchasePage
from utilities.BaseClass import BaseClass


# @pytest.mark.usefixtures('setup')
class TestOne(BaseClass):

    def test_e2e(self):
        home_page = HomePage(self.driver)

        shop_page = home_page.shop_items()

        products = shop_page.get_products()
        for product in products:
            product_name = shop_page.get_product_name(product)
            if product_name == 'Blackberry':
                shop_page.get_product_button(product).click()

        checkout_page = shop_page.get_checkout_button()
        purchase_page = checkout_page.checkout_items()
        purchase_page.get_country_input().send_keys('ind')
        wait = WebDriverWait(self.driver, 7)
        wait.until(
            purchase_page.is_country_present('India')
        )
        purchase_page.get_country('India').click()
        purchase_page.get_terms_checkbox().click()

        # Purchase button
        purchase_page.get_purchase_button().click()

        alert = purchase_page.get_alert()

        assert 'Success! Thank you!' in alert.text

        self.driver.get_screenshot_as_file('screen.png')
