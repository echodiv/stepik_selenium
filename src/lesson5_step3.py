import math
from selenium import webdriver
from time import sleep
main_link = "http://suninjuly.github.io/find_link_text"
browser = webdriver.Chrome()
browser.get(main_link)
text = str(math.ceil(math.pow(math.pi, math.e)*10000))
link = browser.find_element_by_link_text(text)
link.click()

values = ['first_name', 'last_name', 'firstname']
ids = ['country']
input1 = browser.find_element_by_name(values[0])
input1.send_keys("Sergey")
input2 = browser.find_element_by_name(values[1])
input2.send_keys("Batalov")
input3 = browser.find_element_by_name(values[2])
input3.send_keys("Saint-Petersburg")
input4 = browser.find_element_by_id(ids[0])
input4.send_keys("Russia")
button = browser.find_element_by_css_selector("button.btn")
button.click()
