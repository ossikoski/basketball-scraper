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
    browser.get('https://www.basket.fi/basket/sarjat/sarja/?season_id=119175&league_id=4')
    print(browser.current_url)
    element = browser.find_element_by_class_name('mbt-v2-widget-content')
    print(element)
    print(element.text)
    all_links = browser.find_elements_by_tag_name('a')
    print(all_links)
    browser.quit()

main()