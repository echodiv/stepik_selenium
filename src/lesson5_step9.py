from selenium import webdriver
from time import sleep

link = "http://suninjuly.github.io/registration2.html"
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
# Проверяем, что смогли зарегистрироваться
# ждем загрузки страницы
sleep(1)
# находим элемент, содержащий текст
welcome_text_elt = browser.find_element_by_tag_name("h1")
# записываем в переменную welcome_text текст из элемента welcome_text_elt
welcome_text = welcome_text_elt.text
# с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
assert "Поздравляем! Вы успешно зарегистировались!" == welcome_text     
#fin
