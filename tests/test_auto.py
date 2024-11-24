from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

def test_login_success():
    selenium_url = os.getenv("SELENIUM_REMOTE_URL", "http://localhost:4444/wd/hub")
    driver = webdriver.Remote(
        command_executor=selenium_url,
        options=webdriver.FirefoxOptions()
    )

    try:
        driver.get("https://opensource-demo.orangehrmlive.com/")


        WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.NAME, "username"))).send_keys("Admin")
        WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.NAME, "password"))).send_keys("admin123")
        WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.CLASS_NAME, "orangehrm-login-button"))).click()

        WebDriverWait(driver, 2).until(EC.url_contains("dashboard"))
        assert "dashboard" in driver.current_url.lower()

    finally:
        driver.quit()

def test_add_employee():
    selenium_url = os.getenv("SELENIUM_REMOTE_URL", "http://localhost:4444/wd/hub")
    driver = webdriver.Remote(
        command_executor=selenium_url,
        options=webdriver.FirefoxOptions()
    )
    
    try:
        driver.get("https://opensource-demo.orangehrmlive.com/")

        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "username"))).send_keys("Admin")
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "password"))).send_keys("admin123")
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "orangehrm-login-button"))).click()

        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[contains(@class, 'oxd-main-menu-item--name') and text()='PIM']"))).click()
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'oxd-button--secondary') and text()=' Add ']"))).click()
    
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "firstName"))).send_keys("Francisco")
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "lastName"))).send_keys("Beleza")
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[text()=' Save ']"))).click()
    
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//h6[contains(@class, 'oxd-text oxd-text--h6 orangehrm-main-title')]")))
        assert "Personal Details" in driver.page_source


    finally:
        driver.quit()
    