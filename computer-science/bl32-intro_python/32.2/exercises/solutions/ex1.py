# Agora a prática
# Exercício 1:
# Faça um programa que receba um nome e imprima o mesmo na vertical
#  em escada invertida.
# Exemplo:

# Entrada:
# PEDRO

# Saída:
# PEDRO
# PEDR
# PED
# PE
# P


def vertical_print_name():
    name = input("Digite seu nome: ")
    for remove_letter in range(len(name)):
        for letter in range(len(name) - remove_letter):
            print(name[letter], end="")
        print()


if __name__ == "__main__":
    vertical_print_name()
