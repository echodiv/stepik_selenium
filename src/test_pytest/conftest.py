import pytest
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome', help='Chose browser: chrome or firefox')

@pytest.fixture(scope='function')
def browser(request):
    browser_name = request.config.getoption('browser_name')
    if browser_name == 'chrome':
        print('\nstart chrome browser...')
        browser = webdriver.Chrome()
    elif browser_name == 'firefox':
        cap = DesiredCapabilities().FIREFOX
        cap['marionette'] = False
        print('\nstart firefox browser...')
        browser = webdriver.Firefox(capabilities=cap)
    else:
        print(f'\nuncown "{browser_name}" browser')
    yield browser
    print('\nquit browser...')
    browser.quit()
