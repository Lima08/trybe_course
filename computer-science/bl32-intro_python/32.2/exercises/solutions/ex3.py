# Exercício 3:
# Modifique o exercício anterior para que as palavras sejam lidas de um arquivo
# Considere que o arquivo terá cada palavra em uma linha.
# Exercício 2:
# Jogo da palavra embaralhada.
# Desenvolva um jogo em que a pessoa usuária tenha que
#  adivinhar uma palavra que será mostrada com as letras embaralhadas.
# O programa terá uma lista de palavras e escolherá uma aleatoriamente.
# O jogador terá três tentativas para adivinhar a palavra.
# Ao final a palavra deve ser mostrada na tela,
#  informando se a pessoa ganhou ou perdeu o jogo.
# Para embaralhar uma palavra faça:
# scrambled_word = "".join(random.sample(word, len(word)))

# O sorteio de uma palavra aleatória pode ser feito utilizando o método choice:
#  random.choice(["word1", "word2", "word3"]) -> "word2"
import random

MAX_ATTEMPTS = 3


def list_of_words():
    with open('../helper/words_list.txt') as words:
        return words.read().split('\n')


def select_and_shuffle_word(words_list):
    secret_word = random.choice(words_list)
    shuffle_word = ''.join(random.sample(secret_word, len(secret_word)))
    return secret_word, shuffle_word


def attempts_maker():
    choices_list = []
    for attempt in range(MAX_ATTEMPTS):
        choice = input(f'Palpite numero {attempt + 1}: ')
        choices_list.append(choice)
    return choices_list


def check_result(attempts, secret):
    if secret in attempts:
        print(f'Parabéns, você acertou! A palavra é {secret}.')
    else:
        print(f'Não foi dessa vez. A palavra é {secret}.')


if __name__ == '__main__':
    words = list_of_words()
    secret, shuffle_word = select_and_shuffle_word(words)
    print(f'De seu palpite para a palavra {shuffle_word}.')
    choices_list = attempts_maker()
    check_result(choices_list, secret)
