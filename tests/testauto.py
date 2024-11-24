from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def test_login_success():
    driver = webdriver.Firefox()
    driver.get("https://opensource-demo.orangehrmlive.com/")

    time.sleep(2)

    driver.find_element(By.NAME, "username").send_keys("Admin")

    time.sleep(2)

    driver.find_element(By.NAME, "password").send_keys("admin123")

    time.sleep(2)

    driver.find_element(By.CLASS_NAME, "orangehrm-login-button").click()

    time.sleep(2)

    assert "dashboard" in driver.current_url
    
    driver.quit()
test_login_success()