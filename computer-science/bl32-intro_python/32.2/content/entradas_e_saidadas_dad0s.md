
Comandos:
>> input("Digite uma mensagem:")
>> print("O resultado é", 42)  # saída: O resultado é 42
>> print("Os resultado são", 6, 23, 42)  # saída: Os resultados são 6 23 42
>> print("Em duas ")
>> print("linhas.")
>> print("Na mesma", end="")  # Faz o fim do output ser "".
>> print("linha.")

 Em Python , podemos fazer interpolação de variáveis e expressões utilizando f-string . Adicionamos um f antes das aspas e o valor de saída entre chaves. Essa dica é importante, pois é a maneira mais eficiente de formatar strings.
 
 import sys

err = "Arquivo não encontrado"
print(f"Erro aconteceu: {err}", file=sys.stderr)

ex:
import random

random_number = random.randint(1, 10)  # escolhe um número aleatório entre 1 e 10
guess = ""

while guess != random_number:  # enquanto não adivinhar o número
    guess = int(input("Qual o seu palpite? "))  # pergunte a pessoa usuária um número

print("O número sorteado era: ", guess)


Ambiente Virtual
Imagine que, em uma máquina, há um projeto Python que tem alguns pacotes de terceiros instalados e, dentre eles, há uma biblioteca na versão 1.4. Imagine também que, na mesma máquina, um novo projeto é iniciado e ele precisa da mesma biblioteca, mas, dessa vez, na versão 2.0. O que fazer? As versões são compatíveis? Se eu atualizar o sistema, a versão antiga vai continuar a funcionar?
O venv entra como resposta à essas perguntas! Ele é um módulo, já embutido na linguagem, que serve para isolar ambientes entre projetos. Ou seja, eu consigo ter dois projetos rodando, em dois ambientes diferentes, com versões diferentes de uma mesma biblioteca.
Na prática, o que vamos fazer é instalar as bibliotecas em um diretório, que está relacionado ao projeto. Assim, cada projeto pode ter suas próprias bibliotecas na versão que quiser. A ideia é a mesma do npm que vocês já vêm usando.
O comando para criação deste ambiente isolado é python3 -m venv .venv , sendo que .venv é o nome do ambiente isolado. Este comando deve ser executado na raiz do projeto.
💡 Caso o venv não esteja instalado, utilize o comando sudo apt install python3-venv .
Este ambiente isolado será visto como um diretório criado na raiz do projeto. O ponto na frente do nome faz com que o diretório fique oculto.
Depois de criado, temos de ativar este ambiente para usá-lo. Isto é importante, pois sempre que decidirmos trabalhar neste projeto devemos repetir este passo.
Comando para ativação:

 source .venv/bin/activate


 Você pode conferir se o comando de ativação do ambiente virtual deu certo com o seguinte comando:

$ which python3
O resultado será o caminho para a pasta onde você criou seu ambiente virtual ( pwd ), acrescido de .venv/bin/python3 .
Pronto, agora estamos preparados e preparadas para instalar as bibliotecas que precisaremos para nossos projetos.

EScrevendo em arquivos
comando:
>> aquivo = open('nome do arquivo', mode='w')
>> aquivo.write('textoo que quero escrever')
>> aquivo.writelines(['escrever, 'uma, 'lista, 'de, 'coisas'])
>> aquivo.close()

Tratamento de exceções
Para tratarmos exceções, utilizamos o conjunto de instruções try , com as palavras reservadas try e except . O funcionamento dessa cláusula ocorre da seguinte forma:
Se nenhuma exceção ocorrer, a cláusula except é ignorada, e a execução da instrução try é finalizada.
Se ocorrer uma exceção durante a execução da cláusula try , as instruções remanescentes na cláusula são ignoradas. Se o tipo da exceção ocorrida tiver sido previsto em algum except , então essa cláusula será executada.
Se não existir nenhum tratador previsto para tal exceção, trata-se de uma exceção não tratada e a execução do programa termina com uma mensagem de erro.
Vamos agora ver um exemplo de tratamento de exceções:

while True:
    try:
        x = int(input("Please enter a number: "))
        break
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")


Lidando com exceções enquanto manipulamos arquivos
Agora cientes de como tratar exceções, podemos nos prevenir de possíveis erros que ocorrem quando manipulamos arquivos. Sempre devemos fechar um arquivo e podemos, em um bloco try , fazer isso utilizando a instrução finally ou else . O finally é uma outra cláusula do conjunto try , cuja finalidade é permitir a implementação de ações de limpeza, que sempre devem ser executadas independentemente da ocorrência de ações. Já o else ocorre sempre que todo o try for bem sucedido.

try:
    arquivo = open("arquivo.txt", "r")
except OSError:
    # será executado caso haja uma exceção
    print("arquivo inexistente")
else:
    # será executado se tudo ocorrer bem no try
    print("arquivo manipulado e fechado com sucesso")
    arquivo.close()
finally:
    # será sempre executado, independentemente de erro
    print("Tentativa de abrir arquivo")

    O with é a palavra reservada para gerenciamento de contexto. Este gerenciamento ( with ) é utilizado para encapsular a utilização de um recurso, garantindo que certas ações sejam tomadas independentemente se ocorreu ou não um erro naquele contexto.
A função open retorna um objeto que se comporta como um gerenciador de contexto de arquivo que será responsável por abrir e fechar o mesmo. Isto significa que o arquivo possui mecanismos especiais que, quando invocados, utilizando with , alocam um determinado recurso, no caso um arquivo, e, quando o bloco for terminado, este recurso será liberado.
Copiar
# Criamos um contexto, limitando o escopo onde o arquivo está aberto.
# O uso do "as" aqui é somente para atribuir o valor utilizado no contexto à variável file
with open("arquivo.txt", "w") as file:
    file.write("Michelle 27\n")
# como estamos fora do contexto, o arquivo foi fechado
print(file.closed)


Manipulando arquivos JSON
Seus principais métodos para manipulação são: load , loads , dump , dumps .

