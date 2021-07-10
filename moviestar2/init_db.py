from pymongo import MongoClient

import requests
from bs4 import BeautifulSoup

client = MongoClient('localhost', 27017)
#client = MongoClient('mongodb://test:test@localhost',27017)
db = client.dbaloe

def get_urls():
    headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    url="https://movie.naver.com/movie/sdb/rank/rpeople.nhn"
    data = requests.get(url, headers=headers)
    soup = BeautifulSoup(data.text,'html.parser')
    trs=soup.select("#old_content > table > tbody > tr")

    urls=[]
    for tr in trs:
        a=tr.select_one("td.title>a")
        if a is not None:
            url= "https://movie.naver.com/"+a['href']
            urls.append(url)

    return urls

def insert_star(url):
    headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    data = requests.get(url, headers=headers)
    soup = BeautifulSoup(data.text,'html.parser')

    name = soup.select_one("#content > div.article > div.mv_info_area > div.mv_info.character > h3 > a").text
    image = soup.select_one("#content > div.article > div.mv_info_area > div.poster > img")['src']
    work = soup.select_one("#content > div.article > div.mv_info_area > div.mv_info.character > dl > dd > a:nth-child(1)").text

    doc = {
        "name":name,
        "url":url,
        "image":image,
        "work":work,
        "like":0
    }

    db.star.insert_one(doc)

    print(name, "완료")

def insert_all():
    db.star.drop()
    urls=get_urls()
    for url in urls:
        insert_star(url)

insert_all()