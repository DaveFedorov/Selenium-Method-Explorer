from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def verify_elements_presence():
    browser = webdriver.Chrome()
    browser.get("https://the-internet.herokuapp.com/large")
    for row_num in range(1, 51):
        row_class = f"row-{row_num}"
        row = browser.find_element(By.CLASS_NAME, row_class)
        for col_num in range(1, 51):
            col_class = f"column-{col_num}"
            column = row.find_element(By.CLASS_NAME, col_class)
            for f_num in range(1,51):
                for s_num in range(1, 51):
                    column_text = f"{f_num}.{s_num}"
                    if column.text == column_text:
                        print("all objects present")
                    else: print("not all objects present")

verify_elements_presence()