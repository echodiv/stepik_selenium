import os
from selenium import webdriver

link = 'http://suninjuly.github.io/file_input.html'

browser = webdriver.Chrome()
browser.get(link)

name = browser.find_element_by_name('firstname')
name.send_keys('Oleg')

surname = browser.find_element_by_name('lastname')
surname.send_keys('Tin\'koff')

email = browser.find_element_by_name('email')
email.send_keys('oleg@tin.koff')

current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'file.txt')

sel = browser.find_element_by_name('file')
sel.send_keys(file_path)

browser.execute_script('window.scrollBy(0, 100)')

b = browser.find_element_by_tag_name('button')
b.click()
