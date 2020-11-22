from selenium import webdriver
import time 

link = "http://selenium1py.pythonanywhere.com/ru/"

try:
    # Arrange
    browser = webdriver.Chrome()
    browser.get(link)

    step1 = browser.find_element_by_id('login_link')
    step1.click()
    time.sleep(5)

    # Act
    step2 = browser.find_element_by_id('id_login-username')
    step2.send_keys('denis.troyan92@gmail.com')

    step3 = browser.find_element_by_id('id_login-password')
    step3.send_keys('uVw6R2uqCyjQYeq')

    # Assert
    step4 = browser.find_element_by_name('login_submit')
    step4.click()



finally:
    
    time.sleep(10)
    
    browser.quit()

