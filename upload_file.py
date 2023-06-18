import time
import logging
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.common.exceptions import NoSuchElementException

def run_upload():
    file_path = 'W:\\the_internet_project\\downloads\\robot.txt'

    browser = webdriver.Chrome()
    browser.get("http://the-internet.herokuapp.com/upload")
    time.sleep(2)
    upload_element = browser.find_element(By.ID, 'file-upload')
    upload_element.send_keys(file_path)
    time.sleep(2)
    cofirm_upload_button = browser.find_element(By.ID, 'file-submit')
    cofirm_upload_button.click()
    time.sleep(2)
    try:
        is_visible = browser.find_element(By.ID, "uploaded-files").is_displayed()
    except NoSuchElementException:
        is_visible = False
    if (is_visible):
           print("File uploaded!")
    else:
        print("File is not uploaded!")

    

run_upload()