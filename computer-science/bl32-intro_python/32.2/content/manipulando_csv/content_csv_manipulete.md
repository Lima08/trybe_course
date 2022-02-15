Manipulando arquivos CSV
O formato CSV ( Comma Separated Values ) é muito comum em exportações de planilhas de dados e base de dados. Foi utilizado por muito tempo antes de sua definição formal e isso acabou gerando uma não padronização neste formato e o surgimento de vários dialetos.
Cada dialeto tem seus próprios delimitadores e caracteres de citação, porém o formato geral é semelhante o suficiente para utilizarmos o mesmo módulo para este processamento.
Ainda que seu nome indique que o delimitador seja a " , " (vírgula), existem variações que utilizam " ; " (ponto e vírgula) ou até mesmo tabulações (" \t ").
🎲 Sem dúvidas, análise de dados é o que se destaca quando estamos falando sobre manipular arquivos CSV .
Vamos analisar então uma base de dados a respeito da balneabilidade da costa baiana. O arquivo que utilizaremos será o balneabilidade.csv .
💡 Para fazer o exemplo, cole o arquivo balneabilidade.csv na raiz do diretório em que estará o seu script.
O módulo csv , contêm duas principais funções:
Um leitor ( reader ) que nos ajuda a ler o conteúdo, já fazendo as transformações dos valores para Python;
E um escritor ( writer ) para facilitar a escrita nesse formato.
Copiar
import csv

with open("balneabilidade.csv") as file:
    beach_status_reader = csv.reader(file, delimiter=",", quotechar='"')
    header, *data = beach_status_reader

print(data)
O leitor define como dialeto padrão excel , que significa dizer que o delimitador de campos será a " , " e o caractere de citação será aspas duplas ( " ). Uma forma de modificar estes padrões é definindo-os de forma diferente na criação do leitor.
Um leitor de CSV pode ser percorrido utilizando o laço de repetição for e, a cada iteração, retorna uma nova linha já transformada em uma lista python com seus respectivos valores.
header, *data é um truque para separarmos o cabeçalho do restante dos dados. Quando há uma atribuição múltipla e o valor da direita ( beach_status_reader ) pode ser percorrido, o Python entende que deve atribuir cada um dos valores a uma variável da esquerda (header, *data), seguindo a ordem. Isto é chamado de desempacotamento de valores. Dito isso, vamos ver o exemplo abaixo para entendermos melhor como o desempacotamento de valores funciona:
💡 Execute o código abaixo para que você veja os valores printados e entenda melhor o funcionamento.
Copiar
a, b = "cd"
print(a)  # saída: c
print(b)  # saída: d

head, *tail = [1,2,3] # Quando um * está presente no desempacotamento, os valores são desempacotados em formato de lista.
print(head)  # saída: 1
print(tail)  # saída: [2, 3]
Podemos fazer uma análise agrupando a balneabilidade por campanha e depois salvamos o resultado também no formato csv:
Copiar
import csv

# lê os dados
with open("balneabilidade.csv") as file:
    beach_status_reader = csv.reader(file, delimiter=",", quotechar='"')
    header, *data = beach_status_reader

# agrupa campanhas e suas respectivas balneabilidades
bathing_by_campaign = {}
for row in data:
    campaign = row[6]
    bathing = row[2]
    if campaign not in bathing_by_campaign:
        bathing_by_campaign[campaign] = {
            "Própria": 0,
            "Imprópria": 0,
            "Muito Boa": 0,
            "Indisponível": 0,
            "Satisfatória": 0,
        }
    bathing_by_campaign[campaign][bathing] += 1

# escreve o relatório em csv
# abre um arquivo para escrita
with open("report_por_campanha.csv", "w") as file:
    writer = csv.writer(file)

    # escreve o cabeçalho
    headers = [
        "Campanha",
        "Própria",
        "Imprópria",
        "Muito Boa",
        "Indisponível",
        "Satisfatória",
    ]
    writer.writerow(headers)

    # escreve as linhas de dados
    for campaign, bathing in bathing_by_campaign.items():
        # desempacota os valores de balneabilidade para formar uma linha
        # equivalente a
        # row = [campaign]
        # for value in bathing.values():
        #     row.append(value)
        row = [campaign, *bathing.values()]
        writer.writerow(row)
Existe ainda o leitor e escritor baseado em dicionários. Sua principal vantagem é que, com ele, não precisamos manipular os índices para acessar os dados das colunas. Mas, devido a estrutura de dados utilizada, ele tem como desvantagem o espaço ocupado em memória, sendo maior que o comum:
Copiar
import csv

# lê os dados
with open("balneabilidade.csv") as file:
    beach_status_reader = csv.DictReader(file, delimiter=",", quotechar='"')
    # a linha de cabeçaçhos é utilizada como chave do dicionário
    # agrupa campanhas e suas respectivas balneabilidades
    bathing_by_campaign = {}
    for row in beach_status_reader:
        campaign = row["numero_boletim"]  # as linhas são dicionários
        bathing = row["categoria"]
        if campaign not in bathing_by_campaign:
            bathing_by_campaign[campaign] = {
                "Própria": 0,
                "Imprópria": 0,
                "Muito Boa": 0,
                "Indisponível": 0,
                "Satisfatória": 0,
            }
        bathing_by_campaign[campaign][bathing] += 1

# abre um arquivo para escrita
with open("report_por_campanha_dicionarios.csv", "w") as file:
    # os valores a serem escritos devem ser dicionários
    header = [
        "Campanha",
        "Própria",
        "Imprópria",
        "Muito Boa",
        "Indisponível",
        "Satisfatória",
    ]
    # É necessário passar o arquivo e o cabeçalho
    writer = csv.DictWriter(file, fieldnames=header)
    # escreve as linhas de dados
    for campaign, bathing in bathing_by_campaign.items():
        # desempacota os valores de balneabilidade para formar uma linha
        # equivalente a
        # row = {"campanha": campaign}
        # for name, value in bathing.items():
        #     row[name] = value
        row = {"Campanha": campaign, **bathing}
        writer.writerow(row)