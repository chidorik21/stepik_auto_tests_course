from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import math
import time

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

link = "https://suninjuly.github.io/math.html"

try:
    service = Service(ChromeDriverManager().install())
    browser = webdriver.Chrome(service=service)
    browser.get(link)

    # Считываем значение x
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)

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

    # Ждём появления алерта и выводим код
    time.sleep(2)
    alert = browser.switch_to.alert
    print("Полученный код:", alert.text)
    alert.accept()

finally:
    # Даём время увидеть результат
    time.sleep(5)
    if 'browser' in locals():
        browser.quit()