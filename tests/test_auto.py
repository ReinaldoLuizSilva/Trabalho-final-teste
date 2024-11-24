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

        WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.NAME, "username"))).send_keys("Admin")
        WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.NAME, "password"))).send_keys("admin123")
        WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.CLASS_NAME, "orangehrm-login-button"))).click()

        WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.XPATH, "//span[contains(@class, 'oxd-main-menu-item--name') and text()='PIM']"))).click()
        WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'oxd-button--secondary') and text()=' Add ']"))).click()
    
        WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.NAME, "firstName"))).send_keys("Francisco")
        WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.NAME, "lastName"))).send_keys("Beleza")
        WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.XPATH, "//button[text()=' Save ']"))).click()
    
        WebDriverWait(driver, 2).until(EC.visibility_of_element_located((By.XPATH, "//h6[contains(@class, 'oxd-text oxd-text--h6 orangehrm-main-title')]")))

    finally:
        driver.quit()
    

def test_logout():
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

        WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.XPATH, "//i[contains(@class, 'oxd-icon bi-caret-down-fill oxd-userdropdown-icon')]"))).click()
        WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.XPATH, "//a[contains(@class, 'oxd-userdropdown-link')and text()='Logout']"))).click()

        WebDriverWait(driver, 2).until(EC.url_contains("login"))
        assert "login" in driver.current_url.lower()
    finally:
        driver.quit()

def test_navegacao():
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

        WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.XPATH, "//span[contains(@class, 'oxd-main-menu-item--name') and text()='Admin']"))).click()
        WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.XPATH, "//span[contains(@class, 'oxd-main-menu-item--name') and text()='PIM']"))).click()
        WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.XPATH, "//span[contains(@class, 'oxd-main-menu-item--name') and text()='Leave']"))).click()
        WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.XPATH, "//span[contains(@class, 'oxd-main-menu-item--name') and text()='Time']"))).click()
        
        WebDriverWait(driver, 2).until(EC.visibility_of_element_located((By.XPATH, "//h6[contains(@class, 'oxd-text oxd-text--h6 orangehrm-main-title')]")))
    finally:
        driver.quit()

def test_auterar_info():
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

        WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.XPATH, "//span[contains(@class, 'oxd-text oxd-text--span oxd-main-menu-item--name') and text()='My Info']"))).click()
        WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.NAME, "firstName"))).send_keys("Roberto")
        WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.NAME, "lastName"))).send_keys("Santos")
        WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.XPATH, "//input[contains(@class, 'oxd-input oxd-input--active')]"))).send_keys("1234")
        WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.XPATH, "//button[text()=' Save ']"))).click()

        WebDriverWait(driver, 2).until(EC.visibility_of_element_located((By.XPATH, "//h6[contains(@class, 'oxd-text oxd-text--h6 orangehrm-main-title')]")))

    finally:
        driver.quit()

def test_paginacao():
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

        WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.XPATH, "//span[contains(@class, 'oxd-main-menu-item--name') and text()='PIM']"))).click()
        WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.XPATH, "//i[contains(@class, 'oxd-icon bi-chevron-right')]"))).click()
        WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.XPATH, "//i[contains(@class, 'oxd-icon bi-chevron-right')]"))).click()
        WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.XPATH, "//i[contains(@class, 'oxd-icon bi-chevron-left')]"))).click()
        WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.XPATH, "//i[contains(@class, 'oxd-icon bi-chevron-left')]"))).click()

        WebDriverWait(driver, 2).until(EC.visibility_of_element_located((By.XPATH, "//h5[contains(@class, 'oxd-text oxd-text--h5 oxd-table-filter-title')]")))

    finally:
        driver.quit()

def test_deletar_funcionario():
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

        WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.XPATH, "//span[contains(@class, 'oxd-main-menu-item--name') and text()='PIM']"))).click()
        WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.XPATH, "//i[contains(@class, 'oxd-icon bi-trash')]"))).click()
        WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.XPATH, "//button[text()=' Yes, Delete ']"))).click()
    finally:
        driver.quit()

def test_busca_funcionario():
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

        WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.XPATH, "//span[contains(@class, 'oxd-main-menu-item--name') and text()='PIM']"))).click()
        WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.XPATH, "//input[@data-v-1f99f73c='']"))).send_keys("0007")

        WebDriverWait(driver, 2).until(EC.visibility_of_element_located((By.XPATH, "//span[contains(text(), ' (1) Records Found')]")))
    
    finally:
        driver.quit()
