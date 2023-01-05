# https://stepik.org/lesson/228249/step/5?unit=200781

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

try:
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    input_field = browser.find_element(By.CSS_SELECTOR, "input[type='text']:required")
    input_field.send_keys(calc(x))
    time.sleep(1)

    check_box_robo = browser.find_element(By.ID, "robotCheckbox")
    check_box_robo.click()

    submit_btn = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    browser.execute_script("return arguments[0].scrollIntoView(true);", submit_btn)

    radio_robo_rule = browser.find_element(By.ID, "robotsRule")
    radio_robo_rule.click()

    submit_btn.click()
    time.sleep(5)

finally:
    time.sleep(30)
    browser.quit()
