from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    input1 = browser.find_element(By.CSS_SELECTOR, '[name="firstname"]')
    print(input1)
    input1.send_keys("Margo")
    input2 = browser.find_element(By.CSS_SELECTOR, '[name="lastname"]')
    print(input2)
    input2.send_keys("Mor")
    input3 = browser.find_element(By.CSS_SELECTOR, '[name="email"]')
    print(input3)
    input3.send_keys("m@gmail.com")

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_name = "text.txt"
    file_path = os.path.join(current_dir, file_name)
    element = browser.find_element(By.CSS_SELECTOR, '[type="file"]')
    element.send_keys(file_path)

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, '[type="submit"]')
    button.click()



finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()