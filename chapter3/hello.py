#1번
fruits=['사과', '배', '배', '감', '수박', '귤', '딸기', '사과', '배', '수박']

def count_fruit(target):
    count =0
    for fruit in fruits:
        if fruit== target:
            count+=1
    print(count)

count_fruit('배')

#2번
people = [{'name': 'bob', 'age': 20}, 
          {'name': 'carry', 'age': 38},
          {'name': 'john', 'age': 7},
          {'name': 'smith', 'age': 17},
          {'name': 'ben', 'age': 27}]

def age(target):
    for person in people:
        if person['name']==target:
            return person['age']
    return "해당이름이 없습니다."

print(age('bob'))
print(age('bop'))