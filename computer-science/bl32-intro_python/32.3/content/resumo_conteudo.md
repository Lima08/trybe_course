Em nosso curso utilizaremos a biblioteca pytest , um framework que facilita a escrita de testes simples, mas capazes de testar funcionalidades complexas em aplicações e bibliotecas.
Lembre-se de instalar a biblioteca somente no ambiente virtual do seu projeto.
A instalação é feita através do pip utilizando o comando:

python3 -m pip install pytest
E podemos verificar utilizando o comando:

python3 -m pytest --version
A saída esperada é similar à apresentada abaixo.

This is pytest version 5.3.0, imported from /home/cassiobotaro/projects/gerenciador-tarefas/.venv/lib/python3.8/site-packages/pytest.py
📝 Que tal vermos um exemplo?
codigo.py

def is_odd(number):
    'Retorna True se um número é ímpar, senão False.'
    return number % 2 != 0
test_codigo.py

from codigo import is_odd


def test_is_odd_when_number_is_odd_returns_true():
    'Para um número ímpar a função deve retornar o valor True'
    assert is_odd(3) is True


def test_is_odd_when_number_is_even_returns_false():
    'Para um número par a função deve retornar o valor False'
    assert is_odd(2) is False
Notem que o nome do arquivo de testes possui o prefixo test_ , assim como a definição das funções de teste. Isto é necessário para que seus testes sejam descobertos pela ferramenta.
Uma função de teste é similar a qualquer outra, porém tem o propósito de verificar se o resultado obtido foi o mesmo do esperado. No código isto pode ser visto através da utilização da palavra reservada assert .
O comando assert funciona da seguinte maneira: caso a expressão recebida seja verdadeira (avaliada como True ), nada acontece, porém caso seja falsa (avaliada como False ), uma exceção do tipo AssertionError é lançada. A pytest captura este erro e tenta apresentar uma comparação entre o esperado e o recebido da melhor maneira possível.
Vamos rodar nossos testes e ver o resultado? Vamos utilizar o comando:

python3 -m pytest

Testando falhas
Erros acontecem e nem sempre são inesperados. O Python utiliza de exceções para sinalizar que ocorreram erros durante a execução de um código e que nem sempre são fatais.
Podemos escrever testes que verificam que um erro deve ocorrer a partir de uma determinada entrada.
📝 Um exemplo pode ser visto abaixo:
codigo.py

# ...

def divide(a_number, other_number):
    "Retorna a divisão de a_number por other_number"
    return a_number / other_number
test_codigo.py

import pytest
from codigo import is_odd, divide

# ...

def test_divide_when_other_number_is_zero_raises_an_exception():
    with pytest.raises(ZeroDivisionError, match="division by zero"):
        divide(2, 0)
Utilizamos a função raises da pytest , que verifica se a exceção ocorreu. Caso contrário, ela lança um AssertionError , indicando que o teste não passou. Podemos verificar também se o texto retornado na exceção é o esperado, através do parâmetro match , que pode receber uma expressão regular. No exemplo, temos uma divisão por zero, que lança a exceção esperada, e o teste passa com sucesso.


Um pouco de contexto
Quando escrevemos testes, pensamos em cenários distintos que podem ocorrer ao nosso sistema: "dado um arquivo com as seguintes linhas", "visto que temos um banco de dados com um dado registro" ou "a partir de um cliente web". Às precondições ou estados necessários para a execução de um teste, damos o nome de test fixture ou apenas fixture .
Cada teste pode ter seu próprio cenário (contexto) ou compartilhá-lo com outros testes.
test_codigo.py

# get_most_ordered_dish_per_costumer é uma função que retorna o prato mais pedido por uma
# determinada pessoa cliente, considerando que os pedidos estão em uma lista.

# get_order_frequency_per_costumer é uma função que retorna a frequência que uma determinada
# pessoa cliente pede um determinado prato , considerando que os pedidos estão em uma lista.


# uma fixture utilizando a biblioteca pytest
# é definida utilizando a sintaxe abaixo
@pytest.fixture
def orders():
    """Nosso cenário (contexto) temos os seguintes pedidos"""
    return [
        {"customer": "maria", "order": "pizza", "day": "terça-feira"},
        {"customer": "joao", "order": "hamburger", "day": "terça-feira"},
        {"customer": "maria", "order": "pizza", "day": "quarta-feira"},
        {"customer": "maria", "order": "hamburger", "day": "quinta-feira"},
    ]

# estamos adicionando a fixture orders ao teste
# ou seja temos um contexto onde os pedidos são os definidos anteriormente
def test_get_most_ordered_dish_per_costumer_when_customer_is_maria(orders):
    assert get_most_ordered_dish_per_costumer(orders, "maria") == "pizza"

# novamente adicionamos um cenário (contexto) ao teste onde os pedidos realizados são os
# definidos na fixture
def test_get_order_frequency_per_costumer_when_customer_is_joao_and_order_is_pizza(orders):
    assert get_order_frequency_per_costumer(orders, "joao", "pizza") == 0

def test_get_order_frequency_per_costumer_when_customer_is_maria_and_order_is_hamburger(orders):
    assert get_order_frequency_per_costumer(orders, "maria", "hamburger") == 1
É importante ressaltar que este contexto poderia ser a abertura de uma conexão com o banco de dados, uma referência à conexão a um cliente web, um arquivo temporário ou qualquer outro contexto.


DUBLE

