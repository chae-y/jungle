from pymongo import MongoClient
from flask import Flask, render_template, jsonify, request

client = MongoClient('localhost', 27017)
#client = MongoClient('mongodb://test:test@localhost',27017)
db = client.dbaloe

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get', methods=['GET'])
def show():
    stars = list(db.star.find({},{'_id':False}).sort('like',-1))
    return jsonify({'result':'success', 'star_list':stars})

@app.route('/like',methods={'POST'})
def like():
    name_receive = request.form['name_give']
    star = db.star.find_one({'name':name_receive})
    db.star.update_one({'name':name_receive},{'$set':{'like':star['like']+1}})
    return jsonify({'result':'success'})

@app.route('/delete',methods={'POST'})
def delete():
    name_receive = request.form['name_give']
    db.star.delete_one({'name':name_receive})
    return jsonify({'result':'success'})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)