from selenium import webdriver
import time
import unittest

class TestAbs(unittest.TestCase):
    
    def test_abs1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)

        first_name = browser.find_element_by_css_selector('input[placeholder="Input your first name"]')
        first_name.send_keys("Denis")
        time.sleep(5)

        last_name = browser.find_element_by_css_selector('input[placeholder="Input your last name"]')
        last_name.send_keys("Troyan")
        time.sleep(5)
    
        email = browser.find_element_by_css_selector('input[placeholder="Input your email"]')
        email.send_keys("denis.troyan@rambler.ru")
        time.sleep(5)

        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        time.sleep(1)

        welcome_text_elt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text

        assert "Congratulations! You have successfully registered!" == welcome_text

        time.sleep(10)
        browser.quit()

    def test_abs2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        first_name = browser.find_element_by_css_selector('input[placeholder="Input your first name"]')
        first_name.send_keys("Denis")
        time.sleep(5)

        last_name = browser.find_element_by_css_selector('input[placeholder="Input your last name"]')
        last_name.send_keys("Troyan")
        time.sleep(5)
    
        email = browser.find_element_by_css_selector('input[placeholder="Input your email"]')
        email.send_keys("denis.troyan@rambler.ru")
        time.sleep(5)

        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        time.sleep(1)

        welcome_text_elt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text

        assert "Congratulations! You have successfully registered!" == welcome_text
        time.sleep(10)
        browser.quit()

if __name__ == "__main__":
    unittest.main()