from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get('https://fantlab.ru/')
time.sleep(2)
input_field = driver.find_element_by_name('searchstr')
input_field.send_keys('мастер и маргарита')
time.sleep(2)
submit_button = driver.find_element_by_class_name('input-group-btn')
submit_button.click()


