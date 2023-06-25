import time
import logging
import sys
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

browser = webdriver.Chrome()

def key_press(browser):
    browser.get("http://the-internet.herokuapp.com/key_presses")
    action = ActionChains(browser)
    result = browser.find_element(By.ID, "result")
    keys_to_press = ["q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "a", "s", "d", "f", "g", "h", "j", "k", "l", "z", "x", "c", "v", "b", "n", "m",]

    for key in keys_to_press:
        action.send_keys(key)
        time.sleep(0.1)
        action.perform()

        if key == "q" and result.text == "You entered: Q":
            print("'Q' key entered")
        elif key == "w" and result.text == "You entered: W":
            print("'W' key entered")
        elif key == "e" and result.text == "You entered: E":
            print("'E' key entered")
        elif key == "r" and result.text == "You entered: R":
            print("'R' key entered")
        elif key == "t" and result.text == "You entered: T":
            print("'T' key entered")
        elif key == "y" and result.text == "You entered: Y":
            print("'Y' key entered")
        elif key == "u" and result.text == "You entered: U":
            print("'U' key entered")
        elif key == "i" and result.text == "You entered: I":
            print("'I' key entered")
        elif key == "o" and result.text == "You entered: O":
            print("'O' key entered")
        elif key == "p" and result.text == "You entered: P":
            print("'P' key entered")
        elif key == "a" and result.text == "You entered: A":
            print("'A' key entered")
        elif key == "s" and result.text == "You entered: S":
            print("'S' key entered")
        elif key == "d" and result.text == "You entered: D":
            print("'D' key entered")
        elif key == "f" and result.text == "You entered: F":
            print("'F' key entered")
        elif key == "g" and result.text == "You entered: G":
            print("'G' key entered")
        elif key == "h" and result.text == "You entered: H":
            print("'H' key entered")
        elif key == "j" and result.text == "You entered: J":
            print("'J' key entered")
        elif key == "k" and result.text == "You entered: K":
            print("'K' key entered")
        elif key == "l" and result.text == "You entered: L":
            print("'L' key entered")
        elif key == "z" and result.text == "You entered: Z":
            print("'Z' key entered")
        elif key == "x" and result.text == "You entered: X":
            print("'X' key entered")
        elif key == "c" and result.text == "You entered: C":
            print("'C' key entered")
        elif key == "v" and result.text == "You entered: V":
            print("'V' key entered")
        elif key == "b" and result.text == "You entered: B":
            print("'B' key entered")
        elif key == "n" and result.text == "You entered: N":
            print("'N' key entered")
        elif key == "m" and result.text == "You entered: M":
            print("'M' key entered")
        else:
            print(f"Unknown key: {key}")

    browser.quit()
key_press(browser)
        

