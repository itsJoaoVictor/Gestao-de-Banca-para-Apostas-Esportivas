import pandas as pd
#Criar arquivo csv a partir de um dataframe
base = pd.DataFrame({'Id':[],'Data':[],'Esporte':[],'Campeonato':[],'Mandante':[],'Visitante':[],'Mercado':[],'Stake':[],'Odd':[],'Resultado':[],'Lucro':[]})
#Salvar arquivo csv
base.to_csv('gestao_banca.csv',index=False)

