# https://stepik.org/lesson/184253/step/4?unit=158843

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import math

try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element(By.TAG_NAME, "button").click()
    time.sleep(3)
    browser.switch_to.alert.accept()

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    x = browser.find_element(By.ID, "input_value").text
    browser.find_element(By.ID, "answer").send_keys(calc(x))
    # time.sleep(1)
    browser.find_element(By.CSS_SELECTOR, ".btn").click()
    time.sleep(3)

finally:
    time.sleep(15)
    browser.quit()
