from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

def test_login_success():
    # Conecta ao Selenium Remote WebDriver
    selenium_url = os.getenv("SELENIUM_REMOTE_URL", "http://localhost:4444/wd/hub")
    driver = webdriver.Remote(
        command_executor=selenium_url,
        options=webdriver.FirefoxOptions()
    )

    try:
        # Acessa o site
        driver.get("https://opensource-demo.orangehrmlive.com/")

        # Espera até que o campo de usuário esteja presente e interage com ele
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "username"))).send_keys("Admin")

        # Interage com o campo de senha
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "password"))).send_keys("admin123")

        # Clica no botão de login
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "orangehrm-login-button"))).click()

        # Confirma se o redirecionamento para o dashboard foi feito
        WebDriverWait(driver, 10).until(EC.url_contains("dashboard"))
        assert "dashboard" in driver.current_url

    finally:
        driver.quit()
