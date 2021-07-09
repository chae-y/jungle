from pymongo import MongoClient
from flask import Flask, render_template, jsonify, request
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

client = MongoClient('localhost', 27017)
#client = MongoClient('mongodb://test:test@localhost',27017)
db = client.dbaloe

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get', methods=['GET'])
def show():
    memos = list(db.memo.find({},{'_id':False}))
    return jsonify({'result':'success', 'memo_list':memos})

@app.route('/post',methods={'POST'})
def insert():
    url_receive = request.form['url_give']
    comment_receive = request.form['comment_give']

    headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    data = requests.get(url_receive, headers=headers)
    soup = BeautifulSoup(data.text,'html.parser')

    og_title = soup.select_one('meta[property="og:title"]')
    og_image = soup.select_one('meta[property="og:image"]')
    og_des = soup.select_one('meta[property="og:description"]')

    doc = {
        "title":og_title['content'],
        "image":og_image['content'],
        "description":og_des['content'],
        "url":url_receive,
        "comment":comment_receive
    }

    db.memo.insert_one(doc)
   
    # article = {'url':url_receive, 'title':og_title['content'], 'desc':og_des['content'], 'image':og_image['content'], 'comment':comment_receive}
    
    # # 3. mongoDB에 데이터 넣기
    # db.articles.insert_one(article)

    return jsonify({'result':'success'})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
