import time
import logging
from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains
from selenium.webdriver.common.alert import Alert
from selenium.common.exceptions import NoAlertPresentException

def run_drag_and_drop():
    browser = webdriver.Chrome()
    browser.get("http://the-internet.herokuapp.com/context_menu")
    time.sleep(1)
    element = browser.find_element(By.ID, "hot-spot")
    action = ActionChains(browser)
    action.context_click(element).perform()
    try:
        alert = Alert(browser)
        print('alert is shown')
        alert.accept()
    except NoAlertPresentException:
        print("no alert is shown")
    time.sleep(3)
run_drag_and_drop()
