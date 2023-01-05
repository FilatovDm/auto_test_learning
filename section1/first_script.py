import time

# webdriver это и есть набор команд для управления браузером
from selenium import webdriver

# импортируем класс By, который позволяет выбрать способ поиска элемента
from selenium.webdriver.common.by import By

# Инициализируем драйвер браузера. После этой команды вы должны увидеть новое открытое окно браузера
driver = webdriver.Chrome()
username = "filatov-d@mail.ru"
password = "***************"
# команда time.sleep устанавливает паузу в 2 секунды, чтобы мы успели увидеть, что происходит в браузере
time.sleep(2)

# Метод get сообщает браузеру, что нужно открыть сайт по указанной ссылке
driver.get("https://stepik.org/lesson/25969/step/12")
time.sleep(5)

submit_btn = driver.find_element(By.CSS_SELECTOR, ".navbar__auth")
submit_btn.click()
time.sleep(5)

s_username = driver.find_element(By.ID, "id_login_email")
s_username.send_keys(username)
time.sleep(5)

s_password = driver.find_element(By.ID, "id_login_password")
s_password.send_keys(password)
time.sleep(5)

sign_in_btn = driver.find_element(By.CSS_SELECTOR, ".sign-form__btn")
sign_in_btn.click()
time.sleep(7)

# Метод find_element позволяет найти нужный элемент на сайте, указав путь к нему.
# Способы поиска элементов мы обсудим позже
# Метод принимает в качестве аргументов способ поиска и значение, по которому мы будем искать.
# Ищем поле для ввода текста
textarea = driver.find_element(By.CSS_SELECTOR, ".textarea")

# Напишем текст ответа в найденное поле
textarea.send_keys("get()")
time.sleep(5)

# Найдем кнопку, которая отправляет введенное решение
submit_button = driver.find_element(By.CSS_SELECTOR, ".submit-submission")

# Скажем драйверу, что нужно нажать на кнопку. После этой команды мы должны увидеть сообщение о правильном ответе
submit_button.click()
time.sleep(5)

# После выполнения всех действий мы должны не забыть закрыть окно браузера
driver.quit()
