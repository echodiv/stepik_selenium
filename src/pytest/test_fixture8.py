import pytest
from selenium import webdriver
link = "http://selenium1py.pythonanywhere.com/"
@pytest.fixture(scope='function')
def browser():
    print('\nstart browser for sedt...')
    browser = webdriver.Chrome()
    yield browser
    print('\nquit browser...')
    browser.quit()

class TestMainPage1(object):
    '''
    test for main page
    '''
    @pytest.mark.smoke
    def test_1guest_should_see_login_link(self, browser):
        browser.get(link)
        browser.find_element_by_css_selector('#login_link')

    @pytest.mark.regression
    @pytset.mark.win10
    def test_2guest_should_see_basket_link_on_main_page(self, browser):
        browser.get(link)
        browser.find_element_by_css_selector('.basket-mini .btn-group > a')


