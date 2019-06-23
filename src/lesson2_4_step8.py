from math import log, sin
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver


def foo(x):
    return log(abs(12*sin(x)))


link = 'http://suninjuly.github.io/explicit_wait2.html'
browser = webdriver.Chrome()
browser.get(link)

text = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, 'h5#price'), '10000 RUR'))

button = browser.find_element_by_css_selector('button#book')
button.click()

x = browser.find_element_by_id('input_value')
y = str(foo(int(x.text)))

answer = browser.find_element_by_id('answer')
answer.send_keys(y)

out = browser.find_element_by_id('solve')
out.click()
