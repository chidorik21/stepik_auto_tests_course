from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
import time

link = "https://suninjuly.github.io/selects1.html"

try:
    # Автоматическая загрузка драйвера
    service = Service(ChromeDriverManager().install())
    browser = webdriver.Chrome(service=service)
    browser.get(link)

    # Находим числа
    num1 = browser.find_element(By.ID, "num1")
    num2 = browser.find_element(By.ID, "num2")
    
    # Получаем их значения и считаем сумму
    x = int(num1.text)
    y = int(num2.text)
    sum_result = x + y

    # Находим выпадающий список и выбираем нужное значение
    select = Select(browser.find_element(By.ID, "dropdown"))
    select.select_by_value(str(sum_result))

    # Нажимаем кнопку Submit
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    

finally:
    # Даём время увидеть результат
    time.sleep(20)
    if 'browser' in locals():
        browser.quit()