from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import math
import time

link = "http://suninjuly.github.io/find_link_text"

browser = None
try:
    # Автоматическая загрузка подходящего ChromeDriver
    service = Service(ChromeDriverManager().install())
    browser = webdriver.Chrome(service=service)
    browser.get(link)

    # Вычисляем текст ссылки по формуле
    link_text = str(math.ceil(math.pow(math.pi, math.e) * 10000))
    # Находим ссылку с точным текстом и кликаем
    link_element = browser.find_element(By.LINK_TEXT, link_text)
    link_element.click()

    # Небольшая пауза для загрузки формы регистрации
    time.sleep(1)

    # Заполняем форму (аналогично предыдущему шагу урока)
    # Поле "first name"
    first_name = browser.find_element(By.NAME, "first_name")
    first_name.send_keys("Ivan")
    # Поле "last name"
    last_name = browser.find_element(By.NAME, "last_name")
    last_name.send_keys("Petrov")
    # Поле "city"
    city = browser.find_element(By.CLASS_NAME, "city")
    city.send_keys("Smolensk")
    # Поле "country"
    country = browser.find_element(By.ID, "country")
    country.send_keys("Russia")
    # Кнопка отправки
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Ждём появления результата
    time.sleep(2)

    # Переключаемся на алерт и получаем код
    alert = browser.switch_to.alert
    code = alert.text
    print("Полученный код:", code)
    alert.accept()

finally:
    # Дополнительная пауза, чтобы увидеть результат
    time.sleep(5)
    if browser:
        browser.quit()