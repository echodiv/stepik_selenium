from selenium import webdriver

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/find_xpath_form")

value = 'input'
elements = browser.find_elements_by_tag_name(value)
for element in elements:
    element.send_keys("Мой ответ")

button = browser.find_element_by_xpath("//button[text()='Отправить']")
button.click()
# не забывайте добавлять пустую строку в конце каждого файла в Python
