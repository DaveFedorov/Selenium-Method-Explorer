import time
import logging
import sys
from selenium.webdriver import ActionChains
from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

browser = webdriver.Chrome()

def alert(browser):
    browser.get("http://the-internet.herokuapp.com/javascript_alerts")
    JSalert = browser.find_element(By.XPATH, "/html/body/div[2]/div/div/ul/li[1]/button")
    JSalert.click()
    wait = WebDriverWait(browser, 10)
    alert = wait.until(EC.alert_is_present())
    text = alert.text
    alert.accept()
    print(text)


def confirm_box(browser):
    browser.find_element(By.XPATH, "/html/body/div[2]/div/div/ul/li[2]/button").click()
    wait = WebDriverWait(browser, 10)
    alert = wait.until(EC.alert_is_present())
    
    alert.dismiss()
    element = browser.find_element(By.ID, "result")
    if element.text == "You clicked: Cancel":
        print("confrim box dismissed")
    else:
        print("something went wrong")

def Prompt(browser):
    browser.find_element(By.XPATH, "/html/body/div[2]/div/div/ul/li[3]/button").click()
    wait = WebDriverWait(browser, 10)
    alert = wait.until(EC.alert_is_present())
   
    alert.send_keys("Something")
    alert.accept()
    element = browser.find_element(By.ID, "result")
    if element.text == "You entered: Something":
        print("looks fine to me ;)")
    else:
        print("something went wrong")

alert(browser)
time.sleep(1)
confirm_box(browser)
time.sleep(1)
Prompt(browser)
time.sleep(1)