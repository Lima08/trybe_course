Exercícios
Agora vamos colocar em prática todo o conteúdo que vimos. Para isso faremos alguns exercícios práticos utilizando nossos conhecimentos sobre firewall.

Exercício 1 : Defina uma regra de firewall utilizando o comando iptables -A , que bloqueie ( block ou REJECT/DROP ) toda a entrada ( in ou INPUT ) de pacotes utilizando o protocolo ICMP , impedindo assim que a máquina responda ao comando ping . Lembre-se, você pode executar o comando ping para validar se sua regra está funcionando corretamente: ping 127.0.0.1 (você pode adicionar o parâmetro -O para exibir os pings rejeitados também 😉).
R:  iptables -A INPUT -p icmp -j REJECT

Exercício 2 : Exclua a regra anterior utilizando o parâmetro -D .
R:  iptables -D INPUT -p icmp -j REJECT

Exercício 3 : Agora vamos criar uma regra para bloquear o tráfego HTTPS. Para isso, iremos bloquear a saída de pacotes ( out ou OUTPUT ). Lembre-se, a porta padrão para esse protocolo é a 443 , para especificá-la utilize o parâmetro --sport (sport significa --> S de source + port ). Ele utiliza também o protocolo tcp . Para testar sua regra, tente acessar um site pelo navegador que use o protocolo, como o Youtube, o Google ou o Facebook.
R:  iptables -A OUTPUT -p tcp --sport 443 -j REJECT

Exercício 4 : Bloqueie agora o tráfego de saída para HTTP. Lembre-se, também é utilizado o protocolo tcp e a porta 80 . Para testar sua regra, tente acessar um site pelo navegador que use HTTP .
R:  iptables -A OUTPUT -p tcp --sport 80 -j REJECT

Exercício 5 : Para finalizar, vamos limpar todas as regras. Para isso, utilize o comando --flush do iptables (Linux).
R:  iptables --flush

Exercício 6 : Agora, vamos utilizar um tipo de proxy bem legal que pode ser bastante útil no nosso dia como pessoas desenvolvedoras: o NGROK (https://ngrok.com/). Com ele conseguimos criar um túnel para o nosso localhost .
  1 - Crie um servidor HTTP em sua máquina executando na porta 80 , pode ser um front-end ou um back-end criado em aulas anteriores.
  2 - Baixe o ngrok e extraia o arquivo baixado em uma pasta de sua preferência, conforme instruções no site oficial (https://ngrok.com/download) .
  3 - Conforme instruções do site, crie um túnel para a porta 80 de sua máquina.
  4 - Acesse o o link disponibilizado em seu navegador. Utilize ele para acessar de outros dispositivos, como seu smartphone ou outro computador 😎.

Exercício 7 : No conteúdo vimos o que são os protocolos SSL e TLS. Vamos subir nosso próprio servidor HTTPS, utilizando nosso próprio certificado!
   1 - Vamos utilizar a ferramenta OpenSSL  (https://www.openssl.org/) para gerar nossos certificados. Ela já vem instalada na maioria das distros Linux. No Docker, no entanto, você vai precisar executar:

$ apt-get update && apt-get install python3 openssl
    2 -Para gerar nosso próprio certificado auto-assinado, utilize os comandos abaixo. Lembrando que, como nós estamos gerando o certificado, ele não será reconhecido por nenhuma entidade certificadora, de modo que ele só nos servirá para utilizar o protocolo TLS com o HTTPS, não sendo capaz de ser aceito pelo navegador.

$ openssl genrsa -out key.pem
$ openssl req -new -key key.pem -out csr.pem
$ openssl x509 -req -days 9999 -in csr.pem -signkey key.pem -out cert.pem
$ rm csr.pem

   3 Acabamos de gerar dois arquivos, o cert.pem (o certificado) e o key.pem (chave privada). Copie os dois arquivos para um diretório onde iremos criar nosso servidor HTTPS.

   4- Agora vamos escrever um servidor https usando os módulos nativos do python ssl (https://docs.python.org/3/library/ssl.html) e http.server (https://docs.python.org/3/library/http.server.html) . Embora esses módulos tenham muitos muitos recursos (muitos mesmo), nós vamos usar apenas alguns. Tente seguir as instruções a seguir:
  4.1 Crie um contexto SSL com a classe SSLContext , usando o protocolo de versão mais alta disponível para servidores. (dica: as opções estão listadas na documentação). 4.2 Carregue no contexto SSL a cadeia de certificação, passando tanto a o arquivo de certificação quanto a sua chave. (dica: existe um método para isso). 4.3 Crie uma instância de HTTPServer . O endereço deve ser uma tupla ('localhost', 8000) e para responder as requisições, use SimpleHTTPRequestHandler . (dica: apesar do exemplo na documentação, não use with .) 4.4 Crie um socket server-side usando o método wrap_socket do seu contexto SSL. Passe como parâmetro o socket do servidor ( server.socket ). 4.5 Substitua o socket do servidor pelo socket que vc acabou de criar. 4.6 Execute o servidor com o método serve_forever .

   5 - Acesse o servidor no endereço https://localhost:8000/ utilizando o Firefox (precisa ser o Firefox!). Perceba que ele irá informar que o certificado não é reconhecido por ele, pois não foi assinado por nenhuma autoridade da confiança dele.
  5.1 Chrome e Safari se recusam a acessar um site cujo certificado não está assinado por NENHUMA autoridade certificadora (existem instruções para agir como uma autoridade certificadora mas não precisa seguir por esse caminho - https://stackoverflow.com/questions/7580508/getting-chrome-to-accept-self-signed-localhost-certificate/60516812#60516812) .
Acesse o servidor novamente, porém, desta vez utilizando cURL (de fora do Docker, se vc estiver usando).
Por último, vamos utilizar um recurso do cURL, somente para testes (somente utilize, caso realmente você esteja esperando por aquilo), que é o parâmetro -k ou --insecure . Com ele, falamos para o nosso cURL prosseguir a request mesmo sabendo que a conexão não é "confiável".


BONUS
Exercício 8 : Crie uma conta no Ngrok e explore o dashboard disponibilizado por ele para monitorar seus túneis. Aproveite e explore outros recursos dessa poderosa ferramenta



DICA CONTEUDO: https://www.digitalocean.com/community/tutorials/iptables-essentials-common-firewall-rules-and-commands#allowing-established-outgoing-connections