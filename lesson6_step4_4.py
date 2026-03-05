from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service  # новый импорт
from webdriver_manager.chrome import ChromeDriverManager  # новый импорт
import time

link = "http://suninjuly.github.io/find_xpath_form"


try:
    # Автоматически скачивает подходящий ChromeDriver и запускает браузер
    service = Service(ChromeDriverManager().install())
    browser = webdriver.Chrome(service=service)
    
    browser.get(link)

    input1 = browser.find_element(By.TAG_NAME, "input")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.NAME, "last_name")
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.CLASS_NAME, "city")  
    input3.send_keys("Smolensk")
    input4 = browser.find_element(By.ID, "country")
    input4.send_keys("Russia")
    button = browser.find_element(By.XPATH, "//button[text()='Submit']")
    button.click()

finally:
    time.sleep(30)
    # Проверяем, что браузер был создан, прежде чем закрывать
    if browser:
        browser.quit()