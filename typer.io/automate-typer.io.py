import time

from selenium import webdriver

import os

os.environ['PATH'] += "msedgedriver.exe"

options = webdriver.EdgeOptions()
options.add_argument("--ignore-certificate-error")

driver = webdriver.Edge(options = options)

driver.get("https://typer.io")

# this is for maximizing the window
driver.maximize_window()

driver.implicitly_wait(30)

quickPlay = driver.find_element("xpath", '//*[@id="__next"]/main/div/section[1]/div[2]/a[1]')
quickPlay.click()

# #scroll by pixel
# driver.execute_script("window.scrollBy(0,200)","")

time.sleep(3)

try:
    driver.execute_script("scrollBy(0,-1000);") # -> this is for scrolling, see -ve sign for
    print("scrolling successful!") #  scrolling up, use +ve for scrolling down, it is the value of pixels
except:
    print("scrolling failed!")
time.sleep(3)

source = driver.page_source



from bs4 import BeautifulSoup
import lxml

soup = BeautifulSoup(source, 'lxml')

text_ = soup.find('div', class_ = "Gameboard_container__QyjKg")
wordList = [i.text for i in text_]

print(len(wordList))
print(wordList)


# time.sleep(15) we don't want to wait by time, we wait till go appears
# we want to wait till the timer starts, and then start typing.

from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait # -> this is wrong import
from selenium.webdriver.support.wait import WebDriverWait # -> this is the correct import
from selenium.webdriver.support import expected_conditions

'''
# initiate explicit wait
WebDriverWait(driver, 15).until(
    expected_conditions.text_to_be_present_in_element(
        # first argument is text to check, then second is text to appear
        (By.XPATH, '//*[@id="__next"]/div[2]/div[1]/div[2]/div[2]/h3'),
        'GO!' # -> this is the text we wait till it appears
    )
)
# when "GO! will appear we imeaditly execute the following task
'''

# initiate explicit wait
WebDriverWait(driver, 20).until(expected_conditions.text_to_be_present_in_element((By.XPATH, '//*[@id="__next"]/div[2]/div[1]/div[2]/div'), "GO!"))

try:
    type_here_when_the_game_begins  = driver.find_element("xpath", '//*[@id="__next"]/div[2]/div[1]/div[4]/div/div')
    type_here_when_the_game_begins.click()
    print("clikc succefull!")
except:
    print("element not found!")


# time.sleep(17)

import pyautogui

print('started')
for j in wordList:
    pyautogui.write(j)
    pyautogui.press("space")

time.sleep(20)
driver.close()