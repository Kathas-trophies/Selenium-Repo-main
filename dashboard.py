from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

#Set up the webdriver
driver = webdriver.Chrome()

try:
    driver.get("file:///Users/kathi/Documents/04_Weiterbildung/2025/01_Bildungskarenz/03_Code-Factory/01_Software-Testing/Module_12_Exercises/Selenium-Repo-main/Dashboard.html")
    time.sleep(2)
    #Testcase001: Check if the welcome message is displayed
    #header = driver.find_element(By.TAG_NAME, 'h1')
    #assert "Welcome, Thabelo!" in header.text
    #print("Welcome message is displayed")
    #TestCase002: Check if the logout button exists
    #logout_btn = driver.find_element(By.CLASS_NAME, "logout-btn")
    #assert logout_btn.is_displayed() and logout_btn.is_enabled()
    #print("Logout button exists")
    #TestCase003: Type in searchbox
    #searchbox = driver.find_element(By.ID, "search-box")
    #assert searchbox.is_displayed()
    #searchbox.send_keys("It works")
    #print("The searchbox has been successfully filled")
    #TestCase004: Chose a date
    #date = driver.find_element(By.ID, "calendar")
    #date.send_keys("24/08/2025")
    #print("Successfully entered date")
    #TestCase005: Find an image
    image = driver.find_element(By.CSS_SELECTOR, ".profile-img img")
    assert image.get_attribute("src")!=""
    print("Image found")
except AssertionError as e:
    print("Test failed",e)
except Exception as e:
    print("Error occurred",e)
finally:
    time.sleep(2)
    driver.quit()