from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import math
import time

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

link = "http://suninjuly.github.io/redirect_accept.html"

try:
    # Автоматическая загрузка драйвера
    service = Service(ChromeDriverManager().install())
    browser = webdriver.Chrome(service=service)
    browser.get(link)

    # Нажимаем на кнопку
    button = browser.find_element(By.CSS_SELECTOR, "button.trollface")
    button.click()

    # Получаем список всех вкладок и переключаемся на новую
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    # На новой странице решаем капчу
    # Считываем значение x
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)

    # Вводим ответ
    answer_input = browser.find_element(By.ID, "answer")
    answer_input.send_keys(y)

    # Нажимаем кнопку Submit
    submit_button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    submit_button.click()

    
finally:
    time.sleep(50)
