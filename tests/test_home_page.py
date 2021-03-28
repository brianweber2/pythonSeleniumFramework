import pytest

from page_objects.HomePage import HomePage
from test_data.home_page_data import HomePageData
from utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):

    def test_form_submission(self, get_data):
        logger = self.get_logger()
        home_page = HomePage(self.driver)
        logger.info(f"First name is {get_data['first_name']}")
        home_page.get_name().send_keys(get_data['first_name'])
        home_page.get_email().send_keys(get_data['email'])
        home_page.get_check_box().click()
        self.select_option_by_text(home_page.get_gender(), get_data['gender'])
        home_page.get_email_button().click()
        alert_text = home_page.get_success_message().text

        assert 'Success' in alert_text
        self.driver.refresh()  # needed to clean the form.

    @pytest.fixture(params=HomePageData.test_home_page_data)
    def get_data(self, request):
        return request.param
