#  Exercício 1 Faça uma requisição ao site https://httpbin.org/encoding/utf8 e exiba seu conteúdo de forma legível.
from parsel import Selector
import requests

print('rasdfasdfasdf')
response = requests.get('https://httpbin.org/encoding/utf8')
selector = Selector(text=response.text)
print(selector)