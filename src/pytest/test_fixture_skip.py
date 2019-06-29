import pytest
from selenium import webdriver

link = 'http://forum.igromania.ru/'

@pytest.fixture(scope='function')
def browser():
    print('\nstart Chrome browser for test ...')
    browser = webdriver.Chrome()
    yield browser
    print('\nclose Chrome browser...')
    browser.quit()

class TestMainPage(object):
    '''
    main test class
    '''
    def test_guest_should_see_login_form(self, browser):
        browser.get(link)
        browser.find_element_by_id('navbar_username')
        browser.find_element_by_id('navbar_password')
        browser.find_element_by_css_selector('#igromania_whole_page_div_container > div > div > div > table:nth-child(2) > tbody > tr:nth-child(1) > td:nth-child(2) > table:nth-child(2) > tbody > tr:nth-child(1) > td:nth-child(2) > table > tbody > tr > td > form > table > tbody > tr:nth-child(2) > td:nth-child(3) > input')

    @pytest.mark.skip(reason='one way or enother')
    def test_see_the_forum_title(self, browser):
        browser.get(link)
        browser.find_element_by_css_selector('#igromania_whole_page_div_container > div > div > div > table:nth-child(2) > tbody > tr:nth-child(1) > td:nth-child(1) > a > img')

    @pytest.mark.xfail(reason='fix in anyway')
    def test_cabinet_link(self, browser):
        browser.get(link)
        browser.find_element_by_css_selector('#igromania_whole_page_div_container > div > div > div > table:nth-child(2) > tbody > tr:nth-child(1) > td:nth-child(2) > table:nth-child(3) > tbody > tr > td:nth-child(4) > a:nth-child(1) > img')
