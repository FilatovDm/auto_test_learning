from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
	link = "http://suninjuly.github.io/registration1.html"
	browser = webdriver.Chrome()
	browser.get(link)

	input1 = browser.find_element(By.CSS_SELECTOR, 'div.first_block>div.first_class>input.first')
	input1.send_keys('Ivan')
	input2 = browser.find_element(By.CSS_SELECTOR, "div.first_block>div.second_class>input.second")
	input2.send_keys('Ivanov')
	input3 = browser.find_element(By.CSS_SELECTOR, "div.first_block>div.third_class>input.third")
	input3.send_keys('ivan89ivanov@gmail.com')

	# Отправляем заполненную форму
	button = browser.find_element(By.CSS_SELECTOR, "button.btn")
	button.click()

	# Проверяем, что смогли зарегестрироваться
	# ждем загрузки страницы
	time.sleep(1)

	# находим элемент, содержащий текст
	welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
	# записываем в переменную welcome_text текст из элемента welcome_text_elt
	welcome_text = welcome_text_elt.text

	# с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
	assert "Congratulations! You have successfully registered!" == welcome_text

finally:
	# ожидание чтобы визуально оценить результаты прохождения скрипта
	time.sleep(10)
	# закрываем браузер после всех манипуляций
	browser.quit()