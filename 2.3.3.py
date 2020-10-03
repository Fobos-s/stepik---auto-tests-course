from selenium import webdriver
import time
import math

def calc():
    return str(math.log(abs(12*math.sin(int(element_text)))))

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/alert_accept.html")
    browser.find_element_by_class_name('btn.btn-primary').click()
    blabla = browser.switch_to.alert
    blabla.accept()
    element = browser.find_element_by_id('input_value')
    element_text = element.text
    inp = calc()
    str_inp = browser.find_element_by_id('answer')
    str_inp.send_keys(inp)
    browser.find_element_by_class_name('btn.btn-primary').click()
    
finally:
    time.sleep(10)
    browser.quit()

