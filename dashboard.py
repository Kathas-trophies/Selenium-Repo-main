from selenium import webdriver
from selenium.webdriver.common.by import By
import time

#Set up the webdriver
driver = webdriver.Chrome()

try:
    driver.get("/Users/kathi/Documents/04_Weiterbildung/2025/01_Bildungskarenz/03_Code-Factory/01_Software-Testing/Module_12_Exercises/Selenium-Repo-main/Dashboard.html")
    time.sleep(2)
    #Testcase001: Check if the welcome message is displayed
    header = driver.find_element(By.TAG_NAME, 'h1')
    assert "Welcome, Thabelo!" in header.text
    print("Welcome message is displayed")
except AssertionError as e:
    print("Test failed",e)
except Exception as e:
    print("Error occurred",e)
finally:
    time.sleep(2)
    driver.quit()