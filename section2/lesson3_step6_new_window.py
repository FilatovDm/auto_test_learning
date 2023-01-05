# https://stepik.org/lesson/184253/step/6?unit=158843

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import result_for_stepik

try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element(By.CSS_SELECTOR, ".trollface").click()

    second_window = browser.window_handles[1]
    browser.switch_to.window(second_window)


    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))


    x = browser.find_element(By.ID, "input_value").text
    browser.find_element(By.ID, "answer").send_keys(calc(x))
    browser.find_element(By.CSS_SELECTOR, ".btn").click()
    time.sleep(1)

    result_for_stepik.input_result(browser)

finally:
    time.sleep(15)
    browser.quit()