Em testes automatizados (de unidade), é desejado que cada teste não interfira no estado manipulado por outro teste, e também que recursos externos (arquivos, internet, banco de dados) não atrapalhem a sua execução. Por isso, é muito comum a utilização de dublês de testes para simular estes recursos externos.
Estes componentes simulados de software são chamados, de forma genérica, de mock , mas existem diversas técnicas específicas de simulações que nos ajudam a escrever os testes.
Podemos substituir componentes para que retornem um determinado valor simulado ou podemos substituir os componentes por objetos falsos que registram as informações sobre sua invocação como o número de vezes em que foram chamados ou os parâmetros com o qual foram chamados.
Na literatura encontramos as técnicas de dublê com os nomes mocks , fakes , stubs e spy , e de uma forma bem resumida podemos defini-las:
fakes: objetos que possuem implementações funcionais, porém normalmente simplificadas;
mocks: são pré programados para verificarem as chamadas das funções que receberem;
stubs: proveem respostas predefinidas;
spies: são como stubs, mas também armazenam informações de como foram chamados.
Caso queira mais detalhes, dê uma olhada no artigo do Martin Fowler sobre o assunto ou no material complementar sobre dublês de testes que se encontra na seção de recursos adicionais .
Vamos analisar dois cenários e escrever seus respectivos testes utilizando dublês, evitando assim a dependência externa a um arquivo real.
No primeiro cenário nós temos nossa dependência externa (o arquivo) sendo recebido como parâmetro.
pokemon.py
Copiar
import json


def retrieve_pokemons_by_type(type, reader):
    # lê o conteudo de reader e o transforma de json
    # para dicionário
    pokemons = json.load(reader)["results"]
    # filtra somente os pokemons do tipo escolhido
    pokemons_by_type = [
        pokemon for pokemon in pokemons if type in pokemon["type"]
    ]
    return pokemons_by_type
Vamos utilizar uma técnica onde substituiremos a abertura do nosso arquivo real por um objeto que possui as implementações funcionais de um arquivo (método read , necessário na operação de leitura). Este objeto será alocado na memória, "simulando" nosso arquivo real.
test_pokemon.py
Copiar
import json
from pokemon import retrieve_pokemons_by_type
from io import StringIO


def test_retrieve_pokemons_by_type():
    # definimos um pokemon do tipo grama
    grass_type_pokemon = {
        "national_number": "001",
        "evolution": None,
        "name": "Bulbasaur",
        "type": ["Grass", "Poison"],
        "total": 318,
        "hp": 45,
        "attack": 49,
        "defense": 49,
        "sp_atk": 65,
        "sp_def": 65,
        "speed": 45,
    }
    # definimos também um pokemon do tipo água
    water_type_pokemon = {
        "national_number": "007",
        "evolution": None,
        "name": "Squirtle",
        "type": ["Water"],
        "total": 314,
        "hp": 44,
        "attack": 48,
        "defense": 65,
        "sp_atk": 50,
        "sp_def": 64,
        "speed": 43,
    }
    # criamos um arquivo em memória que o seu conteúdo são os dois pokemons
    fake_file = StringIO(
        json.dumps({"results": [grass_type_pokemon, water_type_pokemon]})
    )
    # quando pesquisamos por pokemons do tipo grama,
    # o pokemon do tipo água não deve ser retornado
    assert retrieve_pokemons_by_type("Grass", fake_file) == [
        grass_type_pokemon
    ]
Um segundo cenário é onde a função espera o nome de um arquivo e a abertura do mesmo acontece dentro da função.
pokemon.py
Copiar
import json


def retrieve_pokemons_by_type(type, filepath):
    with open(filepath) as file:
        pokemons = json.load(file)["results"]
        pokemons_by_type = [
            pokemon for pokemon in pokemons if type in pokemon["type"]
        ]
        return pokemons_by_type
Para escrever este teste, vamos aproveitar da natureza dinâmica da linguagem e substituir o método open em tempo de execução por um objeto mock_open , que já vem embutido na linguagem e se comporta como o open , retornando o que foi definido em read_data como seu conteúdo. Um detalhe interessante é que esse objeto obtido através da função mock_open também possui a capacidade de armazenar informações sobre como foram as chamadas de seus métodos e os parâmetros recebidos.
test_pokemon.py
Copiar
import json
from unittest.mock import mock_open, patch
from pokemon import retrieve_pokemons_by_type

def test_retrieve_pokemons_by_type():
    # definimos um pokemon do tipo grama
    grass_type_pokemon = {
        "national_number": "001",
        "evolution": None,
        "name": "Bulbasaur",
        "type": ["Grass", "Poison"],
        "total": 318,
        "hp": 45,
        "attack": 49,
        "defense": 49,
        "sp_atk": 65,
        "sp_def": 65,
        "speed": 45,
    }
    # definimos também um pokemon do tipo água
    water_type_pokemon = {
        "national_number": "007",
        "evolution": None,
        "name": "Squirtle",
        "type": ["Water"],
        "total": 314,
        "hp": 44,
        "attack": 48,
        "defense": 65,
        "sp_atk": 50,
        "sp_def": 64,
        "speed": 43,
    }
    pokemon_json_content = json.dumps({"results": [grass_type_pokemon, water_type_pokemon]})
    # substituímos a função padrão do python open por mock_open
    # uma versão que se comporta de forma parecida, porém simulada
    with patch("builtins.open", mock_open(read_data=pokemon_json_content)):
        # repare que o nome do arquivo não é importante aqui
        # a esses parâmetros não utilizados damos o nome de dummies
        # como neste contexto alteramos o open pelo mock_open,
        # o argumento "dummy" poderia ser substituído por qualquer coisa, já que não será utilizado pela função
        assert retrieve_pokemons_by_type("Grass", "dummy") == [
            grass_type_pokemon
        ]
A primeira abordagem torna o código menos acoplado a um arquivo e nos permite utilizar qualquer objeto (que tenha o método reader) em seu lugar. Assim, essa função pode ser reutilizável, por exemplo, para ler pokemons a partir de uma requisição web ou outra fonte.

