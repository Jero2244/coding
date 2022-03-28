#! /usr/bin/python3

from selenium import webdriver
from selenium.webdriver.common.keys import Keys  
from selenium.webdriver.common.by import By 

browser = webdriver.Firefox()

browser.get('https://play2048.co/')

for i in range(75):
    try:
        tryAgain = browser.find_element(By.CSS_SELECTOR, '.retry-button')
        tryAgain.click()
        break
    except:
        htmlElem = browser.find_element(By.TAG_NAME, 'html')
        htmlElem.send_keys(Keys.UP)
        htmlElem.send_keys(Keys.RIGHT)
        htmlElem.send_keys(Keys.DOWN)
        htmlElem.send_keys(Keys.LEFT)

browser.close()
