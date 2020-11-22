from selenium import webdriver
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/get_attribute.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_xpath('//img[@src="images/chest.png"]')
    x = x_element.get_attribute('valuex')
    y = calc(x)
    
    input1 = browser.find_element_by_id('answer')
    input1.send_keys(f"{y}")

    option1 = browser.find_element_by_id('robotCheckbox')
    option1.click()

    option2 = browser.find_element_by_id('robotsRule')
    option2.click()

    option3 = browser.find_element_by_xpath('//button[@type="submit"]')
    option3.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла