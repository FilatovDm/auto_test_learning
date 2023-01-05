# https://stepik.org/lesson/228249/step/3?unit=200781

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

try:
    link = 'http://suninjuly.github.io/selects1.html'
    browser = webdriver.Chrome()
    browser.get(link)
    # time.sleep(1)

    num1_element = browser.find_element(By.ID, "num1")
    num1 = int(num1_element.text)
    num2_element = browser.find_element(By.ID, "num2")
    num2 = int(num2_element.text)
    sum_captcha = str(num1 + num2)
    # print(f'{num1} + {num2} = ', num1 + num2)

    Select(browser.find_element(By.TAG_NAME, "select")).select_by_value(sum_captcha)
    time.sleep(1)

    submit = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    submit.click()
    time.sleep(3)

finally:
    browser.quit()
