import time
import logging
import sys
from selenium.webdriver import ActionChains
from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.support import expected_conditions as EC


def run_move_slider():
    browser = webdriver.Chrome()
    browser.get("http://the-internet.herokuapp.com/horizontal_slider")
    time.sleep(2)
    range = browser.find_element(By.ID, "range")
    previous_text = range.text
    time.sleep(2)
    slider = browser.find_element(By.XPATH, '/html/body/div[2]/div/div/div/input')
    action_chains = ActionChains(browser)
    action_chains.move_to_element(slider).click_and_hold().move_by_offset(50, 0).release().perform()
    time.sleep(2)
    range_u = browser.find_element(By.ID, "range")
    current_text = range_u.text
    if previous_text != current_text:
        print("valuse is changed!")
    else:
        print("valuse is NOT changed!")

    
    

run_move_slider()
