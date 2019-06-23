from selenium import webdriver
from selenium.webdriver.support.ui import Select
link = 'http://suninjuly.github.io/selects1.html'
browser = webdriver.Chrome()
browser.get(link)

input_one = int(browser.find_element_by_id('num1').text)
input_two = int(browser.find_element_by_id('num2').text)

output = str(input_one + input_two)

select = Select(browser.find_element_by_tag_name('select'))
select.select_by_visible_text(output)

button = browser.find_element_by_css_selector('.btn-default')
button.click()
