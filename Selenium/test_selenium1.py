import time

import pytest
from selenium import webdriver
import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

def test_Basic_Orange(driver):
    LOGGER = logging.getLogger(__name__)
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    wait = WebDriverWait(driver, 10)
    name = wait.until(EC.presence_of_element_located((By.NAME, "username")))
    name.send_keys("Admin")

    password = driver.find_element(By.NAME, "password")
    password.send_keys("admin123")

    login = driver.find_element(By.CLASS_NAME,"oxd-button.oxd-button--medium.oxd-button--main.orangehrm-login-button")
    login.click()
    time.sleep(6)
    LOGGER.info(driver.title)

    assert "OrangeHRM" in driver.title
    time.sleep(5)

def test_Basic_Orange(driver):
    LOGGER = logging.getLogger(__name__)
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    wait = WebDriverWait(driver, 10)
    name = wait.until(EC.presence_of_element_located((By.NAME, "username")))
    name.send_keys("Admin")

    password = driver.find_element(By.NAME, "password")
    password.send_keys("admin123")

    login = driver.find_element(By.CLASS_NAME,"oxd-button.oxd-button--medium.oxd-button--main.orangehrm-login-button")
    login.click()
    time.sleep(6)
    LOGGER.info(driver.title)

    assert "OrangeHRM" in driver.title
    time.sleep(5)
