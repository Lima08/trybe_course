# Exercício 5 Modifique o exercício anterior para retornar também quantos
#  livros estão disponíveis apresentando como último campo no retorno.

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

stock = selector.css(".product_main .availability::text").re_first("\d")

suffix = "...more"
if description.endswith(suffix):
    description = description[: -len(suffix)]

print(f"{title},{price},{description},{URL_BASE + img_url},{stock}")
