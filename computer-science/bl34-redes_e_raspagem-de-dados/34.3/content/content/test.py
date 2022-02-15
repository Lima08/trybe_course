# Teste 1 -----------------------
# from parsel import Selector
# import requests

# URL_BASE = "http://books.toscrape.com/catalogue/"

# response = requests.get(URL_BASE + "page-1.html")
# selector = Selector(text=response.text)

# href = selector.css(".product_pod h3 a::attr(href)").get()
# detail_page_url = URL_BASE + href

# # baixa o conteúdo da página de detalhes
# detail_response = requests.get(detail_page_url)
# detail_selector = Selector(text=detail_response.text)

# # recupera a descrição do produto
# # ~ significa a tag irmã
# description = detail_selector.css("#product_description ~ p::text").get()
# print(description)

# Teste 2 -----------------------
# from parsel import Selector
# import requests


# response = requests.get("http://books.toscrape.com/")
# selector = Selector(text=response.text)
# # Extrai todos os preços da primeira página
# prices = selector.css(".product_price .price_color::text").re(r"£\d+\.\d{2}")
# print(prices)

# Teste 3 -----------------------

from parsel import Selector
import requests


response = requests.get(
    "http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"
)
selector = Selector(text=response.text)

# Extrai a descrição
description = selector.css("#product_description ~ p::text").get()
# print(description)

# "Fatiamos" a descrição removendo o sufixo
suffix = "...more"
if description.endswith(suffix):
    description = description[: -len("...more")]
print(description)


# Agora que temos nossos dados, precisamos armazenar esta informação,
# e para isto utilizaremos o MongoDB que, como já estudamos, é
# um banco de dados de documentos, que armazena dados em formato JSON ( BSON ).
#  Precisaremos de uma biblioteca para nos comunicarmos com o sistema
# de gerenciamento do banco de dados, e a mais popular e robusta é a pymongo.
#  Podemos instalá-la com o comando:
# $ python3 -m venv .venv && source .venv/bin/activate
# $ python3 -m pip install pymongo
