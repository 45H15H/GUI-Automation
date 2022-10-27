from selenium import webdriver

import os
os.environ['PATH'] = "C:\Users\Ashish/ Singh\Documents\GitHub\GUI-Automation\msedgedriver.exe"

options = webdriver.EdgeOptions()
options.add_argument("--ignore-certificate-errors")
driver = webdriver.Edge(options = options)

driver.get("https://monkeytype.com/")

driver.implicitly_wait(30)


 
cookie = driver.find_element("xpath", '//*[@id="cookiePopup"]/div[2]/div[2]/div[1]')
cookie.click()

source = driver.page_source

from bs4 import BeautifulSoup
import lxml
soup = BeautifulSoup(source, 'lxml')

texts = soup.find('div', id = 'words')

word_list = [i.text for i in texts]
# only 100 words are scrapped


import pyautogui

for i in word_list:
    pyautogui.write(i, interval=0.01)
    pyautogui.press('space')


# time.sleep(5)
# driver.close()
