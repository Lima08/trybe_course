# Exercício 1:
# Faça um programa que solicite o nome de uma pessoa usuária
# e imprima-o na vertical.
# Exemplo:
# F
# U
# L
# A
# N
# O
name = input('Escreva seu nome: ')
for letter in name:
    print(letter)


# Exercício 2:
# Escreva um programa que receba vários números naturais e calcule a soma
#  desses valores. Caso algum valor da entrada seja inválido,
#  por exemplo uma letra, uma mensagem deve ser exibida,
#  na saída de erros, no seguinte formato:
# "Erro ao somar valores, {valor} é um valor inválido". Ao final,
# você deve imprimir a soma dos valores válidos.
# 🦜 Receba os valores em um mesmo input ,
# solicitando à pessoa usuária que separe-os com um espaço.
# Receba os valores no formato str e utilize o método
# split para pegar cada valor separado. O método isdigit,
#  embutido no tipo str , pode ser utilizado para verificar se a string
#  corresponde a um número natural.
nums = input('Escreva varios numeros separados por espaço ')
numbers = nums.split(' ')

total = 0

for number in numbers:
    if not number.isdigit():
        print(f"Erro ao somar valores, {number} é um valor inválido")
    else:
        total += int(number)

print(total)


# Exercício 3: Dado um arquivo contendo estudantes e suas respectivas notas,
#  escreva um programa que lê todas essas informações e filtre
# mantendo somente as pessoas que estão reprovadas,
#  e escreva seus nomes em outro arquivo. A nota miníma para aprovação é 6.
# Arquivo:
# Marcos 10
# Felipe 4
# José 6
# Ana 10
# Maria 9
# Miguel 5

# Exemplo saída:
# Felipe
# Miguel

# 🦜 A função split pode ser utilizada para dividir o nome em uma linha.
# Ex: line.split -> ["Marcos", "10"]

estudantes_reprovados = []
with open('exercises/helper/file.txt') as notas_estudantes:
    for line in notas_estudantes:
        estudante = line.split()
        if int(estudante[1]) < 6:
            estudantes_reprovados.append(estudante[0])
print(estudantes_reprovados)

with open('exercises/helper/reproved.txt', mode='w') as lista_reprovados:
    for estudante in estudantes_reprovados:
        lista_reprovados.write(estudante + '\n')
        print(estudante)
