# 모듈 import
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver

import time
import re

home_url = 'https://page.kakao.com'

# 웹 브라우저 열기
browser = webdriver.Chrome("./chromedriver.exe")
browser.get(home_url)
time.sleep(5)

def login():

    input_id = 'input your ID'
    input_pw = 'input your PassWord'
    # 로그인 창 열기
    login = browser.find_element_by_xpath('//*[@id="kpw-header"]/div/div/button/div[3]')
    login.click()
        # 로그인 창으로 전환
    browser.switch_to.window(browser.window_handles[1])

    # 로그인 정보 입력
    browser.find_element_by_id("id_email_2").send_keys(input_id)
    browser.find_element_by_id("id_password_3").send_keys(input_pw)

    # 로그인
    browser.find_element_by_class_name("btn_g.btn_confirm.submit").click()

    # 원래 창으로 돌아오기
    browser.switch_to.window(browser.window_handles[0])


def get_novel_info(url, browser=browser):

    info_url = url
    info_list = {}

    # 새 탭으로 열기
    browser.execute_script(f"window.open('{info_url}')")
    time.sleep(1.5)
    # 새 탭으로 전환
    browser.switch_to.window(browser.window_handles[1])

    # 서비스 종료 팝업창 끄기
    try:
        close_popup = browser.find_element_by_class_name("jsx-3114325382.modalClose.modalClose_pc.title")
        close_popup.click()
    except:
        pass

    # id
    idx = url.split('=')[1]
    info_list['id'] = idx

    # 제목
    title = browser.find_element_by_class_name("text-ellipsis.css-jgjrt").text
    info_list['Title'] = title

    # 독자 수
    readers = browser.find_element_by_class_name("css-fjzm5m").text
    info_list['Readers'] = readers

    # 전체 댓글 수
    comments = browser.find_element_by_class_name("css-12ymafv").text
    info_list['Total Comments'] = comments

    # 연재 요일, 작가
    days_writer = browser.find_elements_by_class_name("text-ellipsis.css-7a7cma")
    days_of_week = days_writer[0].text
    info_list['Days of Week'] = days_of_week
    writer = days_writer[1].text
    info_list['Writer'] = writer

    # 전체 화수
    try:
        episodes = browser.find_element_by_xpath('//*[@id="root"]/div[3]/div/div/div[4]/div[1]/div[1]').text
    # 웹에서 서비스 되지 않는 소설은 이하를 수행
    except:
        episodes = browser.find_element_by_xpath('//*[@id="root"]/div[3]/div/div/div[5]/div[1]/div[1]').text
    info_list['Total Episodes'] = int(re.sub(r"[^0-9]", "", episodes))

    # 작품 소개
    button = browser.find_element_by_xpath('//*[@id="root"]/div[3]/div/div/div[1]/div[1]/div[2]/div[3]/div[2]/button[1]')
    button.click()
    time.sleep(0.5)
    description = browser.find_element_by_xpath('/html/body/div[2]/div/div/div/div[2]/div/div/table/tbody/tr[1]/td[2]/div[1]').text
    info_list['Description'] = description

    # 장르
    genre = browser.find_element_by_xpath('/html/body/div[2]/div/div/div/div[2]/div/div/table/tbody/tr[1]/td[2]/div[2]/div[2]').text
    info_list['Genre'] = genre

    # 연령등급
    grade = browser.find_element_by_xpath('/html/body/div[2]/div/div/div/div[2]/div/div/table/tbody/tr[1]/td[2]/div[4]/div[2]').text
    info_list['Grade'] = grade

    browser.close()

    # 기존 창으로 전환
    browser.switch_to.window(browser.window_handles[0])
    
    return info_list


url_df = pd.read_csv('./kkp_url.csv')[['0']]
print(url_df.head())

# 빈 데이터 프레임 생성
df = pd.DataFrame(index=range(0,3), columns=['id', 'Title', 'Writer', 'Readers', 'Total Comments', 'Genre', 'Grade', 'Days of Week', 'Total Episodes', 'Description'])

# 로그인
login()

# 데이터 저장
for url in url_df['0']:
    info = get_novel_info(url)
    df = df.append(info, ignore_index=True)
    if len(df) % 200 == 0:
        df.iloc[3:].to_csv('kkp_info3.csv', encoding='utf-8-sig')

df.iloc[3:].to_csv('kkp_info3.csv', encoding='utf-8-sig')