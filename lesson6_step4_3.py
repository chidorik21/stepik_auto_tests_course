from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

try:
    # Автоматическая загрузка подходящего ChromeDriver
    service = Service(ChromeDriverManager().install())
    browser = webdriver.Chrome(service=service)
    
    browser.get("http://suninjuly.github.io/huge_form.html")
    
    # Находим все поля ввода на странице (тег input)
    elements = browser.find_elements(By.TAG_NAME, "input")
    for element in elements:
        element.send_keys("Мой ответ")
    
    # Находим кнопку и кликаем
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # Ждём 30 секунд, чтобы увидеть результат
    time.sleep(30)
    # Закрываем браузер, если он был создан
    if 'browser' in locals() and browser:
        browser.quit()