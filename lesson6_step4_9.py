from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import os
import time

# Создаем временный текстовый файл для загрузки
with open("file.txt", "w") as file:
    file.write("Hello, world!")

# Получаем путь к файлу
current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, "file.txt")

link = "http://suninjuly.github.io/file_input.html"

try:
    # Автоматическая загрузка драйвера
    service = Service(ChromeDriverManager().install())
    browser = webdriver.Chrome(service=service)
    browser.get(link)

    # Заполняем поля
    first_name = browser.find_element(By.NAME, "firstname")
    first_name.send_keys("Ivan")
    
    last_name = browser.find_element(By.NAME, "lastname")
    last_name.send_keys("Petrov")
    
    email = browser.find_element(By.NAME, "email")
    email.send_keys("ivan@example.com")

    # Загружаем файл
    file_input = browser.find_element(By.ID, "file")
    file_input.send_keys(file_path)

    # Нажимаем кнопку Submit
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    time.sleep(30)
    if 'browser' in locals():
        browser.quit()
    # Удаляем временный файл
    if os.path.exists(file_path):
        os.remove(file_path)