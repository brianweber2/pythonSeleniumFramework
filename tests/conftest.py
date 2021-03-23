import pytest
from selenium import webdriver

from config import (
    CHROME_DRIVER_EXECUTABLE_PATH, RAHUL_SHETTY_URL, FIREFOX_DRIVER_EXECUTABLE_PATH
)
from utilities.logger import logger


# https://docs.pytest.org/en/stable/example/simple.html
def pytest_addoption(parser):
    parser.addoption(
        '--browser_name', action='store', default='chrome'
    )


@pytest.fixture(scope='class')
def setup(request):
    browser_name = request.config.getoption('browser_name')
    if browser_name == 'chrome':
        driver = webdriver.Chrome(executable_path=CHROME_DRIVER_EXECUTABLE_PATH)
    elif browser_name == 'firefox':
        # Code for Firefox.
        driver = webdriver.Firefox(executable_path=FIREFOX_DRIVER_EXECUTABLE_PATH)
    elif browser_name == 'ie':
        # Code for Internet Explorer.
        logger.warning('Internet Explorer not implemented. Exiting!')
        exit()
        # driver = webdriver.Ie(executable_path=IE_DRIVER_EXECUTABLE_PATH)
    else:
        logger.error(f'{browser_name} is not a valid browser name. Exiting!')
        exit()
    driver.get(f'{RAHUL_SHETTY_URL}/angularpractice/')
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()
