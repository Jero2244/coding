#! /usr/bin/python3

from selenium import webdriver
from selenium.webdriver.common.keys import Keys  
from selenium.webdriver.common.by import By 
import sys
import pyinputplus as pyip

browser  = webdriver.Firefox()
browser.get('https://sjmulder.nl/en/textonly.html')

links = browser.find_elements(By.TAG_NAME, 'a')
for link in links:
    try:
        href = link.get_attribute('href')
        browser.get(href)
        browser.back()
    except:
        print(f'{href} cannot be opened')
        browser.back()
        continue

        