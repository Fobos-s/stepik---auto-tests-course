from selenium import webdriver
import time
import math 

def calc():
    return str(math.log(abs(12*math.sin(int(element_text)))))

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/redirect_accept.html")
    browser.find_element_by_class_name('trollface').click()
    window_second = browser.window_handles[1]
    browser.switch_to.window(window_second)
    element_1 = browser.find_element_by_id('input_value')
    element_text = element_1.text
    summ = calc()
    element_2 = browser.find_element_by_name('text')
    element_2.send_keys(summ)
    browser.find_element_by_class_name('btn.btn-primary').click()

finally:
    time.sleep(10)
    browser.quit()