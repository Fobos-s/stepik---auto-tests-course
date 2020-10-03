from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math 

def calc():
    return str(math.log(abs(12*math.sin(int(element_text)))))


try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")
    price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), '$100'))
    browser.find_element_by_id('book').click()

    element_1 = browser.find_element_by_id('input_value')
    element_text = element_1.text
    summ = calc()
    element_2 = browser.find_element_by_name('text')
    element_2.send_keys(summ)
    browser.find_element_by_id('solve').click()
finally:
    time.sleep(10)
    browser.quit()