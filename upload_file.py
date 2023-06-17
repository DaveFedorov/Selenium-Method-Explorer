import time
import logging
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By 


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
    if (browser.page_source.find("File Uploaded!")):
           print("File uploaded!")
    else:
        print("File is not uploaded!")
    
    

run_upload()