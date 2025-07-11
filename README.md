# ETL de Viagens a Serviço do Governo

Este projeto realiza a extração, transformação e carga (ETL) de dados de viagens a serviço do governo federal a partir de um arquivo CSV público, carregando os dados tratados em um banco de dados MySQL (XAMPP).

## Funcionalidades

- Leitura de arquivo CSV de viagens públicas
- Conversão e limpeza de colunas financeiras
- Carregamento dos dados em banco MySQL via SQLAlchemy
- Pronto para análises e relatórios

## Pré-requisitos

- Python 3.8 ou superior
- XAMPP com MySQL ativo
- Bibliotecas Python: pandas, sqlalchemy, pymysql

## Instalação

1. Clone este repositório:
   git clone https://github.com/eduardopedrox/pipeline-ETL.git
   cd pipeline-ETL

2. Instale as dependências:
   pip install -r requirements.txt

3. Certifique-se de que o MySQL do XAMPP está rodando e crie um banco chamado `etldb` via phpMyAdmin.

4. Coloque o arquivo CSV (`2025_Viagem.csv`) na raiz do projeto.

## Como usar

Execute o script principal:

python etl.py

## O script irá:

- Ler o arquivo CSV
- Limpar e converter os dados das colunas financeiras
- Carregar os dados na tabela `viagens` do banco `etldb`

## Observações

- Ajuste o nome das colunas no script caso o arquivo CSV tenha alterações.
- Não compartilhe dados sensíveis (senhas, CPFs, etc.) em repositórios públicos.

## Licença

Este projeto está sob a licença MIT.
