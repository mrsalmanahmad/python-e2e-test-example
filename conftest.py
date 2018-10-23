import pytest
import sys
from selenium import webdriver


# tell python where our modules are...
sys.path.append('pages')

# add cli options...
def pytest_addoption(parser):
    parser.addoption('--url', action='store', default='https://qualityshepherd.com', help='specify the base URL to test against')
    parser.addoption('--browser', action='store', default='chrome', help='chrome or firefox')

# driver fixture passed to all tests
@pytest.fixture(scope='session')
def driver(request):
    browser = request.config.getoption('--browser')
    if browser == 'firefox' or browser == 'ff':
        driver = webdriver.Firefox()
    elif browser == 'chrome':
        driver = webdriver.Chrome()
    else:
        raise ValueError('invalid browser name: ' + browser)
    driver.set_window_size(1200, 800)
    yield driver
    driver.quit()