from bs4 import BeautifulSoup
from urllib.request import urlopen
url = urlopen(
'https://music.bugs.co.kr/chart/track/realtime/total?chartdate=20181114')
soup = BeautifulSoup(url, 'lxml')
n_artist = 0 #아티스트 수
n_title=0 #제목의 수

for i in soup.find_all(name='p', attrs=({"class":"artist"})):
    n_artist += 1 # += 는 누적
    print(str(n_artist)+" 위")  # 1위
    print("아티스트: "+i.find('a').text) # text 는 메소드가 아니라 속성값
print('------')

for i in soup.find_all(name='p', attrs=({"class","title"})):
    n_title += 1
    print(str(n_title)+" 위")
    print("노래제목:"+i.text)