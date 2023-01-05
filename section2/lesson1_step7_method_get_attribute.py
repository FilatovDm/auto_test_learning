# https://stepik.org/lesson/165493/step/7?unit=140087

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.CSS_SELECTOR, "img")
    x = x_element.get_attribute("valuex")

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    input_field = browser.find_element(By.CSS_SELECTOR, "input[type='text']:required")
    input_field.send_keys(calc(x))
    time.sleep(2)

    check_box_robo = browser.find_element(By.ID, "robotCheckbox")
    check_box_robo.click()

    radio_robo_rule = browser.find_element(By.ID, "robotsRule")
    radio_robo_rule.click()
    time.sleep(2)

    submit_btn = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    submit_btn.click()
    time.sleep(5)

finally:
    time.sleep(30)
    browser.quit()
