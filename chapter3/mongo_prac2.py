from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbjungle

#Q1. 영화제목 매트릭스의 평점 가져오기
mat = db.movies.find_one({'title':'매트릭스'})
print(mat['star'])

#Q2. 매트릭스의 평점과 같은 영화 제목 가져오기
movies = list(db.movies.find({}))
for movie in movies:
    if mat['star']==movie['star']:
        print(movie['title'])

#Q3. 매트릭스 영화 평점을 0으로 만들기
db.movies.update_one({'title':'매트릭스'},{'$set':{'star':0}})
print(mat['star'])