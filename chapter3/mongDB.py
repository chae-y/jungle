from pymongo import MongoClient #pymongo 패키지
client = MongoClient('localhost',27017) #몯고디비는 27017 포트로 돌아감
db = client.dbsparta #'dbsparta'라는 이름의 db를 만듦

#1 MongoDB에 insert하기
"""
#'users'라는 collection에 {'name':'bobby', 'age':21} 넣기
#db.users.insert_one({'name':'bobby','age':21})
#db.users.insert_one({'name':'kay','age':27})
#db.users.insert_one({'name':'john','age':30})
"""

#2 MongDB에서 데이터 보기
"""
all_users=list(db.users.find({}))
#특정조건 보기
same_ages=list(db.users.find({'age':27}))
#특정키값 뺴고 보기
user1 = db.users.find_one({'name':'bobby'},{'_id':False})

print(all_users[0])
print(all_users[0]['name'])
print(user1)

for user in all_users:
    print(user)
"""

#3 수정하기

#생김새
#db.people.update_many(찾을조건,{ '$set':어떻게 바꿀지})
db.users.update_one({'name':'bobby'},{'$set':{'age':19}})
user = db.users.find_one({'name':'bobby'})
print(user)

#4 삭제하기

db.users.delete_one({'name':'bobby'})
user = db.users.find_one({'name':'bobby'})
print(user)
