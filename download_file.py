import time
import logging
from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.chrome.options import Options

def run_drag_and_drop():
    chrome_options = webdriver.ChromeOptions()
    prefs = {
        "download.default_directory": f"W:\\the_internet_project\\downloads",
        "safebrowsing.enabled": "false"
    }
    chrome_options.add_experimental_option("prefs", prefs)
    browser = webdriver.Chrome(options=chrome_options)
    browser.get("http://the-internet.herokuapp.com/download")
    download_link = browser.find_element(By.XPATH, '//*[@id="content"]/div/a[25]')
    download_link.click()

    time.sleep(5)

run_drag_and_drop()