Agora a prática
Vamos colocar tudo o que vimos até agora em prática.
Exercício 1 Faça uma requisição ao site https://httpbin.org/encoding/utf8 e exiba seu conteúdo de forma legível.
Exercício 2 Faça uma requisição ao recurso usuários da API do Github ( https://api.github.com/users ), exibindo o username e url de todos os usuários retornados.
Copiar
mojombo https://api.github.com/users/mojombo
defunkt https://api.github.com/users/defunkt
pjhyett https://api.github.com/users/pjhyett
wycats https://api.github.com/users/wycats
...
Exercício 3 Às vezes, você precisa fazer com que o seu raspador da Web pareça estar fazendo solicitações HTTP como o navegador, para que o servidor retorne os mesmos dados que você vê no seu navegador. Faça uma requisição a https://scrapethissite.com/pages/advanced/?gotcha=headers e verifique se foi bem sucedido.
Para verificar se foi bem sucedido, faça assert "bot detected" not in response.text , se nada acontecer, seu código está funcionando.
🦜 Faça a inspeção de como a requisição é feita pelo navegador para conseguir replicar através do código.
Exercício 4 Baseados em uma página contendo detalhes sobre um livro http://books.toscrape.com/catalogue/the-grand-design_405/index.html , faça a extração dos campos título, preço, descrição e url contendo a imagem de capa do livro.
O preço deve vir somente valores numéricos e ponto. Ex: Â£13.76 -> 13.76 .
A descrição de ter o sufixo "more..." removido quando existir.
Os campos extraídos devem ser apresentados separados por vírgula. Ex: título,preço,descrição,capa.
Exemplo:
Copiar
The Grand Design,13.76,THE FIRST MAJOR WORK IN NEARLY A DECADE BY ONE OF THE WORLDâS GREAT THINKERSâA MARVELOUSLY CONCISE BOOK WITH NEW ANSWERS TO THE ULTIMATE QUESTIONS OF LIFEWhen and howdid the universe begin? Why are we here? Why is there something rather than nothing? What is the nature of reality? Why are the laws of nature so finely tuned as to allow for the existenceof beings like ours THE FIRST MAJOR WORK IN NEARLY A DECADE BY ONE OF THE WORLDâS GREAT THINKERSâA MARVELOUSLY CONCISE BOOK WITH NEW ANSWERS TO THE ULTIMATE QUESTIONS OF LIFEÂ When and howdid the universe begin? Why are we here? Why is there something rather than nothing? What is the nature of reality? Why are the laws of nature so finely tuned as to allow for the existenceof beings like ourselves? And, finally, is the apparent âgrand designâor does science offer another explanation? The most fundamental questions about the origins of the universe and of lifeitself, once the province of philosophy, now occupy the territory where scientists, philosophers, and theologians meetâif only to disagree. In their new book, Stephen Hawking and LeonardMlodinow present the most recent scientific thinking about the mysteries of the universe, in nontechnical language marked by both brilliance and simplicity. In The Grand Design they explainthat according to quantum theory, the cosmos does not have just a single existence or history, but rather that every possible history of the universe exists simultaneously. When applied tothe universe as a whole, this idea calls into question the very notion of cause and effect. But the âtop-downâmultiverseâthe idea that ours is just one of many universes that appearedspontaneously out of nothing, each with different laws of nature.Along the way Hawking and Mlodinow question the conventional concept of reality, posing a âmodel-dependentâtheory ofeverything.âand provokeâlike no other. ,http://books.toscrape.com/catalogue/../../media/cache/9b/69/9b696c2064d6ee387774b6121bb4be91.jpg
Exercício 5 Modifique o exercício anterior para retornar também quantos livros estão disponíveis apresentando como último campo no retorno.
Exemplo:
Copiar
The Grand Design,13.76,THE FIRST MAJOR WORK IN NEARLY A DECADE BY ONE OF THE WORLDâS GREAT THINKERSâA MARVELOUSLY CONCISE BOOK WITH NEW ANSWERS TO THE ULTIMATE QUESTIONS OF LIFEWhen and howdid the universe begin? Why are we here? Why is there something rather than nothing? What is the nature of reality? Why are the laws of nature so finely tuned as to allow for the existenceof beings like ours THE FIRST MAJOR WORK IN NEARLY A DECADE BY ONE OF THE WORLDâS GREAT THINKERSâA MARVELOUSLY CONCISE BOOK WITH NEW ANSWERS TO THE ULTIMATE QUESTIONS OF LIFEÂ When and howdid the universe begin? Why are we here? Why is there something rather than nothing? What is the nature of reality? Why are the laws of nature so finely tuned as to allow for the existenceof beings like ourselves? And, finally, is the apparent âgrand designâor does science offer another explanation? The most fundamental questions about the origins of the universe and of lifeitself, once the province of philosophy, now occupy the territory where scientists, philosophers, and theologians meetâif only to disagree. In their new book, Stephen Hawking and LeonardMlodinow present the most recent scientific thinking about the mysteries of the universe, in nontechnical language marked by both brilliance and simplicity. In The Grand Design they explainthat according to quantum theory, the cosmos does not have just a single existence or history, but rather that every possible history of the universe exists simultaneously. When applied tothe universe as a whole, this idea calls into question the very notion of cause and effect. But the âtop-downâmultiverseâthe idea that ours is just one of many universes that appearedspontaneously out of nothing, each with different laws of nature.Along the way Hawking and Mlodinow question the conventional concept of reality, posing a âmodel-dependentâtheory ofeverything.âand provokeâlike no other. ,http://books.toscrape.com/catalogue/../../media/cache/9b/69/9b696c2064d6ee387774b6121bb4be91.jpg,5
❗ Importe o arquivo books.json no MongoDB antes de responder as próximas questões.
🦜 mongoimport --db library books.json
Exercício 6 Escreva um programa que se conecte ao banco de dados library e liste os livros da coleção books para uma determinada categoria recebida por uma pessoa usuária. Somente o título dos livros deve ser exibido.
Exercício 7 Faça o calculo de quantos livros publicados ( STATUS = PUBLISH ) temos em nosso banco de dados por categoria. Ordenando-os de forma decrescente de acordo com a quantidade.
🦜 Você pode utilizar agreggation framework para auxiliar neste exercício.
Saída:
Copiar
Java 95
Internet 41
Microsoft .NET 33
Web Development 16
Software Engineering 15
Business 12
Programming 12
Client-Server 11
Microsoft 8
Theory 7
...
