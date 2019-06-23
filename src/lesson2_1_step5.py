import math
from selenium import webdriver
from time import sleep
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

link = 'http://suninjuly.github.io/get_attribute.html'
browser = webdriver.Chrome()
browser.get(link)
x = browser.find_element_by_css_selector("img#treasure")
z = int(x.get_attribute('valuex'))
y = calc(z)
print(type(y))

out = browser.find_element_by_css_selector(".form-group #answer")
out.send_keys(y)

chek_bot = browser.find_element_by_css_selector(".check-input#robotCheckbox")
chek_bot.click()

robo_cool = browser.find_element_by_id("robotsRule")
robo_cool.click()

button = browser.find_element_by_css_selector(".btn.btn-default")
button.click()


#browser.quit()
#fin
