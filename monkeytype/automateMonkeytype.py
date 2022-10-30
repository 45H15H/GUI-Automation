from selenium import webdriver

import os

# add the path to the WebDriver executable
os.environ['PATH'] += "msedgedriver.exe"

# set options
options = webdriver.EdgeOptions()
options.add_argument("--ignore-certificate-errors")
driver = webdriver.Edge(options = options)

driver.get("https://monkeytype.com/")

driver.implicitly_wait(30)

# to click on "Accept All" button
cookie = driver.find_element("xpath", '//*[@id="cookiePopup"]/div[2]/div[2]/div[1]')
cookie.click()

# get the source of the page
source = driver.page_source

from bs4 import BeautifulSoup
import lxml

soup = BeautifulSoup(source, 'lxml')

# from that source extract the words which appear for typing
texts = soup.find('div', id = 'words')

word_list = [i.text for i in texts]
# only 100 words are scrapped


import pyautogui

# using pyautogui type those words from the word_list
for i in word_list:
    pyautogui.write(i, interval=0.01)
    pyautogui.press('space')


# optional: to close the browser
import time
time.sleep(5)
driver.close()
