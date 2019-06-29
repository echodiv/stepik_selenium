#python

from selenium import webdriver
import unittest

class testCase(unittest.TestCase):
    def test_page_one(self):
        link = 'http://suninjuly.github.io/registration1.html'
        browser = webdriver.Chrome()
        #get page
        browser.get(link)
        elements = {
                '.first_block .form-control.first': 'Name',
                '.first_block .form-control.second': 'Surname',
                '.first_block .form-control.third': 'email@test.stepik'
                }
        for selector, value in elements.items():
            inp=browser.find_element_by_css_selector(selector)
            inp.send_keys(value)
        button = browser.find_element_by_css_selector("button.btn")
        button.click()
        
    def test_page_two(self):
        link = 'http://suninjuly.github.io/registration2.html'
        browser = webdriver.Chrome()
        #get page
        browser.get(link)
        elements = {
                '.first_block .form-control.first': 'Name',
                '.first_block .form-control.second': 'Surname',
                '.first_block .form-control.third': 'email@test.stepik'
                }
        for selector, value in elements.items():
            inp=browser.find_element_by_css_selector(selector)
            inp.send_keys(value)
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        
if __name__ == "__main__":
    unittest.main()


#
