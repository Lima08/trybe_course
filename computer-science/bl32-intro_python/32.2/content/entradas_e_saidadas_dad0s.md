Ambiente Virtual
Imagine que, em uma máquina, há um projeto Python que tem alguns pacotes de terceiros instalados e, dentre eles, há uma biblioteca na versão 1.4. Imagine também que, na mesma máquina, um novo projeto é iniciado e ele precisa da mesma biblioteca, mas, dessa vez, na versão 2.0. O que fazer? As versões são compatíveis? Se eu atualizar o sistema, a versão antiga vai continuar a funcionar?
O venv entra como resposta à essas perguntas! Ele é um módulo, já embutido na linguagem, que serve para isolar ambientes entre projetos. Ou seja, eu consigo ter dois projetos rodando, em dois ambientes diferentes, com versões diferentes de uma mesma biblioteca.
Na prática, o que vamos fazer é instalar as bibliotecas em um diretório, que está relacionado ao projeto. Assim, cada projeto pode ter suas próprias bibliotecas na versão que quiser. A ideia é a mesma do npm que vocês já vêm usando.
O comando para criação deste ambiente isolado é python3 -m venv .venv , sendo que .venv é o nome do ambiente isolado. Este comando deve ser executado na raiz do projeto.
💡 Caso o venv não esteja instalado, utilize o comando sudo apt install python3-venv .
Este ambiente isolado será visto como um diretório criado na raiz do projeto. O ponto na frente do nome faz com que o diretório fique oculto.
Depois de criado, temos de ativar este ambiente para usá-lo. Isto é importante, pois sempre que decidirmos trabalhar neste projeto devemos repetir este passo.
Comando para ativação:
 source .venv/bin/activate