
import pymongo

# Подключение
cl = pymongo.MongoClient("mongodb://localhost:27017/")
db = cl["Mydatabase"]
col = db["projects"]

# 1
filter_1 = [
        {"$group": {"_id": "$Назва мови якою створено", "count": {"$sum": 1}}}
    ]
request = col.aggregate(filter_1)
print(*request, sep='\n')

# 2
filter_2 = {'Кількість поінтів': {'$gte': 1500}}
request = col.find(filter_2)
print(*request, sep='\n')

# # 3
filter_3 = {'Назва проекту': {'$regex': 'Access'}}
request = col.find(filter_3)
print(*request, sep='\n')


# # 4

filter_4 = [
    {"$project": {
        "Назва проекту": 1,
        "length": {"$strLenCP": "$Назва проекту"}
    }},
    {"$sort": {"length": -1}},
    {"$limit": 1}
]

request = col.aggregate(filter_4)


for document in request:
    project_name = document['Назва проекту']
    print(project_name)
    break

filter_4_2 = {'Назва проекту': project_name}
request1 = col.count_documents(filter_4_2)
print(request1, sep='\n')


# # 5
filter_5 = {'$and': [{'Кількість поінтів': {'$lte': 800 }}, {'Кількість поінтів': {'$gt': 2000}}]}

request = col.count_documents(filter_5)
print(request)

