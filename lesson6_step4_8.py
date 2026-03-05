from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import math
import time

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

link = "https://SunInJuly.github.io/execute_script.html"

try:
    # Автоматическая загрузка драйвера
    service = Service(ChromeDriverManager().install())
    browser = webdriver.Chrome(service=service)
    browser.get(link)

    # Считываем значение x
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)

    # Прокручиваем страницу вниз, чтобы все элементы стали видимыми
    browser.execute_script("window.scrollBy(0, 150);")

    # Вводим ответ
    answer_input = browser.find_element(By.ID, "answer")
    answer_input.send_keys(y)

    # Отмечаем checkbox
    robot_checkbox = browser.find_element(By.ID, "robotCheckbox")
    robot_checkbox.click()

    # Выбираем radiobutton
    robots_radio = browser.find_element(By.ID, "robotsRule")
    robots_radio.click()

    # Нажимаем кнопку Submit
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
  
finally:
    time.sleep(30)
    if 'browser' in locals():
        browser.quit()