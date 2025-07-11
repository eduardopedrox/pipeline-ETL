import pandas as pd
from sqlalchemy import create_engine

df = pd.read_csv('2025_Viagem.csv', delimiter=';', encoding='latin1')

for coluna in ['Valor devolucao', 'Valor outros gastos']:
    df[coluna] = (
        df[coluna]
        .astype(str)
        .str.replace('.', '', regex=False)
        .str.replace(',', '.', regex=False)
        .astype(float)
    )


print(df[['Valor devolucao', 'Valor outros gastos']].head())

usuario = 'root'
senha = ''
host = 'localhost'
banco = 'etldb'

engine = create_engine(f'mysql+pymysql://{usuario}:{senha}@{host}/{banco}')

df.to_sql('viagens', con=engine, if_exists='replace', index=False)
print("Dados carregados com sucesso!")
