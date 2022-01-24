# Exercício 4:
# Dado o arquivo file_ex4.json em no diretorio helper
# , leia seu conteúdo e calcule a porcentagem de livros em cada categoria,
#  em relação ao número total de livros.
# O resultado deve ser escrito em um arquivo no
#  formato CSV como no exemplo abaixo.

# Saída:
# categoria,porcentagem
# Python,0.23201856148491878
# Java,0.23201856148491878
# PHP,0.23201856148491878
from email import header
import json
import csv

books_by_categories = {}
counter_books = 0
categories_books_percentage = {}


with open('../helper/file_ex4.json') as file:
    content = [json.loads(line) for line in file]
    for book in content:
        counter_books += 1
        if len(book['categories']) > 0:
            for categorie in book['categories']:
                if categorie in books_by_categories.keys():
                    print(categorie)
                    books_by_categories[categorie] += 1
                else:
                    books_by_categories[categorie] = 1
    print(books_by_categories)
    print(counter_books)


for key in books_by_categories.keys():
    print(f'Resultado do percentual = {(books_by_categories[key] / counter_books)}')
    categories_books_percentage[key] = books_by_categories[key] / counter_books

print(categories_books_percentage)

with open('../helper/file_result_ex4.csv', mode='w') as result:

    headers = ['categoria', 'porcentagem']
    writer = csv.DictWriter(result, fieldnames=headers)
    writer2 = csv.writer(file)

    headerscsv = {'categoria': 'categoria', 'porcentagem': 'porcentagem'}
    writer.writerow(headerscsv)
    for categoria, porcentagem in categories_books_percentage.items():
        print(categoria)
        print(porcentagem)
        row = {'categoria': categoria, 'porcentagem': porcentagem}
        writer.writerow(row)
