# Exercícios de Fixação
# Devem ser resolvidos diretamente no terminal. Comece com o comando python3 .
# Lembre-se que cada linha representa um comando no terminal.
# Exercício 1: No terminal, inicialize duas variáveis a e b, sendo a = 10 e b = 5. Mostre o resultado das 7 operações básicas (soma, subtração, multiplicação, divisão, divisão inteira, potenciação e módulo) envolvendo essas variáveis.

a = 10
b = 5
a + b
a - b
a * b
a / b
a // b
a ** b
a % b

# Exercício 2: Declare e inicialize uma variável: hours = 6 . Quantos minutos têm em 6 horas? E quantos segundos? Declare e inicialize variáveis minutes e seconds que recebem os respectivos resultados das contas. Depois, imprima cada uma delas.

hours = 6
minutes = hours * 60
seconds = minutes * 60
minutes
seconds

# Exercício 3: Teste e verifique o que acontece se você colocar um ponto e vírgula no final de uma instrução em Python.
# Assim como em JavaScript, Python permite que você coloque um ponto e vírgula no final de uma instrução.
# Exercício 4: Suponha que o preço de capa de um livro seja 24,20, mas as livrarias recebem um desconto de 40%. O transporte custa 3,00 para o primeiro exemplar e 75 centavos para cada exemplar adicional. Qual é o custo total de atacado para 60 cópias? Escreva uma expressão que receba o custo total e a imprima.

books = 60
book_price = (1 - 0.4) * 24.20
logistic = 3 + (books - 1) * 0.75
cost = books * book_price + logistic
cost

# Copie a lista abaixo para realizarmos os exercícios de fixação 5 e 6:

trybe_course = ["Introdução", "Front-end", "Back-end"]

# Exercício 5: Adicione o elemento "Ciência da Computação" à lista.

trybe_course.append("Ciência da Computação")

# Exercício 6: Acesse e altere o primeiro elemento da lista para "Fundamentos".

trybe_course[0] = "Fundamentos"

# Exercício 7: Um conjunto ou set pode ser inicializado utilizando-se também o método set() . Inicialize uma variável com essa função var = set() e adicione seu nome ao conjunto utilizando um dos métodos vistos acima. Depois, imprima a variável e confira se o retorno é: {'seu_nome'}.

var = set()
var.add("Lauro Cesar")
var

# Utilizando o código abaixo, faça os exercícios de fixação 8, 9 e 10:

info = {
    "personagem": "Margarida",
    "origem": "Pato Donald",
    "nota": "Namorada do personagem principal nos quadrinhos do Pato Donald",
}

# Exercício 8: O que acontecerá se você tentar acessar o valor da chave "personagem" como fazíamos em JavaScript, utilizando object.key ?
# Essa forma de acesso ao objeto em Python não é permitida, resultando em erro de sintaxe.
# Exercício 9: Insira no objeto uma nova propriedade com o nome de chave "recorrente" e o valor "Sim". Em seguida, imprima o objeto no console.

info["recorrente"] = "Sim"

# Exercício 10: Remova a propriedade cuja chave é "origem" e imprima o objeto no console.

del info["origem"]

# Exercício 11: Após uma consulta do banco de dados, temos linhas que contém nome, sobrenome e idade como: "Thiago", "Nobre", 29 . Que estrutura vista anteriormente seria recomendada dado que após esta consulta somente exibimos estes valores.
# A estrutura recomendada é a tuple . Caso houvesse necessidade de editar os valores ou adicionar mais valores, usaríamos uma list .
# Exercício 12: Realizar a contagem de quantas vezes cada elemento aparece em uma sequência é uma técnica muito útil na solução de alguns problemas. Qual estrutura mais recomendada para armazenamento desta contagem?
# dict é a estrutura mais adequada, pois conseguimos armazenar o elemento da lista como chave e a quantidade de vezes que ele aparece como valor da chave.

my_list = [20, 20, 1, 2]
count_elements = {20: 2, 1: 1, 2: 2}

# Exercício 13: O Fatorial de um número inteiro é representado pela multiplicação de todos os números predecessores maiores que 0. Por exemplo o fatorial de 5 é 120 pois 5! = 1 * 2 * 3 * 4 * 5 . Escreva um código que calcule o fatorial de um número inteiro.

number = 5
counter = 1
result = 1

while counter <= number:
    result = result * counter
    counter += 1
result

# Note que usamos counter += 1 pra incrementar o contador -- não existe counter++ . Da mesma forma, poderíamos ter atualizado o resultado com a expressão result *= counter .
# Uma versão mais pythonica dessa solução usaria range :

number = 5
result = 1
# Usamos number + 1 pro range ir até o number
for factor in range(1, number + 1):
    result *= factor
result

# Exercício 14: Um sistema de avaliações registra valores de 0 a 10 para cada avaliação. Após algumas mudanças estes valores precisam ser ajustados para avaliações de 0 a 100. Dado uma sequência de avaliações ratings = [6, 8, 5, 9, 10] . Escreva um código capaz de gerar as avaliações após a mudança. Neste caso o resultado deveria ser [60, 80, 50, 90, 100] .

ratings = [6, 8, 5, 9, 10]
new_ratings = []

for rating in ratings:
    new_ratings.append(rating * 10)

new_ratings

# Embora essa solução seja perfeita, é muito mais comum ver Pythonistas escrevendo compreensões de lista:

ratings = [6, 8, 5, 9, 10]
new_ratings = [10 * rating for rating in ratings]
new_ratings

