import pandas as pd
import numpy as np
import platform
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

rc('font', family=font_manager.FontProperties(
    fname='C:/Windows/Fonts/malgun.ttf').get_name())
# size, family

print('# 설정 되어있는 폰트 사이즈')
print(plt.rcParams['font.size'])
print('# 설정 되어있는 폰트 글꼴')
print(plt.rcParams['font.family'])  # ['Malgun Gothic']

from selenium import webdriver
import time

driver = webdriver.Chrome('C:/Users/ezen/PycharmProjects/chromedriver.exe')

nec = 'http://info.nec.go.kr/main/showDocument.xhtml? electionId = 0000000000 & topMenuId = VC & secondMenuId = VCCP09'
driver.get(nec)

# driver.switch_to_default_content() # 상위 프레임이동.
# 아래 명령에서 에러발생 방지
# driver.switch_to_frame('main') # 원하는 프레임 이동
# 대통령선거라는 글자부분을 클릭

driver.find_element_by_id("electionType1").click()
driver.find_element_by_id("electionName").send_keys("제19대")
driver.find_element_by_id("electionCode").send_keys("대통령선거")
sido_list_raw = driver.find_element_by_xpath("""//*[@id="cityCode"]""")
sido_list = sido_list_raw.find_elements_by_tag_name("option")
sido_names_values = [option.text for option in sido_list]
sido_names_values = sido_names_values[2:]
sido_names_values

# ['서울특별시', '부산광역시', '대구광역시',
# '인천광역시', '광주광역시', '대전광역시',
# '울산광역시', '세종특별자치시', '경기도',
# '강원도', '충청북도', '충청남도', '전라북도',
# '전라남도', '경상북도', '경상남도',
# '제주특별자치도']

"""
19대 대선 개표 결과 데이터 획득하기
"""

import re
def get_num(tmp):
    return float(re.split('\(', tmp)[0].replace(',', ''))

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

wait = WebDriverWait(driver, 10)

def move_sido(name):
    element = driver.find_element_by_id("cityCode")
    element.send_keys(name)
    make_xpath = """//*[@id="searchBtn"]"""
    wait.until(EC.element_to_be_clickable((By.XPATH, make_xpath)))
    driver.find_element_by_xpath(make_xpath).click()

"""
append_data 함수선언
빈 내용으로 미리 준비한 DataFrame에 append 명령으로 읽은
데이터를 하나씩 추가하는 기능
"""


def append_data(df, sido_name, data):
    for each in df[0].values[1:]:
        data['광역시도'].append(sido_name)
        data['시군'].append(each[0])
        data['pop'].append(get_num(each[2]))
        data['moon'].append(get_num(each[3]))
        data['hong'].append(get_num(each[4]))
        data['ahn'].append(get_num(each[5]))

election_result_raw = {'광역시도': [],
                       '시군': [],
                       'pop': [],
                       'moon': [],
                       'hong': [],
                       'ahn': []}

from bs4 import BeautifulSoup
for each_sido in sido_names_values:
    move_sido(each_sido)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    table = soup.find('table')
    df = pd.read_html(str(table))
    append_data(df, each_sido, election_result_raw)

election_result = pd.DataFrame(election_result_raw,
                               columns=['광역시도', '시군', 'pop', 'moon', 'hong', 'ahn'])

election_result