# Desafio Software Engineer - Backend 

## API

## Objetivo:
O desafio é fazer uma API que busque e retorne a matrícula do servidor em um determinado portal.

## Input

Você deve criar uma api para receber um json contendo o numero do CPF do cliente e credenciais de login do portal. 

## Output

O cliente tem que ser capaz de pegar o dado quando o processamento termina, então você deve criar um mecanismo que permita isso, retornando sempre um JSON.

### Etapas obrigatórias:

* A lista de CPFs deve ser inicialmente colocada em uma fila do **RabbitMQ.**
* Na fila do rabbitmq, devem existir CPFs repetidos.
* Ao consumir da fila do **RabbitMQ** um CPF, o sistema deve verificar previamente no cache do **Redis** se existe um JSON com os dados referentes ao crawler do CPF.
* Após o crawler executar, os dados de matriculas de um CPF devem ser indexados utilizando **Elasticsearch**.
* Construir uma interface web com um campo de busca. Ao digitar um CPF, o sistema deve verificar no **Elasticsearch** se existem informações de matrícula para o CPF desejado. 

## Dependências Necessárias
- Instalar o Python 3.11
- Instalar Docker na máquina
- Instalar Pacote Poetry

## Instruções de execução

* Abrir 2 terminais de código.
* Executar na raiz do projeto o comando em um terminal 'docker-compose up', para instalar o banco de dados do elasticsearch e cache.
* No segundo terminal, na raiz do projeto digitar o comando 'poetry shell', para abrir um ambiente virtual
* digitar o comando 'poetry install'
* digitar o comando 'python main.py', para incializar a aplicação.

## Endpoints criados

- Pesquisar por todos os registros
* http://localhost:7000/api/cpf/?page={página atual}&page_size={limite da página}
* http://localhost:7000/api/cpf/?cpf={CPF para pesquisar, com pontuação}