# Bônus
# Exercício 5:
# Utilizando o arquivo pokemons.json que está em helpers,
#  vamos escrever um programa que sorteie
# um pokemon aleatoriamente. O programa deve
#  perguntar à pessoa usuária "Quem é esse
# pokemon?", até que ela o acerte.
# A cada erro, apresente um número de letras
# do nome daquele pokemon igual ao número de erros.
# Exemplo:
# o pokemon sorteado pelo programa é butterfree,
#  a pessoa usuária chuta charizard , o programa deve exibir b.
#  Em seguida, a pessoa chuta blastoise , o programa deve
# exibir bu e assim por diante até a pessoa acertar.
# Você pode utilizar o método choice do modulo random para sortear
#  aleatoriamente um pokemon.
# Ex: random.choice(pokemon) -> Saída: {"name": "Pikachu", }
import random
import json


def get_pokemon_list():
    with open("../helper/pokemons.json") as data:
        print('oi')
        pokemons = json.load(data)["results"]
        pokemon_list = [pokemon['name'] for pokemon in pokemons]
        return pokemon_list


def select_a_random_pokemon(pokemon_list):
    return random.choice(pokemon_list)


def make_a_guess(pokemon):
    guess = ""
    counter = 0
    while guess != pokemon:
        print('Dica: ', end="")
        for number in range(counter):
            print(pokemon[number], end="")
        print()
        counter += 1

        gamer_try = input("Quem é esse pokemon? ")
        guess = gamer_try
    print()
    print(f"Parabéns! O pokemon é {guess}")


if __name__ == "__main__":
    pokemons_list = get_pokemon_list()
    secret_pokemon = select_a_random_pokemon(pokemons_list)
    print(secret_pokemon)
    make_a_guess(secret_pokemon)
