from selenium import webdriver
from time import sleep

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/cats.html")
browser.implicitly_wait(5)
#sleep(1)

button = browser.find_element_by_id("button")
button.click()


jfjgjsjgps
message = browser.find_element_by_id("check_message")

assert "успешно" in message.text
