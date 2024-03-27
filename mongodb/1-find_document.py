from pymongo import MongoClient

# 1 - Conectando com o banco MongoDB e o Database
client = MongoClient()
db = client['nobel']
print(db.list_collection_names())
prizes = db['prizes']
laureates = db['laureates']

# 2 - Contando documentos pelo genero
print(db.laureates.count_documents({'gender': 'female'}))
print(db.laureates.count_documents({'gender': 'male'}))

# 3 - Filtro composto com mais informações

filter_doc= {
    'diedCountry': 'France',
    'gender': 'female',
    'bornCity': 'Warsaw'
}

print(db.laureates.count_documents(filter_doc))

# 4 - Buscando documento pelo filtro

print(db.laureates.find_one(filter_doc))

# 5 - Usando os operadore in(sql) e ne(not)

print(db.laureates.count_documents({'diedCountry': {'$in': ['France', 'Germany']}}))
print(db.laureates.count_documents({'diedCountry': {'$ne': 'France'}}))

# 6 - Buscando em subestruturas

california = db.laureates.count_documents({
    'prizes.affiliations.name': 'University of California'
})

print(california)

san_francisco = db.laureates.count_documents({
    'prizes.affiliations.city': 'San Francisco, CA'
})

print(san_francisco)

# 7 - Contando documentos que possuem uma informação

qtd = db.laureates.count_documents({
    'prizes.1': {
        '$exists': True
    }
})
print(qtd)

no_coutry = db.laureates.count_documents({
    'bornCountry': {
        '$exists': False
    }
})

print(f"Não possui pais de morte: {no_coutry}")