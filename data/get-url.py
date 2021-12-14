# 모듈 import
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import time

def get_url_list(url='https://page.kakao.com/main?categoryUid=11&subCategoryUid=1101'):
    url_list = []

    options = Options()
    options.add_argument('--kiosk')


    browser = webdriver.Chrome("./chromedriver.exe", chrome_options=options)
    browser.get(url)

    SCROLL_PAUSE_TIME = 0.4

    # Get scroll height
    last_height = browser.execute_script("return document.body.scrollHeight")

    while True:

        elements = browser.find_elements_by_css_selector("a")

        for e in elements:
            if 'seriesId' in e.get_attribute('href'):
                # print(e.get_attribute('href'))
                url_list.append(e.get_attribute('href'))

        # Scroll down to bottom
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Wait to load page
        time.sleep(SCROLL_PAUSE_TIME)
        new_height = browser.execute_script("return document.body.scrollHeight")

        if new_height == last_height:
            break
        last_height = new_height

    # csv로 저장
    url_series = pd.Series(url_list)
    url_series.to_csv('kkp_url.csv', index=True)
    return url_series

get_url_list()