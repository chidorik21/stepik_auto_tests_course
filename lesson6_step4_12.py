from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
import time

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

link = "http://suninjuly.github.io/explicit_wait2.html"

try:
    # Автоматическая загрузка драйвера
    service = Service(ChromeDriverManager().install())
    browser = webdriver.Chrome(service=service)
    browser.get(link)

    # Ждем, когда цена станет $100 (ожидание до 12 секунд)
    price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )

    # Нажимаем кнопку Book
    book_button = browser.find_element(By.ID, "book")
    book_button.click()

    # Решаем математическую задачу
    # Считываем значение x
    x_element = WebDriverWait(browser, 5).until(
        EC.presence_of_element_located((By.ID, "input_value"))
    )
    x = x_element.text
    y = calc(x)

    # Вводим ответ
    answer_input = browser.find_element(By.ID, "answer")
    answer_input.send_keys(y)

    # Нажимаем кнопку Submit
    submit_button = browser.find_element(By.ID, "solve")
    submit_button.click()

finally:
    time.sleep(30)
