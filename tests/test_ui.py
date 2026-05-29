import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import os

@pytest.fixture
def driver():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    
    path = os.path.abspath("index.html")
    driver.get(f"file://{path}")
    yield driver
    driver.quit()

def test_title(driver):
    assert "Форма регистрации" in driver.title

def test_button(driver):
    btn = driver.find_element(By.ID, "submitBtn")
    assert "Отправить" in btn.text

def test_h1_text(driver):
    h1 = driver.find_element(By.ID, "title")
    assert h1.text == "Добро пожаловать!"

def test_form_submission(driver):
    input_field = driver.find_element(By.ID, "username")
    btn = driver.find_element(By.ID, "submitBtn")
    
    input_field.send_keys("Ivan")
    btn.click()
    
    message = driver.find_element(By.ID, "message")
    assert message.is_displayed()