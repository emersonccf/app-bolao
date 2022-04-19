# Bolão da Sorte

Sistema destinado a participação de apostadores em bolões de partidas de futebol.

## Qual problema e motivação este sistema pretende resolver?

1. A inspiração para este sistema vem de uma atividade muito comum em tempos de copa do mundo: Apostar em um BOLÃO. O sistema deve:
   a. Na parte de voltada ao administrador:
   i. Permitir o cadastro dos apostadores (Nome, Login (único) e senha). Cada novo apostador recebe um crédito de R$ 10,00 automaticamente.
   ii. Permitir o cadastro das partidas.
   iii. Definir o resultado das partidas
   iv. Adicionar créditos para um jogador.
   b. Na parte pública
   i. Permitir que um Apostador faça o login
   ii. Depois de logar, deve exibir o nome do Apostador, o valor que ele tem a sua disposição para apostar e a lista de todas as partidas cadastradas.
   iii. Permitir que um Apostador possa selecionar e Apostar em uma partida (Apenas uma aposta de cada Apostador por partida). Cada aposta tem valor fixo de R$ 5,00.
   iv. Distribuir o prêmio (total do montante de apostas) usando o seguinte critério (nessa ordem): 1. O vencedor será quem acertar o placar. Se mais de um Apostador acertar o placar, o premio será dividido igualmente entre eles. 2. Se ninguém acertar o placar, o vencedor será quem acertar o resultado (vitória ou empate). Se mais de um Apostador acertar o resultado, o premio será dividido igualmente entre eles. 3. Se Ninguém acertar o resultado, o dinheiro vai ser devolvido para cada Apostador.
   v. Listar o ranking dos Apostadores cadastrados ordenados por valores ganhos.
2. O sistema deve ser feito em Python + Django e usar um banco de dados relacional (a sua escolha). A escolha de qualquer outra biblioteca
   / tecnologia complementar está autorizada.

## Como Proceder?

1. Certifique-se de ter instalado e funcionando o Docker v. 20.10.14 e o Docker Compose v. 2.4.1 em seu sistema operacional antes deste processo;
2. Clone o repositório;
3. Entre na pasta do repositório (diretório de trabalho) `app-bolao`;
4. Execute o comando para baixar as imagens e compor os containers da aplicação e do banco de dados;
5. Reinicie os containers para que possam se reconhecerem em rede;
6. Execute o comando que irá chamar um script de nome `app_up.sh` que irá fazer a migração da base de dados, popular as tabelas com alguns registros, coletar os arquivos estáticos e solicitar as credenciais, se desejar, para a criação de super usuário para acessoa à area administrativa do sistema (`localhost:8000/admin`), caso não deseje criar este usuário basta pressiona CRTL + C, para abortar esta etapa.
7. Abra a aplicação no link, em seu navegador de preferência: `localhost:8000`

Certifique-se de executar os comandos do docker-compose dentro da pasta de trabalho `app-bolao`. Os comandos para realizar as etapas descritas acima são os seguintes:

### No Windows (PowerShell) - Copie estas linhas em conjunto, cole no PowerShell e execute:

```commandline
git clone https://github.com/emersonccf/app-bolao.git && `
cd app-bolao && `
docker-compose up -d && `
docker-compose restart && `
docker-compose exec -it app ./app_up.sh && `
docker-compose restart
```

### No Unix (Linux/Mac) - Copie estas linhas em conjunto, cole no Terminal e execute:

```commandline
git clone https://github.com/emersonccf/app-bolao.git && \
cd app-bolao && \
docker-compose up -d && \
docker-compose restart && \
docker-compose exec -it app ./app_up.sh && \
docker-compose restart
```

### ATENÇÃO:

1. Pode ocorrer um erro no passo 6 que representa a linha de comando `docker-compose exec -it app ./app_up.sh` e não seja possível criar o super usuário neste script. Caso isto ocorra execute a linha de comando abaixo, para criar um super usuário:

```commandline
docker exec -it app-bolao-app bash -c "python manage.py createsuperuser"
```

2. Caso dê algo errado ou não funcione, habitue-se a consultar o log do container para saber o que pode ter ocorrido, então use:

a. para verificar logs do serviço app

```commandline
docker-compose logs -ft app
```

b. para verificar logs do serviço mysql

```commandline
docker-compose logs -ft mysql
```

ATENÇÃO: o horário do log é apresentado no formato UTC.

3. Para fazer as coisas se ajustarem sempre é bom reiniciar os serviços, então tente:

```commandline
docker-compose restart
```

### Outros Comandos, coso necessário:

Para eliminar os containers, apagar as imagens, a rede e o volume onde foram armazenados os dados, execute o seguinte comando:

```commandline
docker-compose down -v --rmi all
```

Caso queira apenas remover os containers e deixar as imagens e o volume para para rodar a aplicação em outra oportunidade, faça:

```commandline
docker-compose down
```

Caso queira somente parar o serviço dos container, execute:

```commandline
docker-compose stop
```

E para recarregar um serviço que foi parado, execute:

```commandline
docker-compose start
```

### Esperamos que este exemplo possa lhe ajudar a compreender o uso do Docker associado ao Python com Django utilizando como banco de dados o MySQL 5.7.
