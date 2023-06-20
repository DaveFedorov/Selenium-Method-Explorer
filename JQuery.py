import time
import logging
import sys
from selenium.webdriver import ActionChains
from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.support import expected_conditions as EC
browser = webdriver.Chrome()

def go_to_menu(browser):
  browser.get("http://the-internet.herokuapp.com/jqueryui")
  time.sleep(3)
  menu_link = browser.find_element(By.LINK_TEXT, "Menu")
  menu_link.click()
def download_files(browser):
  download_dict = {
    "PDF" : browser.find_element(By.ID, "ui-id-6"),
    "CSV" : browser.find_element(By.ID, "ui-id-7"),
    "Excel" : browser.find_element(By.ID, "ui-id-8")
  }
  for x, y in download_dict.items():
    enabled_button = browser.find_element(By.ID, "ui-id-2")
    enabled_button.click()
    downloads_button = browser.find_element(By.ID, "ui-id-4")
    downloads_button.click()
    time.sleep(1)
    browser.execute_script("arguments[0].click();", y)

go_to_menu(browser)
download_files(browser)