from tkinter.tix import TCL_DONT_WAIT
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def main():
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    browser = webdriver.Chrome("C:/Users/Ossi/Downloads/chromedriver_win32/chromedriver.exe", options=options)
    browser.get('https://basket.fi/basket/sarjat/pelaajatilastot/?league_id=4&season_id=125119')
    #print(browser.current_url)
    element = browser.find_element(by=By.CLASS_NAME, value='mbt-v2-widget-content')
    #element = browser.find_element_by_class_name('mbt-v2-widget-content')
    #print(element)
    #print(element.text)
    rows = browser.find_elements(by=By.TAG_NAME, value='tr')
    for row in rows:
        cells = row.find_elements(by=By.TAG_NAME, value='td')
        for i, c in enumerate(cells):
            print(cells[i].text)

    browser.quit()

main()