import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

class TestRegistration(unittest.TestCase):
    
    def setUp(self):
        # Автоматическая загрузка драйвера перед каждым тестом
        service = Service(ChromeDriverManager().install())
        self.browser = webdriver.Chrome(service=service)
    
    def tearDown(self):
        # Закрываем браузер после каждого теста
        time.sleep(3)
        self.browser.quit()
    
    def test_registration1(self):
        # Тест для первой страницы регистрации
        link = "http://suninjuly.github.io/registration1.html"
        self.browser.get(link)
        
        # Заполняем обязательные поля
        first_name = self.browser.find_element(By.CSS_SELECTOR, ".first_block .first")
        first_name.send_keys("Ivan")
        
        last_name = self.browser.find_element(By.CSS_SELECTOR, ".first_block .second")
        last_name.send_keys("Petrov")
        
        email = self.browser.find_element(By.CSS_SELECTOR, ".first_block .third")
        email.send_keys("ivan@example.com")
        
        # Отправляем форму
        button = self.browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()
        
        # Находим элемент с текстом благодарности
        welcome_text = self.browser.find_element(By.TAG_NAME, "h1").text
        
        # Проверяем, что ожидаемый текст совпадает с полученным
        expected_text = "Congratulations! You have successfully registered!"
        self.assertEqual(welcome_text, expected_text, f"Текст на странице '{welcome_text}' не совпадает с ожидаемым")
    
    def test_registration2(self):
        # Тест для второй страницы регистрации
        link = "http://suninjuly.github.io/registration2.html"
        self.browser.get(link)
        
        # Заполняем обязательные поля
        first_name = self.browser.find_element(By.CSS_SELECTOR, ".first_block .first")
        first_name.send_keys("Ivan")
        
        last_name = self.browser.find_element(By.CSS_SELECTOR, ".first_block .second")
        last_name.send_keys("Petrov")
        
        email = self.browser.find_element(By.CSS_SELECTOR, ".first_block .third")
        email.send_keys("ivan@example.com")
        
        # Отправляем форму
        button = self.browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()
        
        # Ждем загрузки страницы
        time.sleep(1)
        
        # Находим элемент с текстом благодарности
        welcome_text = self.browser.find_element(By.TAG_NAME, "h1").text
        
        # Проверяем, что ожидаемый текст совпадает с полученным
        expected_text = "Congratulations! You have successfully registered!"
        self.assertEqual(welcome_text, expected_text, f"Текст на странице '{welcome_text}' не совпадает с ожидаемым")

if __name__ == "__main__":
    unittest.main()