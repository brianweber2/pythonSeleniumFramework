from page_objects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestOne(BaseClass):

    def test_e2e(self):
        logger = self.get_logger()
        home_page = HomePage(self.driver)
        shop_page = home_page.shop_items()
        logger.info('Going shopping!')

        products = shop_page.get_products()
        for product in products:
            product_name = shop_page.get_product_name(product).text
            logger.info(f'Product name: {product_name}')
            if product_name == 'Blackberry':
                shop_page.get_product_button(product).click()

        checkout_page = shop_page.get_checkout_button()
        purchase_page = checkout_page.checkout_items()
        logger.info('Entering country name.')
        purchase_page.get_country_input().send_keys('ind')
        self.verify_link_presence('India')
        purchase_page.get_country('India').click()
        purchase_page.get_terms_checkbox().click()

        # Purchase button
        purchase_page.get_purchase_button().click()

        alert = purchase_page.get_alert()
        logger.info(f'Alert text received is {alert.text}')

        assert 'Success! Thank you!' in alert.text

        self.driver.get_screenshot_as_file('screen.png')
