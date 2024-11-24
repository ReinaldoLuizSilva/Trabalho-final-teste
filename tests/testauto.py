from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def test_login_success():
    driver = webdriver.Firefox()
    driver.get("https://opensource-demo.orangehrmlive.com/")

    # Entrar com credenciais válidas
    driver.find_element(By.ID, "txtUsername").send_keys("Admin")
    driver.find_element(By.ID, "txtPassword").send_keys("admin123")
    driver.find_element(By.ID, "btnLogin").click()

    # Verificar se o login foi bem-sucedido
    assert "dashboard" in driver.current_url.lower()
    driver.quit()
