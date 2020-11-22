from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/explicit_wait2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    wait = WebDriverWait(browser, 20)
    element = wait.until(EC.text_to_be_present_in_element((By.ID,'price'), '$100'))
    input0 = browser.find_element_by_xpath('//button[@class="btn btn-primary"]')
    input0.click()

    x_element = browser.find_element_by_id('input_value')
    x = x_element.text
    y = calc(x)

    input1 = browser.find_element_by_id('answer')
    input1.send_keys(f"{y}")

    button = browser.find_element_by_id('solve')
    button.click() 

   
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()