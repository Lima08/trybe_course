# import requests


# # Requisição do tipo GET
# response = requests.get("https://www.betrybe.com/")
# print(response.status_code)  # código de status
# print(response.headers["Content-Type"])  # conteúdo no formato html

# # Conteúdo recebido da requisição
# print(response.text)

# # Bytes recebidos como resposta
# print(response.content)

# Requisição do tipo post
# response = requests.post("http://httpbin.org/post", data="some content")
# print(response.text)

# # Requisição enviando cabeçalho (header)
# response = requests.get(
#   "http://httpbin.org/get",headers={"Accept": "application/json"}
# )
# print(response.text)

# # Requisição a recurso binário
# response = requests.get("http://httpbin.org/image/png")
# print(response.content)

# # Recurso JSON
# response = requests.get("http://httpbin.org/get")
# # Equivalente ao json.loads(response.content)
# print(response.json())

# lança uma exceção caso o status não seja OK
# response = requests.get("http://httpbin.org/status/404")
# response.raise_for_status()


# -------------------------------------------------
# rate limit
# import requests


# # À partir da décima requisição somos bloqueados de acessar o recurso
# # Código de status 429: Too Many Requests
# for _ in range(15):
#     response = requests.get("https://www.cloudflare.com/rate-limit-test/")
#     print(response.status_code)
# -------------------------------------------------

# import requests
# import time


# Coloca uma pausa de 6 segundos a cada requisição
# Obs: este site de exemplo tem um rate limit de 10 requisições por minuto
# for _ in range(15):
#     response = requests.get("https://www.cloudflare.com/rate-limit-test/")
#     print(response)
#     time.sleep(6)


# import requests
# from parsel import Selector
# import time

#  Ex 1:
# for _ in range(1):
#     resp = requests.get("https://www.cloudflare.com/rate-limit-test/")
#     print(resp.status_code)
#     time.sleep(6)

#  Ex 2:
# Lindando com erros em requisições utilizando um url que demora 10 sec para
# responder e configurando para dar timeout em 2 sec.
# try:
#     response = requests.get("http://httpbin.org/delay/10", timeout=2)
# except requests.Timeout:
#     response = requests.get("http://httpbin.org/delay/1", timeout=2)
# finally:
#     print(response.status_code)

#  Ex 3:
# response = requests.get("http://books.toscrape.com/")
# print(response.text)
# selector = Selector(text=response.text)
# print(selector.css("img.thumbnail").getall()[0])
# print(selector)


# Pegando todas as imagens da pagina:

# for thumbnail in selector.css("img.thumbnail").getall():
#     print(thumbnail)

#  Ex 4:
# import requests
# from parsel import Selector


# base_url = "http://books.toscrape.com/"


# response = requests.get(base_url)
# # print(response)  # status 200
# selector = Selector(text=response.text)
# # print(selector) # o O text de dota pagina hmtl
# thumbnail_url_selector = 'div.image_container a::attr(href)'


# for url in selector.css(thumbnail_url_selector).getall():
#     thumbnail_request = requests.get(base_url + url)
#     thumbnail_selector = Selector(text=thumbnail_request.text)
#     book_title = thumbnail_selector.css("div.product_main h1")
#     print(book_title.get())


# Ex 5
# import requests
# from parsel import Selector


# response = requests.get("http://books.toscrape.com/").text
# selector = Selector(text=response)

# O título está no atributo title em um elemento âncora (<a>)
# Dentro de um h3 em elementos que possuem classe product_pod
# titles = selector.css(".product_pod h3 a::attr(title)").getall()
# Estamos utilizando a::attr(title) para capturar somente o
# valor contido no texto do seletor

# Os preços estão no texto de uma classe price_color
# Que se encontra dentro da classe .product_price
# prices = selector.css(".product_price .price_color::text").getall()

# Combinando tudo podemos buscar os produtos
# em em seguida buscar os valores individualmente
# for product in selector.css(".product_pod"):
#     title = product.css("h3 a::attr(title)").get()
#     price = product.css(".price_color::text").get()
#     print(title, price)


# Recurso JSON
# response = requests.get("http://httpbin.org/get")
# Equivalente ao json.loads(response.content)
# print(response.json())
