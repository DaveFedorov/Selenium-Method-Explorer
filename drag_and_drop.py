import time
import logging
from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains

def run_drag_and_drop():
    browser = webdriver.Chrome()
    browser.get("http://the-internet.herokuapp.com/drag_and_drop")
    time.sleep(1)
    column_A = browser.find_element(By.ID, "column-a")
    column_B = browser.find_element(By.ID, "column-b")
    target_position = column_A.location
    action = ActionChains(browser)
    action.drag_and_drop_by_offset(column_B, target_position["x"] + 20, target_position["y"] + 20).perform()
    time.sleep(3)
run_drag_and_drop()
