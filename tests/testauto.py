from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def test_login_success():
    driver = webdriver.Firefox()
    driver.get("https://opensource-demo.orangehrmlive.com/")

    time.sleep(2)

    # Localizar o campo de usuário e senha e o botão de login usando a classe dos elementos
    driver.find_element(By.NAME, "username").send_keys("Admin")

    time.sleep(2)

    driver.find_element(By.NAME, "password").send_keys("admin123")

    time.sleep(2)

    driver.find_element(By.CLASS_NAME, "orangehrm-login-button").click()

    # Aguardar o carregamento da página após o login
    time.sleep(2)

    # Verificar se o login foi bem-sucedido
    assert "dashboard" in driver.current_url.lower()
    
    driver.quit()
