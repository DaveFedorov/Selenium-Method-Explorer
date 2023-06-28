from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def verify_elements_presence():
    browser = webdriver.Chrome()
    browser.get("https://the-internet.herokuapp.com/large")
    counts = []
    for row_num in range(1, 51):
        row_class = f"row-{row_num}"
        row = browser.find_element(By.CLASS_NAME, row_class)
        one_l = 0
        for col_num in range(1, 51):
            col_class = f"column-{col_num}"
            column = row.find_element(By.CLASS_NAME, col_class)

            if column.is_displayed():
                one_l += 1 
        counts.append(one_l)
    all_table_elements = sum(counts)
    if all_table_elements == 2500:
        print("all elements are present")
    else: print(f"only {all_table_elements} of 2500 elements are present")
verify_elements_presence()