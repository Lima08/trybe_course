# Exercício 4 Baseados em uma página contendo detalhes sobre um livro
# http://books.toscrape.com/catalogue/the-grand-design_405/index.html,
# faça a extração dos campos título, preço, descrição e url contendo
#  a imagem de capa do livro.
# O preço deve vir somente valores numéricos e ponto. Ex: Â£13.76 -> 13.76 .
# A descrição de ter o sufixo "more..." removido quando existir.
# Os campos extraídos devem ser apresentados separados por vírgula.
# Ex: título,preço,descrição,capa.

import requests
from parsel import Selector


URL_BASE = "http://books.toscrape.com/catalogue/"

response = requests.get(
    URL_BASE + "the-grand-design_405/index.html",
    headers={"User-agent": "Chrome", "Accept": "text/html"},
)

selector = Selector(response.text)
title = selector.css(".product_main h1::text").get()
price = selector.css(".product_main .price_color::text").re_first(
    r"\d*\.\d{2}"
)
description = selector.css("#product_description ~ p::text").get()
img_url = selector.css("img").attrib["src"]

suffix = "...more"
if description.endswith(suffix):
    description = description[: -len(suffix)]

print(f"{title},{price},{description},{URL_BASE + img_url}")
#  ou..
#  print(title, price, description, URL_BASE + img_ur, sep=",")
