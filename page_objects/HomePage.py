from selenium.webdriver.common.by import By

from page_objects.ShopPage import ShopPage


class HomePage:
    shop_button = (By.CSS_SELECTOR, "a[href*='shop']")
    name = (By.CSS_SELECTOR, "[name='name']")
    email = (By.NAME, 'email')
    check_box = (By.ID, 'exampleCheck1')
    gender_selection = (By.ID, 'exampleFormControlSelect1')
    email_button = (By.XPATH, "//input[@value='Submit']")
    alert_success = (By.CSS_SELECTOR, "[class*='alert-success']")

    def __init__(self, driver):
        self.driver = driver

    def shop_items(self):
        self.driver.find_element(*HomePage.shop_button).click()
        return ShopPage(self.driver)

    def get_name(self):
        return self.driver.find_element(*HomePage.name)

    def get_email(self):
        return self.driver.find_element(*HomePage.email)

    def get_check_box(self):
        return self.driver.find_element(*HomePage.check_box)

    def get_gender(self):
        return self.driver.find_element(*HomePage.gender_selection)

    def get_email_button(self):
        return self.driver.find_element(*HomePage.email_button)

    def get_success_message(self):
        return self.driver.find_element(*HomePage.alert_success)
