from konlpy.tag import Okt
import re
from nltk.tokenize import word_tokenize

"""
import  nltk
nltk.download()
"""



"""
ctx='C:/Users/ezen/PycharmProjects/Day0406/web_craw/Data/'
filename= ctx+'kr-Report_2018.txt'

"""

okt = Okt()

okt.pos("삼성전자 글로벌센터 전자사업부", stem=True)

# ***********

# 1 text 문서에서 token 추출하기

# ***********

# Step 1 - pdf 에서 변환한 Document 불러오기

filename = 'C:/Users/ezen/PycharmProjects/Day0406/web_craw/Data/kr-Report_2018.txt'

with open(filename, 'r', encoding='utf-8') as f:

    texts = f.read()

texts[:300]

# Step 2 - 한글만 추출

import re

texts     = texts.replace('\n', ' ')   # 해당줄의 줄바꿈 내용 제거
tokenizer = re.compile(r'[^ ㄱ-힣]+')   # 한글과 띄어쓰기를 제외한 모든 글자를 선택
texts     = tokenizer.sub('', texts)   # 한글과 띄어쓰기를 제외한 모든 부분을 제거
texts[:300]

# Step 3 - Token으로 변환한다

from nltk.tokenize import word_tokenize

tokens    = word_tokenize(texts)

tokens[:7]

# Step 4 - 복합명사는 묶어서 Filtering 출력

# ex) 삼성전자의 스마트폰은 -- > 삼성전자 스마트폰
noun_token = []
for token in tokens:
    token_pos = okt.pos(token)
    temp      = [txt_tag[0]   for txt_tag in token_pos
                              if txt_tag[1] == 'Noun']
    if len("".join(temp)) > 1:
        noun_token.append("".join(temp))
texts = " ".join(noun_token)
texts[:300]

# **************
# 2. StopWord 데이터 필터링
# ***************

# stopwords.txt : 2015, 2016, 2017, 2018 모두 출현했던 단어들 불러오기

with open('C:/Users/ezen/PycharmProjects/Day0406/web_craw/Data/stopwords.txt', 'r', encoding='utf-8') as f:
    stopwords = f.read()
stopwords = stopwords.split(' ')
stopwords[:10]

# 필터링 텍스트를 살펴보기

from nltk.tokenize import word_tokenize
texts = word_tokenize(texts)
texts[:8]

# Stopwords 를 활용하여 Token을 필터링
texts = [text for text in texts
              if text not in stopwords]
# pandas 를 활용하여 상위빈도 객체를 출력한다
import pandas as pd
from nltk import FreqDist
freqtxt = pd.Series(dict(FreqDist(texts))).sort_values(ascending=False)  #Python 자료구조 4가지 학습
freqtxt[:30]

# ************
# 3 Konlpy 의 단점들
# 오타/ 비정형 텍스트의 처리
# ************

from konlpy.tag import Okt

okt = Okt()
okt.pos('가치창출')
okt.pos('갤러시')  #오타는 갤럭시로 처리

# ************
# 4 WordCloud 출력
# ************
# wordcloud 출력

from wordcloud import WordCloud

wcloud = WordCloud('C:/Users/ezen/PycharmProjects/Day0406/web_craw/Data/D2Coding.ttf',
                   relative_scaling = 0.2,
                   background_color = 'white').generate(" ".join(texts))
wcloud

import matplotlib.pyplot as plt
plt.figure(figsize=(12,12))
plt.imshow(wcloud, interpolation='bilinear')
plt.axis("off")
plt.show()