# Exercício 15: Percorra a lista do exercício 14 e imprima "Múltiplo de 3" se o elemento for divisível por 3.

ratings = [6, 8, 5, 9, 10]

for rating in ratings:
    # o sinal % representa a operação "resto".
    if (rating % 3) == 0:  # se o resto é zero, é divisível
        print(f"{rating} é múltiplo de 3")

# Exercícios
# Exercício 1: Crie uma função que receba dois números e retorne o maior deles.


def bigger(number, other):
    if other > number:
        return other
    return number


# Exercício 2: Calcule a média aritmética dos valores contidos em uma lista.


def mean(numbers):
    total = 0
    for number in numbers:
        total += number
    return total / len(numbers)


# Exercício 3: Faça um programa que, dado um valor n qualquer, tal que n > 1 , imprima na tela um quadrado feito de asteriscos de lado de tamanho n . Por exemplo:

n = 5

# *****
# *****
# *****
# *****
# *****
# 🦜 Dica: Python sabe multiplicar sequências! Por exemplo, 3 * 'bla' resulta em blablabla . Isso se aplica a listas também, caso você precise.


def draw_square(n):
    for row in range(n):
        print(n * "*")


# Exercício 4: Crie uma função que receba uma lista de nomes e retorne o nome com a maior quantidade de caracteres. Por exemplo, para ["José", "Lucas", "Nádia", "Fernanda", "Cairo", "Joana"] , o retorno deve ser "Fernanda" .
# 🦜 Uma dica: Utilize a função len() para verificar o tamanho do nome.


def find_biggest_name(names):
    biggest_name = names[0]
    for name in names:
        if len(name) > len(biggest_name):
            biggest_name = name
    return biggest_name


# Exercício 5: Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Crie uma função que retorne dois valores em uma tupla contendo a quantidade de latas de tinta a serem compradas e o preço total a partir do tamanho de uma parede (em m²).


def paint_costs(area):
    can_price = 80
    required_liters = area / 3
    required_cans = required_liters // 18
    if required_liters % 18:
        required_cans += 1
    return required_cans, required_cans * can_price


# Uma alternativa mais direta, utilizando o módulo math

import math


def paint_costs(area):
    can_price = 80
    required_liters = area / 3
    required_cans = math.ceil(required_liters / 18)
    return required_cans, required_cans * can_price


# Exercício 6: Crie uma função que receba os três lados de um triângulo e informe qual o tipo de triâgulo formado ou "não é triangulo" , caso não seja possível formar um triângulo.
# 🦜 Dica:

#   Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
#   Triângulo Equilátero: três lados iguais;
#   Triângulo Isósceles: quaisquer dois lados iguais;
#   Triângulo Escaleno: três lados diferentes.


def type_of_triangle(side1, side2, side3):
    is_triangle = (
        side1 + side2 > side3
        and side2 + side3 > side1
        and side1 + side3 > side2
    )
    if not is_triangle:
        return "não é triângulo"
    elif side1 == side2 == side3:
        return "equilátero"
    elif side1 == side2 or side2 == side3 or side1 == side3:
        return "isósceles"
    else:
        return "escaleno"


# Bônus
# Exercício 1: Dada uma lista, descubra o menor elemento. Por exemplo, [5, 9, 3, 19, 70, 8, 100, 2, 35, 27] deve retornar 2 .


def minimum(numbers):
    smaller = number[0]
    for number in numbers:
        if number < smaller:
            smaller = number
    return smaller


# 🦜 Dica: a função min já existe nativamente no Python! Trabalhando em Python, sempre compensa pesquisar uma solução primeiro porque este brinquedo vem com todos os acessórios inclusos!


def minimum2(numbers):
    return min(numbers)


# ou mesmo
minimum = min

# Exercício 2: Faça um programa que, dado um valor n qualquer, tal que n > 1 , imprima na tela um triângulo retângulo com n asteriscos de base. Por exemplo, para n = 5 o triângulo terá 5 asteriscos na base:

n = 5

# *
# **
# ***
# ****
# *****


def draw_triangle(n):
    for row in range(1, n + 1):
        print(row * "*")


# Exercício 3: Crie uma função que receba um número inteiro N e retorne o somatório de todos os números de 1 até N . Por exemplo, para N = 5 , o valor esperado será 15 .


def summation(limit):
    total = 0
    for number in range(1, limit + 1):
        total += number
    return total


# 🦜 Dica: a função sum já existe nativamente no Python!


def summation2(limit):
    return sum(range(1, limit + 1))


# Exercício 4: Um posto está vendendo combustíveis com a seguinte tabela de descontos:

#   Álcool:
#     - Até 20 litros, desconto de 3% por litro;
#     - Acima de 20 litros, desconto de 5% por litro.
#   Gasolina:
#     - Até 20 litros, desconto de 4% por litro;
#     - Acima de 20 litros, desconto de 6% por litro.
# Escreva uma função que receba o número de litros vendidos, o tipo de combustível (codificado da seguinte forma: A - álcool, G - gasolina), e retorne o valor a ser pago pelo cliente, sabendo-se que o preço do litro da gasolina é R$ 2,50, e o preço do litro do álcool é R$ 1,90.


def fuel_price(type, liters):
    if type == "A":
        price = 1.90
        discount = 0.03
        if liters > 20:
            discount = 0.05
    elif type == "G":
        price = 2.50
        discount = 0.04
        if liters > 20:
            discount = 0.06
    total = price * liters
    total -= total * discount
    return total
