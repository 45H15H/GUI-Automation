import time

from selenium import webdriver

# below imports are for explicit wait
from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait # -> this is wrong import
from selenium.webdriver.support.wait import WebDriverWait # -> this is the correct import
from selenium.webdriver.support import expected_conditions

import os

# keep the driver file in the project folder itself
os.environ['PATH'] += "msedgedriver.exe"

options = webdriver.EdgeOptions()
options.add_argument("--ignore-certificate-error")

driver = webdriver.Edge(options = options)

driver.get("https://typer.io")

# maximize the window
driver.maximize_window()

# implicitly wait for the page to completely load
driver.implicitly_wait(30)

quickPlay = driver.find_element("xpath", '//*[@id="__next"]/main/div/section[1]/div[2]/a[1]')
quickPlay.click()

# time.sleep(3)
# here also we don't want to wait for 3 seconds to scroll when the play site has been opened
# so apply explicit wait here
WebDriverWait(driver, 5).until(expected_conditions.url_matches("https://typer.io/play"))
# here use url_matches(), not url_changes()
# url_changes() is used to check if the previous ulr changed
# url_matches() checks if the current url is matched or not

# Scrolling up
driver.execute_script("scrollBy(0,-1000);")

# wait for the page to completely load before taking the source
time.sleep(3)
source = driver.page_source

# Scrape the text
from bs4 import BeautifulSoup
import lxml

soup = BeautifulSoup(source, 'lxml')

text_ = soup.find('div', class_ = "Gameboard_container__QyjKg")
wordList = [i.text for i in text_]

# initiate explicit wait, (wait till GO! has appeared)
WebDriverWait(driver, 20).until(expected_conditions.text_to_be_present_in_element((By.XPATH, '//*[@id="__next"]/div[2]/div[1]/div[2]/div'), "GO!"))

type_here_when_the_game_begins  = driver.find_element("xpath", '//*[@id="__next"]/div[2]/div[1]/div[4]/div/div')
type_here_when_the_game_begins.click()

import pyautogui

print('started')
for j in wordList:
    pyautogui.write(j)
    pyautogui.press("space")

# close the browser
time.sleep(20)
driver.close()