import time
import logging
from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains

def run_drag_and_drop():
    browser = webdriver.Chrome()
    browser.get("http://the-internet.herokuapp.com/dropdown")
    time.sleep(1)
    dropdown_list = browser.find_element(By.ID, "dropdown")
    select = Select(dropdown_list)
    select.select_by_index(0)
    selected_option = select.first_selected_option
    print(selected_option.text)

    time.sleep(3)
run_drag_and_drop()
