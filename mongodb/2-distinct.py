from pymongo import MongoClient

# 1 - Conectando com o banco MongoDB e o Database
client = MongoClient()
db = client['nobel']
prizes = db['prizes']
laureates = db['laureates']

# 2 - Lista o mapeamento de generos 

print(db.laureates.distinct('gender'))

# 3 - Lista o mapeamento de categoria de premios

print(db.laureates.distinct('prizes.category'))

# 4 - Count categorias ale de fisica tem laureados com ações trimestrais

print(db.laureates.distinct(
    'prizes.category',
    {'prizes.share': '4'}
))

# 5 - Categorias que ganharam mais de um premio

print(db.laureates.distinct(
    'prizes.category',
    {'prizes.1':{
        '$exists': True
    }}
))