# https://stepik.org/lesson/228249/step/8?unit=200781

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

try:
    link = 'http://suninjuly.github.io/file_input.html'
    browser = webdriver.Chrome()
    browser.get(link)

    with open("step8.txt", "w") as file:
        file.write('stepik cool!')

    browser.find_element(By.CSS_SELECTOR, "[name='firstname']").send_keys("Dmitry")
    browser.find_element(By.CSS_SELECTOR, "[name='lastname']").send_keys("Filatov")
    browser.find_element(By.CSS_SELECTOR, "[name='email']").send_keys("filatov@mail.com")

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, "step8.txt")
    browser.find_element(By.CSS_SELECTOR, "[type='file']").send_keys(file_path)

    print(file_path)

    browser.find_element(By.CSS_SELECTOR, "[type='submit']").click()
    time.sleep(5)

finally:
    time.sleep(30)
    browser.quit()
