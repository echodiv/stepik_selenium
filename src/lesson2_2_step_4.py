from math import log, sin
from selenium import webdriver

browser = webdriver.Chrome()
browser.get('http://suninjuly.github.io/redirect_accept.html')

def foo(x):
    return str(log(abs(12*sin(x))))

b1 = browser.find_element_by_tag_name('button')
b1.click()

#confirm = browser.switch_to.alert
#confirm.accept()

window_name = browser.window_handles[1]
browser.switch_to.window(window_name)

x = int(browser.find_element_by_id('input_value').text)

answer = browser.find_element_by_id('answer')
answer.send_keys(foo(x))
'''
script = """
        button = document.getElementsByTagName("button")[0];
        return button.scrollIntoView();
        """

sc = "window.scrollBy(0, 100);"
browser.execute_script(sc)

imrobo = browser.find_element_by_css_selector('.form-check-custom .form-check-label')
imrobo.click()

robo_cool = browser.find_element_by_css_selector('.form-radio-custom .form-check-label')
robo_cool.click()
'''
b = browser.find_element_by_tag_name('button')
b.click()
