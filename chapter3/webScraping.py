import requests
from bs4 import BeautifulSoup

#타겟 URL을 읽어서 HTML를 받아오고
#header 설정은 내가 프로그램이 아니라 사용자라고 알려주기 위해
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&date=20200303')

#HTML을 BeautifalSoup이라는 라이브러리를 활요ㅛㅇ해 검색하기 용이한 상태로 만듦
#soup이라는 변수에 "파실 용이해진 html"이 담긴 상태가 됨
#이제 코딩을 통해 필요한 부분을 추출하면 된다
soup = BeautifulSoup(data.text, 'html.parser')
#print(soup) #Html 받아온거 확인

#selet를 이용해서 tr들을 불러오기
movies = soup.select('#old_content > table > tbody > tr')
print(len(movies))

for movie in movies:
    #movie안에 a가 있으면,
    #조건을 만족하는 첫번째 요소, 없으면 none을 출력
    a_tag = movie.select_one('td.title > div > a')
    #print(a_tag) #<a href="/movie/bi/mi/basic.nhn?code=147092" title="히든 피겨스">히든 피겨스</a>
    if a_tag is not None:
        print(a_tag.text) #a_tag의 text를 찍어본다

#copy>copy selector하면 선택자를 얻을 수 있음
##old_content > table > tbody > tr:nth-child(2) > td.title > div > a        

#선택자 사용하는 방법
soup.select('태그명')
soup.select('.클래스명')
soup.select('#아이디 명')

soup.select('상위태그명 > 하위태그명 > 하위태그명')
soup.select('상위태그명.클래스명 > 하위태그명.클래스명')

#태그와 속성값으로 찾는 방법
soup.select('태그명[속성=값]')

#한개만 가져오고 싶은 경우
soup.select_one('위와 동일')