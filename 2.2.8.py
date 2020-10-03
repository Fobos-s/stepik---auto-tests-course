from selenium import webdriver
import time
import os

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/file_input.html")
    first = browser.find_element_by_name('firstname')
    first.send_keys('Name')
    second = browser.find_element_by_name('lastname')
    second.send_keys('Surename')
    mail = browser.find_element_by_name('email')
    mail.send_keys('fuck@mail.com')
    element = browser.find_element_by_id('file')
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')
    element.send_keys(file_path)
    browser.find_element_by_class_name('btn').click()



finally:
    time.sleep(30)
    browser.quit()

