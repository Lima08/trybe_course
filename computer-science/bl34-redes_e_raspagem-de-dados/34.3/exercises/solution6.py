# Exercício 6
#  Importe o arquivo
# https://s3.us-east-2.amazonaws.com/assets.app.betrybe.com/computer-science/python/entrada-saida/books-346aab4788ea58d4c3aa988632da100b.json
# no MongoDB antes de responder as próximas questões.
# comando -->  mongoimport --db library books.json
from pymongo import MongoClient

category = input('Escolha uma categoria: ')
with MongoClient() as client:
    db = client.library
    for book in db.book.find({"categories": category}, projection=["title"]):
        print(book['title'])
