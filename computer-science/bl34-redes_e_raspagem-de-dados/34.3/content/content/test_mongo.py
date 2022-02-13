# from pymongo import MongoClient

# client = MongoClient()
# db = client.catalogue
# documents = [
#     {
#         "title": "A Light in the Attic",
#     },
#     {
#         "title": "Tipping the Velvet",
#     },
#     {
#         "title": "Soumission",
#     },
# ]
# ids_news = db.books.insert_many(documents).inserted_ids
# print(ids_news)
# client.close()  # fecha a conexão com o banco de dados

# Pegando os itens no banco --------------------------------------------
# from pymongo import MongoClient

# client = MongoClient()
# db = client.catalogue
# # busca um documento da coleção, sem filtros
# print(db.books.find_one())
# # busca utilizando filtros
# for book in db.books.find({"title": {"$regex": "t"}}):
#     print(book["title"])
# client.close()  
#  ouu....
# -------------------------------------

from pymongo import MongoClient


with MongoClient() as client:
    db = client.catalogue
    for book in db.books.find({"title": {"$regex": "t"}}):
        print(book["title"])
