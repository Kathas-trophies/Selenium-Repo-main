import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os

#logging configuration
logging.basicConfig(
    level=logging.INFO, 
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='login4_test.log',
    filemode='w'
)

#define the function
def test_login_popup(driver):
    file_path = os.path.abspath("Login_Page.html")
    logging.info("Opening file: %s", file_path)
    driver.get("file://" + file_path)

#Test execution
    try:
    #Test case 001: Valid details
        #logging.info("Enter email and password")
        #driver.find_element(By.CLASS_NAME, "email").send_keys("Selenium25@gmail.com")
        #driver.find_element(By.CLASS_NAME, "password").send_keys("Y0uMade1t&3&&")
        #driver.find_element(By.ID, "login-btn").click()
    #Test case 002: Invalid email
        #logging.info("Enter email and password")
        #driver.find_element(By.CLASS_NAME, "email").send_keys("Selenium25@gmail")
        #driver.find_element(By.CLASS_NAME, "password").send_keys("Y0uMade1t&3&&")
        #driver.find_element(By.ID, "login-btn").click()
    #Test case 003: Invalid Password
        #logging.info("Enter email and password")
        #driver.find_element(By.CLASS_NAME, "email").send_keys("Selenium25@gmail.com")
        #driver.find_element(By.CLASS_NAME, "password").send_keys("Y0uMade")
        #driver.find_element(By.ID, "login-btn").click()
    #Test case 004: Empty fields
        logging.info("Enter email and password")
        driver.find_element(By.CLASS_NAME, "email").send_keys("")
        driver.find_element(By.CLASS_NAME, "password").send_keys("")
        driver.find_element(By.ID, "login-btn").click()
        #Take a screenshot
        driver.save_screenshot("screenshot4_before_popup.png")
        logging.info("Screenshot saved before popup appears")
        #Wait for Popup & Validate
        wait = WebDriverWait(driver, 10)
        popup = wait.until(EC.visibility_of_element_located((By.ID, "login-popup")))
        popup_message = driver.find_element(By.ID, "login-popup-message").text
        logging.info("Popup message: %s", popup_message)
        #Assert to validate the behaviour
        assert popup.is_displayed(), "Login did not display the popup."
        assert "success" in popup_message.lower(), f"Unexpected message: {popup_message}"

        logging.info("Login popup test passed on %s", driver.name)
        time.sleep(5)
#Error handling
    except Exception as e:
        logging.error("An error occured during testting: %s", e)
        driver.save_screenshot("error4_screenshot.png") #try jpg as well - failed
        raise
#Run the test
chrome_driver = webdriver.Chrome()
test_login_popup(chrome_driver)
chrome_driver.quit()