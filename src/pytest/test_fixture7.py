from math import log
import pytest
from selenium import webdriver
from time import time, sleep

@pytest.fixture(scope='function')
def browser():
    print('\nstart browser...')
    browser = webdriver.Chrome()
    yield browser
    print('\nquit browser...')
    browser.quit()

@pytest.mark.parametrize('link', 
['https://stepik.org/lesson/236895/step/1',
'https://stepik.org/lesson/236896/step/1',
'https://stepik.org/lesson/236897/step/1',
'https://stepik.org/lesson/236898/step/1',
'https://stepik.org/lesson/236899/step/1',
'https://stepik.org/lesson/236903/step/1',
'https://stepik.org/lesson/236904/step/1',
'https://stepik.org/lesson/236905/step/1']
)
def test_guest_should_see_login_link(browser, link):
    browser.get(link)
    answer = str(log(int(time())))
    sleep(2)
    out = browser.find_element_by_css_selector('.ember-auto-resize.ember-view')
    out.click()
    out.send_keys(answer)
    b = browser.find_element_by_css_selector('.submit-submission ')
    b.click()
    sleep(1)
    i = browser.find_element_by_css_selector('.smart-hints__hint')
    assert i.text == 'Correct!', i.text
#
