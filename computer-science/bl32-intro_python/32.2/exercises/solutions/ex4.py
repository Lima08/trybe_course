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
import json


with open('../helper/file_ex4.json') as file:
    # content = [json.loads(line) for line in file]
    # print(content[0]['title'])
    print(file.read())