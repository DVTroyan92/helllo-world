from selenium.webdriver.support.ui import Select
from selenium import webdriver
import time
import math

def add(x, y):
    return x + y

link = "http://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_id('num1')
    y_element = browser.find_element_by_id('num2')
    x = int(x_element.text)
    y = int(y_element.text)
    z = add(x, y)
    
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(f'{z}') # ищем элемент с текстом "Python"

    option = browser.find_element_by_xpath('//button[@type="submit"]')
    option.click()


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла