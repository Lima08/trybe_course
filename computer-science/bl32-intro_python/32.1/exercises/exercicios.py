from math import ceil


# Exercício 1: Crie uma função que receba dois números e retorne o maior deles.
def higher_number(num1, num2):
    if num1 > num2:
        return num1
    return num2


# Exercício 2: Calcule a média aritmética dos valores contidos em uma lista.
def average(list):
    total = sum(list)
    average = total / len(list)
    return average


# Exercício 3: Faça um programa que, dado um valor n qualquer, tal que n > 1,
# imprima na tela um quadrado feito de asteriscos de lado de tamanho n .
# Por exemplo:

# n = 5

# *****
# *****
# *****
# *****
# *****
# 🦜 Dica: Python sabe multiplicar sequências!
# Por exemplo, 3 * 'bla' resulta em blablabla . Isso se aplica a listas também,
# caso você precise.
# Sentiu aí um certo dejavu? 😁


def asterisk_function(arg):
    line = "*" * arg
    counter = 0
    while counter < arg:
        print(line)
        counter += 1


#  Trybe solução
def draw_square(n):
    for row in range(n):
        print(n * "*")


# Exercício 4: Crie uma função que receba uma lista de nomes e retorne o nome
# com a maior quantidade de caracteres. Por exemplo, para
# ["José", "Lucas", "Nádia", "Fernanda", "Cairo", "Joana"] ,
# o retorno deve ser "Fernanda" .
# 🦜 Uma dica: Utilize a função len() para verificar o tamanho do nome.


# def max_number(array):
# length_list = [len(name) for name in array]
# print(length_list)
# return max(length_list)


# print(max_number(["José", "Lucas", "Nádia", "Fernanda", "Cairo", "Joana"]))


# Exercício 5:
# Considere que a cobertura da tinta é de 1 litro
# para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros,
# que custam R$ 80,00. Crie uma função que retorne dois valores em uma tupla
# contendo a quantidade de latas de tinta a serem compradas
# e o preço total a partir do tamanho de uma parede(em m²).
# ceil é importado de math
def ink_calculetor(square_meter):
    can_price = 80
    can_yield = 54
    quantity_cans = ceil(square_meter / can_yield)
    return quantity_cans, quantity_cans * can_price


print(ink_calculetor(55))


#  Trybe solução
def paint_costs(area):
    can_price = 80
    required_liters = area / 3
    # se cada litro faz 3 metros divide o a area em
    # 3 para fazer a conta de quantos litros precisa.
    required_cans = required_liters // 18
    if required_liters % 18:  # Se sobra metros adiciona mais uma lata
        required_cans += 1
    return required_cans, required_cans * can_price


print(paint_costs(55))


# Exercício 6:
# Crie uma função que receba os três lado de um triângulo
#  e informe qual o tipo de triângulo formado ou "não é triangulo"
#  , caso não seja possível formar um triângulo.

# 🦜 Dica:
#   Três lados formam um triângulo quando a soma de
# quaisquer dois lados for maior que o terceiro;
#   Triângulo Equilátero: três lados iguais;
#   Triângulo Isósceles: quaisquer dois lados iguais;
#   Triângulo Escaleno: três lados diferentes.


#   Bônus
# Exercício 1: Dada uma lista, descubra o menor elemento.
# Por exemplo, [5, 9, 3, 19, 70, 8, 100, 2, 35, 27] deve retornar 2.
def min_element(array):
    return min(array)


print(min_element([5, 9, 3, 19, 70, 8, 100, 2, 35, 27]))


# ou (solução trybe)
def minimum(array):
    smaller = array[0]
    for number in array:
        if number < smaller:
            smaller = number
    return smaller


print(minimum([5, 9, 3, 19, 70, 8, 100, 2, 35, 27]))


# Exercício 2: Faça um programa que, dado um valor n qualquer,
#  tal que n > 1, imprima na tela um triângulo retângulo com n * de base.
#  Por exemplo, para n = 5 o triângulo terá 5 asteriscos na base:
# n = 5
# *
# **
# ***
# ****
# *****
def asterisk_pyramid(number):
    symbol = "*"
    while len(symbol) <= number:
        print(symbol)
        symbol += "*"


asterisk_pyramid(5)


#  ou Trybe
def draw_triangle(n):
    for row in range(1, n + 1):
        print(row * '*')


# Exercício 3:
# Crie uma função que receba um número inteiro N e retorne
#  o somatório de todos os números de 1 até N .
# Por exemplo, para N = 5 , o valor esperado será 15 .
def sum_all_numbers(number):
    value = 0
    for number in range(1, number + 1):
        value += number

    return value


print(sum_all_numbers(5))

# Exercício 4:
# Um posto está vendendo combustíveis com a seguinte tabela de descontos:
#   Álcool:
#     - Até 20 litros, desconto de 3% por litro;
#     - Acima de 20 litros, desconto de 5% por litro.
#   Gasolina:
#     - Até 20 litros, desconto de 4% por litro;
#     - Acima de 20 litros, desconto de 6% por litro.
# Escreva uma função que receba o número de litros vendidos,
#  o tipo de combustível (
#   codificado da seguinte forma: A - álcool, G - gasolina
# ), e retorne o valor a ser pago pelo cliente,
# sabendo-se que o preço do litro da gasolina é R$ 2,50,
#  e o preço do litro do álcool é R$ 1,90.

# A - (álcool é R$ 1,90), Até 20 l 3% por litro; > 5% por litro;
# G - (gasolina é R$ 2,50)--> Até 20 l 4% por litro; > 6% por litro;


def fuel_calculator(type, liters):
    discount = 0
    price = 0

    if type == 'a':
        discount = 0.03
        price = 1.90
        if liters > 20:
            discount = 0.05
    elif type == 'g':
        discount = 0.04
        price = 2.50
        if liters > 20:
            discount = 0.06
    else:
        return('Tipo de combustivel invalido!')

    total = price * liters
    total -= total * discount
    return total


print(fuel_calculator('a', 10))
print(fuel_calculator('a', 21))
print(fuel_calculator('g', 10))
print(fuel_calculator('g', 21))
print(fuel_calculator('c', 21))
