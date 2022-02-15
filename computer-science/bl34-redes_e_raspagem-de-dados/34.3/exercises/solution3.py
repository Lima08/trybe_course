#  Exercício 3 Às vezes, você precisa fazer com que o seu raspador da Web
# pareça estar fazendo solicitações HTTP como o navegador,
# para que o servidor retorne os mesmos dados que você vê no seu navegador.
# Faça requisição a https://scrapethissite.com/pages/advanced/?gotcha=headers
# e verifique se foi bem sucedido.
# Para verificar se foi bem sucedido, faça assert "bot detected"
# not in response.text , se nada acontecer, seu código está funcionando.
# Faça a inspeção de como a requisição é feita pelo navegador para
# conseguir replicar através do código.

# import requests


# response = requests.get(
#    "https://scrapethissite.com/pages/advanced/?gotcha=headers"
# )
# print(response.text)
# assert "bot detected" not in response.text

import requests


response = requests.get(
    "https://scrapethissite.com/pages/advanced/?gotcha=headers",
    headers={"User-agent": "Chrome", "Accept": "text/html"},
)
assert "bot detected" not in response.text
print('deu bom')
print(response.text)
print(response.headers)
