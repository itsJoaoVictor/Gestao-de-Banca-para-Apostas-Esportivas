from argparse import _AppendConstAction
from datetime import date
from datetime import datetime
from xml.etree.ElementInclude import LimitedRecursiveIncludeError
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Classe para conversao de datas
class Conversor_Date:
    def str_para_date(self, data: str) -> date:
        return datetime.strptime(data, '%d/%m/%Y').date()
    
    def date_para_str(self, data: date) -> str:
        return data.strftime('%d/%m/%Y')
            
            
class Arquivo: #classe para leitura e escrita de arquivos
    def __init__(self:object, nome_arquivo: str):
        self.nome_arquivo = nome_arquivo
        
    def leitura(self:object) -> pd.DataFrame:
        return pd.read_csv(self.nome_arquivo)
    
    def escrita(self:object, dataframe: pd.DataFrame):
        dataframe.to_csv(self.nome_arquivo, index=False)
        
    
    
#class para listar informações
class Listar:
    def __init__(self:object, dataframe: pd.DataFrame):
        self.dataframe = dataframe
    
    #metodo para listar esportes
    def esportes(self:object) -> None:
        esportes = self.dataframe['Esporte'].unique()
        print('\n')
        print('Esportes:')
        for i in range(len(esportes)):
            print(esportes[i])
    
    
    #metodo para listar campeonatos
    def campeonatos(self:object) -> None:
        campeonatos = self.dataframe['Campeonato'].unique()
        print('\n')
        print('Campeonatos:')
        for i in range(len(campeonatos)):
            print(campeonatos[i])
    
    
    #metodo para listar mercados
    def mercados(self:object) -> None:
        mercados = self.dataframe['Mercado'].unique()
        print('\n')
        print('Mercados:')
        for i in range(len(mercados)):
            print(mercados[i])
            
    def apostas(self:object) -> None:
        apostas = self.dataframe
        print('\n')
        print('Apostas:')
        for i in range(len(apostas)):
            print(apostas.iloc[i])
            print('\n')
            
    def ultima_aposta(self:object) -> None:
        ultima_aposta = self.dataframe.iloc[-1]
        print('\n')
        print('Última Aposta:')
        print(ultima_aposta)
        print('\n')
        
    #Listar apostar por esporte
    def apostas_esporte(self:object, esporte: str) -> None:
        apostas_esporte = self.dataframe[self.dataframe['Esporte'] == esporte]
        print('\n')
        print('Apostas de ' + esporte + ':')
        for i in range(len(apostas_esporte)):
            print(apostas_esporte.iloc[i])
            print('\n')
    
    #listar apostas por campeonato
    def apostas_campeonato(self:object, campeonato: str) -> None:
        apostas_campeonato = self.dataframe[self.dataframe['Campeonato'] == campeonato]
        print('\n')
        print('Apostas de ' + campeonato + ':')
        for i in range(len(apostas_campeonato)):
            print(apostas_campeonato.iloc[i])
            print('\n')
    
    #listar apostas por mercado
    def apostas_mercado(self:object, mercado: str) -> None:
        apostas_mercado = self.dataframe[self.dataframe['Mercado'] == mercado]
        print('\n')
        print('Apostas de ' + mercado + ':')
        for i in range(len(apostas_mercado)):
            print(apostas_mercado.iloc[i])
            print('\n')
    
    def aposta_data(self:object, data: str) -> None:
        apostas_data = self.dataframe[self.dataframe['Data'] == data]
        print('\n')
        print('Apostas de ' + data + ':')
        for i in range(len(apostas_data)):
            print(apostas_data.iloc[i])
            print('\n')
    
            
#classe para exibir informações
class Informacoes:
    def __init__(self:object, dataframe: pd.DataFrame):
        self.dataframe = dataframe
    
    def info_por_esporte(self:object, esporte: str) -> None:
        dataframe_esporte = self.dataframe[self.dataframe['Esporte'] == esporte]
        print('\n')
        print(f'Informações sobre o esporte {esporte}:')
        print(f'Total de apostas: {len(dataframe_esporte)}')
        print(f'Total de lucros: R$ {dataframe_esporte["Lucro"].sum():.2f}')
        #Calcular ROE
        roe = dataframe_esporte["Lucro"].sum() / dataframe_esporte["Stake"].sum()
        print(f'ROE: {roe:.2%}')
        #Contar quantidade de apostas ganhas
        qtd_ganhas = len(dataframe_esporte[dataframe_esporte['Lucro'] > 0])
        #contar quantidade de apostas
        qtd_apostas = len(dataframe_esporte)
        #calcular taxa de acerto
        taxa_acerto = qtd_ganhas / qtd_apostas
        print(f'Taxa de acerto: {taxa_acerto:.2%}')
        
    def info_por_campeonato(self:object, campeonato: str) -> None:
        dataframe_campeonato = self.dataframe[self.dataframe['Campeonato'] == campeonato]
        print('\n')
        print(f'Informações sobre o campeonato {campeonato}:')
        print(f'Total de apostas: {len(dataframe_campeonato)}')
        print(f'Total de lucros: R$ {dataframe_campeonato["Lucro"].sum():.2f}')
        #Calcular ROE
        roe = dataframe_campeonato["Lucro"].sum() / dataframe_campeonato["Stake"].sum()
        print(f'ROE: {roe:.2%}')
        #Contar quantidade de apostas ganhas
        qtd_ganhas = len(dataframe_campeonato[dataframe_campeonato['Lucro'] > 0])
        #contar quantidade de apostas
        qtd_apostas = len(dataframe_campeonato)
        #calcular taxa de acerto
        taxa_acerto = qtd_ganhas / qtd_apostas
        print(f'Taxa de acerto: {taxa_acerto:.2%}')
    
    def info_por_mercado(self:object, mercado: str) -> None:
        dataframe_mercado = self.dataframe[self.dataframe['Mercado'] == mercado]
        print('\n')
        print(f'Informações sobre o mercado {mercado}:')
        print(f'Total de apostas: {len(dataframe_mercado)}')
        print(f'Total de lucros: R$ {dataframe_mercado["Lucro"].sum():.2f}')
        #Calcular ROE
        roe = dataframe_mercado["Lucro"].sum() / dataframe_mercado["Stake"].sum()
        print(f'ROE: {roe:.2%}')
        #Contar quantidade de apostas ganhas
        qtd_ganhas = len(dataframe_mercado[dataframe_mercado['Lucro'] > 0])
        #contar quantidade de apostas
        qtd_apostas = len(dataframe_mercado)
        #calcular taxa de acerto
        taxa_acerto = qtd_ganhas / qtd_apostas
        print(f'Taxa de acerto: {taxa_acerto:.2%}')
    
    #metodo para exibir informações por mes
    def info_mes_janeiro(self:object) -> None:
        dataframe_mes_janeiro = self.dataframe[self.dataframe['Data'].str.contains('01')]
        print('\n')
        print('Informações do mes de janeiro:')
        print(f'Total de apostas: {len(dataframe_mes_janeiro)}')
        print(f'Total Investido: R$ {dataframe_mes_janeiro["Stake"].sum():.2f}')
        print(f'Total de lucros: R$ {dataframe_mes_janeiro["Lucro"].sum():.2f}')
        #Calcular ROE
        roe = dataframe_mes_janeiro["Lucro"].sum() / dataframe_mes_janeiro["Stake"].sum()
        print(f'ROE: {roe:.2%}')
        #Contar quantidade de apostas ganhas
        qtd_ganhas = len(dataframe_mes_janeiro[dataframe_mes_janeiro['Lucro'] > 0])
        #contar quantidade de apostas
        qtd_apostas = len(dataframe_mes_janeiro)
        #calcular taxa de acerto
        taxa_acerto = qtd_ganhas / qtd_apostas
        print(f'Taxa de acerto: {taxa_acerto:.2%}')
        
    def info_mes_fevereiro(self:object) -> None:
        dataframe_mes_fevereiro = self.dataframe[self.dataframe['Data'].str.contains('02')]
        print('\n')
        print('Informações do mes de fevereiro:')
        print(f'Total de apostas: {len(dataframe_mes_fevereiro)}')
        print(f'Total Investido: R$ {dataframe_mes_fevereiro["Stake"].sum():.2f}')
        print(f'Total de lucros: R$ {dataframe_mes_fevereiro["Lucro"].sum():.2f}')
        #Calcular ROE
        roe = dataframe_mes_fevereiro["Lucro"].sum() / dataframe_mes_fevereiro["Stake"].sum()
        print(f'ROE: {roe:.2%}')
        #Contar quantidade de apostas ganhas
        qtd_ganhas = len(dataframe_mes_fevereiro[dataframe_mes_fevereiro['Lucro'] > 0])
        #contar quantidade de apostas
        qtd_apostas = len(dataframe_mes_fevereiro)
        #calcular taxa de acerto
        taxa_acerto = qtd_ganhas / qtd_apostas
        print(f'Taxa de acerto: {taxa_acerto:.2%}')
        
    def info_mes_marco(self:object) -> None:
        dataframe_mes_marco = self.dataframe[self.dataframe['Data'].str.contains('03')]
        print('\n')
        print('Informações do mes de março:')
        print(f'Total de apostas: {len(dataframe_mes_marco)}')
        print(f'Total Investido: R$ {dataframe_mes_marco["Stake"].sum():.2f}')
        print(f'Total de lucros: R$ {dataframe_mes_marco["Lucro"].sum():.2f}')
        #Calcular ROE
        roe = dataframe_mes_marco["Lucro"].sum() / dataframe_mes_marco["Stake"].sum()
        print(f'ROE: {roe:.2%}')
        #Contar quantidade de apostas ganhas
        qtd_ganhas = len(dataframe_mes_marco[dataframe_mes_marco['Lucro'] > 0])
        #contar quantidade de apostas
        qtd_apostas = len(dataframe_mes_marco)
        #calcular taxa de acerto
        taxa_acerto = qtd_ganhas / qtd_apostas
        print(f'Taxa de acerto: {taxa_acerto:.2%}')
    
    def info_mes_abril(self:object) -> None:
        dataframe_mes_abril = self.dataframe[self.dataframe['Data'].str.contains('04')]
        print('\n')
        print('Informações do mes de abril:')
        print(f'Total de apostas: {len(dataframe_mes_abril)}')
        print(f'Total Investido: R$ {dataframe_mes_abril["Stake"].sum():.2f}')
        print(f'Total de lucros: R$ {dataframe_mes_abril["Lucro"].sum():.2f}')
        #Calcular ROE
        roe = dataframe_mes_abril["Lucro"].sum() / dataframe_mes_abril["Stake"].sum()
        print(f'ROE: {roe:.2%}')
        #Contar quantidade de apostas ganhas
        qtd_ganhas = len(dataframe_mes_abril[dataframe_mes_abril['Lucro'] > 0])
        #contar quantidade de apostas
        qtd_apostas = len(dataframe_mes_abril)
        #calcular taxa de acerto
        taxa_acerto = qtd_ganhas / qtd_apostas
        print(f'Taxa de acerto: {taxa_acerto:.2%}')
        
    def info_mes_maio(self:object) -> None:
        dataframe_mes_maio = self.dataframe[self.dataframe['Data'].str.contains('05')]
        print('\n')
        print('Informações do mes de maio:')
        print(f'Total de apostas: {len(dataframe_mes_maio)}')
        print(f'Total Investido: R$ {dataframe_mes_maio["Stake"].sum():.2f}')
        print(f'Total de lucros: R$ {dataframe_mes_maio["Lucro"].sum():.2f}')
        #Calcular ROE
        roe = dataframe_mes_maio["Lucro"].sum() / dataframe_mes_maio["Stake"].sum()
        print(f'ROE: {roe:.2%}')
        #Contar quantidade de apostas ganhas
        qtd_ganhas = len(dataframe_mes_maio[dataframe_mes_maio['Lucro'] > 0])
        #contar quantidade de apostas
        qtd_apostas = len(dataframe_mes_maio)
        #calcular taxa de acerto
        taxa_acerto = qtd_ganhas / qtd_apostas
        print(f'Taxa de acerto: {taxa_acerto:.2%}')
        
    def info_mes_junho(self:object) -> None:
        dataframe_mes_junho = self.dataframe[self.dataframe['Data'].str.contains('06')]
        print('\n')
        print('Informações do mes de junho:')
        print(f'Total de apostas: {len(dataframe_mes_junho)}')
        print(f'Total Investido: R$ {dataframe_mes_junho["Stake"].sum():.2f}')
        print(f'Total de lucros: R$ {dataframe_mes_junho["Lucro"].sum():.2f}')
        #Calcular ROE
        roe = dataframe_mes_junho["Lucro"].sum() / dataframe_mes_junho["Stake"].sum()
        print(f'ROE: {roe:.2%}')
        #Contar quantidade de apostas ganhas
        qtd_ganhas = len(dataframe_mes_junho[dataframe_mes_junho['Lucro'] > 0])
        #contar quantidade de apostas
        qtd_apostas = len(dataframe_mes_junho)
        #calcular taxa de acerto
        taxa_acerto = qtd_ganhas / qtd_apostas
        print(f'Taxa de acerto: {taxa_acerto:.2%}')
    
    def info_mes_julho(self:object) -> None:
        dataframe_mes_julho = self.dataframe[self.dataframe['Data'].str.contains('07')]
        print('\n')
        print('Informações do mes de julho:')
        print(f'Total de apostas: {len(dataframe_mes_julho)}')
        print(f'Total Investido: R$ {dataframe_mes_julho["Stake"].sum():.2f}')
        print(f'Total de lucros: R$ {dataframe_mes_julho["Lucro"].sum():.2f}')
        #Calcular ROE
        roe = dataframe_mes_julho["Lucro"].sum() / dataframe_mes_julho["Stake"].sum()
        print(f'ROE: {roe:.2%}')
        #Contar quantidade de apostas ganhas
        qtd_ganhas = len(dataframe_mes_julho[dataframe_mes_julho['Lucro'] > 0])
        #contar quantidade de apostas
        qtd_apostas = len(dataframe_mes_julho)
        #calcular taxa de acerto
        taxa_acerto = qtd_ganhas / qtd_apostas
        print(f'Taxa de acerto: {taxa_acerto:.2%}')
    
    def info_mes_agosto(self:object) -> None:
        dataframe_mes_agosto = self.dataframe[self.dataframe['Data'].str.contains('08')]
        print('\n')
        print('Informações do mes de agosto:')
        print(f'Total de apostas: {len(dataframe_mes_agosto)}')
        print(f'Total Investido: R$ {dataframe_mes_agosto["Stake"].sum():.2f}')
        print(f'Total de lucros: R$ {dataframe_mes_agosto["Lucro"].sum():.2f}')
        #Calcular ROE
        roe = dataframe_mes_agosto["Lucro"].sum() / dataframe_mes_agosto["Stake"].sum()
        print(f'ROE: {roe:.2%}')
        #Contar quantidade de apostas ganhas
        qtd_ganhas = len(dataframe_mes_agosto[dataframe_mes_agosto['Lucro'] > 0])
        #contar quantidade de apostas
        qtd_apostas = len(dataframe_mes_agosto)
        #calcular taxa de acerto
        taxa_acerto = qtd_ganhas / qtd_apostas
        print(f'Taxa de acerto: {taxa_acerto:.2%}')
        
    def info_mes_setembro(self:object) -> None:
        dataframe_mes_setembro = self.dataframe[self.dataframe['Data'].str.contains('09')]
        print('\n')
        print('Informações do mes de setembro:')
        print(f'Total de apostas: {len(dataframe_mes_setembro)}')
        print(f'Total Investido: R$ {dataframe_mes_setembro["Stake"].sum():.2f}')
        print(f'Total de lucros: R$ {dataframe_mes_setembro["Lucro"].sum():.2f}')
        #Calcular ROE
        roe = dataframe_mes_setembro["Lucro"].sum() / dataframe_mes_setembro["Stake"].sum()
        print(f'ROE: {roe:.2%}')
        #Contar quantidade de apostas ganhas
        qtd_ganhas = len(dataframe_mes_setembro[dataframe_mes_setembro['Lucro'] > 0])
        #contar quantidade de apostas
        qtd_apostas = len(dataframe_mes_setembro)
        #calcular taxa de acerto
        taxa_acerto = qtd_ganhas / qtd_apostas
        print(f'Taxa de acerto: {taxa_acerto:.2%}')
        
    def info_mes_outubro(self:object) -> None:
        dataframe_mes_outubro = self.dataframe[self.dataframe['Data'].str.contains('10')]
        print('\n')
        print('Informações do mes de outubro:')
        print(f'Total de apostas: {len(dataframe_mes_outubro)}')
        print(f'Total Investido: R$ {dataframe_mes_outubro["Stake"].sum():.2f}')
        print(f'Total de lucros: R$ {dataframe_mes_outubro["Lucro"].sum():.2f}')
        #Calcular ROE
        roe = dataframe_mes_outubro["Lucro"].sum() / dataframe_mes_outubro["Stake"].sum()
        print(f'ROE: {roe:.2%}')
        #Contar quantidade de apostas ganhas
        qtd_ganhas = len(dataframe_mes_outubro[dataframe_mes_outubro['Lucro'] > 0])
        #contar quantidade de apostas
        qtd_apostas = len(dataframe_mes_outubro)
        #calcular taxa de acerto
        taxa_acerto = qtd_ganhas / qtd_apostas
        print(f'Taxa de acerto: {taxa_acerto:.2%}')
        
    def info_mes_novembro(self:object) -> None:
        dataframe_mes_novembro = self.dataframe[self.dataframe['Data'].str.contains('11')]
        print('\n')
        print('Informações do mes de novembro:')
        print(f'Total de apostas: {len(dataframe_mes_novembro)}')
        print(f'Total Investido: R$ {dataframe_mes_novembro["Stake"].sum():.2f}')
        print(f'Total de lucros: R$ {dataframe_mes_novembro["Lucro"].sum():.2f}')
        #Calcular ROE
        roe = dataframe_mes_novembro["Lucro"].sum() / dataframe_mes_novembro["Stake"].sum()
        print(f'ROE: {roe:.2%}')
        #Contar quantidade de apostas ganhas
        qtd_ganhas = len(dataframe_mes_novembro[dataframe_mes_novembro['Lucro'] > 0])
        #contar quantidade de apostas
        qtd_apostas = len(dataframe_mes_novembro)
        #calcular taxa de acerto
        taxa_acerto = qtd_ganhas / qtd_apostas
        print(f'Taxa de acerto: {taxa_acerto:.2%}')
        
    def info_mes_dezembro(self:object) -> None:
        dataframe_mes_dezembro = self.dataframe[self.dataframe['Data'].str.contains('12')]
        print('\n')
        print('Informações do mes de dezembro:')
        print(f'Total de apostas: {len(dataframe_mes_dezembro)}')
        print(f'Total de Investido: R$ {dataframe_mes_dezembro["Stake"].sum():.2f}')
        print(f'Total de lucros: R$ {dataframe_mes_dezembro["Lucro"].sum():.2f}')
        #Calcular ROE
        roe = dataframe_mes_dezembro["Lucro"].sum() / dataframe_mes_dezembro["Stake"].sum()
        print(f'ROE: {roe:.2%}')
        #Contar quantidade de apostas ganhas
        qtd_ganhas = len(dataframe_mes_dezembro[dataframe_mes_dezembro['Lucro'] > 0])
        #contar quantidade de apostas
        qtd_apostas = len(dataframe_mes_dezembro)
        #calcular taxa de acerto
        taxa_acerto = qtd_ganhas / qtd_apostas
        print(f'Taxa de acerto: {taxa_acerto:.2%}')
             
    #Exibir informaçoes de lucro de cada dia formatado como R$
    def info_lucro_dia(self:object) -> None:
        print('\n')
        print('Informações de lucro por dia:')
        print(self.dataframe.groupby('Data').sum()['Lucro'])
        
    #exibir  quantidade de apostas, total investido e total de lucro, roe e win rate de cada esporte
    def info_esporte(self:object) -> None:
        #pegar todos os esportes
        esportes = self.dataframe['Esporte'].unique()
        #Pegar o total de apostas de cada esporte
        for esporte in esportes:
            print(f'\n{esporte}')
            total_apostas = len(self.dataframe[self.dataframe['Esporte'] == esporte])
            print(f'Total de apostas: {total_apostas}')
            #Pegar o total investido de cada esporte
            total_investido = self.dataframe[self.dataframe['Esporte'] == esporte]['Stake'].sum()
            print(f'Total investido: R$ {total_investido:.2f}')
            #Pegar o total de lucro de cada esporte
            total_lucro = self.dataframe[self.dataframe['Esporte'] == esporte]['Lucro'].sum()
            print(f'Total de lucro: R$ {total_lucro:.2f}')
            #Calcular ROE
            roe = total_lucro / total_investido
            print(f'ROE: {roe:.2%}')
            #Calcular win rate
            apostas_ganha = len(self.dataframe[(self.dataframe['Esporte'] == esporte) & (self.dataframe['Lucro'] > 0)])
            win_rate = apostas_ganha / total_apostas
            print(f'Win rate: {win_rate:.2%}')
            
            
    def info_campeonato(self:object) -> None:
        #pegar todos os campeonatos
        campeonatos = self.dataframe['Campeonato'].unique()
        #Pegar o total de apostas de cada campeonato
        for campeonato in campeonatos:
            print(f'\n{campeonato}')
            total_apostas = len(self.dataframe[self.dataframe['Campeonato'] == campeonato])
            print(f'Total de apostas: {total_apostas}')
            #Pegar o total investido de cada campeonato
            total_investido = self.dataframe[self.dataframe['Campeonato'] == campeonato]['Stake'].sum()
            print(f'Total investido: R$ {total_investido:.2f}')
            #Pegar o total de lucro de cada campeonato
            total_lucro = self.dataframe[self.dataframe['Campeonato'] == campeonato]['Lucro'].sum()
            print(f'Total de lucro: R$ {total_lucro:.2f}')
            #Calcular ROE
            roe = total_lucro / total_investido
            print(f'ROE: {roe:.2%}')
            #Calcular win rate
            apostas_ganha = len(self.dataframe[(self.dataframe['Campeonato'] == campeonato) & (self.dataframe['Lucro'] > 0)])
            win_rate = apostas_ganha / total_apostas
            print(f'Win rate: {win_rate:.2%}')
        
    def info_mercado(self:object) -> None:
        #pegar todos os mercados
        mercados = self.dataframe['Mercado'].unique()
        #Pegar o total de apostas de cada mercado
        for mercado in mercados:
            print(f'\n{mercado}')
            total_apostas = len(self.dataframe[self.dataframe['Mercado'] == mercado])
            print(f'Total de apostas: {total_apostas}')
            #Pegar o total investido de cada mercado
            total_investido = self.dataframe[self.dataframe['Mercado'] == mercado]['Stake'].sum()
            print(f'Total investido: R$ {total_investido:.2f}')
            #Pegar o total de lucro de cada mercado
            total_lucro = self.dataframe[self.dataframe['Mercado'] == mercado]['Lucro'].sum()
            print(f'Total de lucro: R$ {total_lucro:.2f}')
            #Calcular ROE
            roe = total_lucro / total_investido
            print(f'ROE: {roe:.2%}')
            #Calcular win rate
            apostas_ganha = len(self.dataframe[(self.dataframe['Mercado'] == mercado) & (self.dataframe['Lucro'] > 0)])
            win_rate = apostas_ganha / total_apostas
            print(f'Win rate: {win_rate:.2%}')
        
       
#classe para gerar graficos
class Graficos(object):
    def __init__(self, dataframe:pd.DataFrame):
        self.dataframe = dataframe
    
    def grafico_esporte(self:object) -> None:
        #Criar um dataframe com os lucros de cada esporte
        lucro_esporte = self.dataframe.groupby('Esporte').sum()['Lucro']
        #criar cada esporte como uma coluna
        lucro_esporte = lucro_esporte.to_frame()
        for esporte in lucro_esporte.index:
            #criar um grafico de barras para cada esporte
            plt.bar(esporte, lucro_esporte.loc[esporte][0])
        #colocar valor de lucro em cada barra centralizado com duas casas decimais
        for bar in lucro_esporte.index:
            plt.text(bar, lucro_esporte.loc[bar][0], f'R${lucro_esporte.loc[bar][0]:.2f}',horizontalalignment='center',fontsize=10, color='black', weight='bold')
        #titulo do grafico
        plt.title('Lucro por esporte')
        #nome das colunas
        plt.xlabel('Esporte')
        plt.ylabel('Lucro') 
        #ajustar grafico para o tamanho da tela
        plt.tight_layout()    
        #exibir grafico
        plt.show()
    
    
    def grafico_campeonato (self:object) -> None:
        #Criar um dataframe com os lucros de cada campeonato
        lucro_campeonato = self.dataframe.groupby('Campeonato').sum()['Lucro']
        #criar cada campeonato como uma coluna
        lucro_campeonato = lucro_campeonato.to_frame()
        for campeonato in lucro_campeonato.index:
            #criar um grafico de barras para cada campeonato
            plt.bar(campeonato, lucro_campeonato.loc[campeonato][0])
        #colocar valor de lucro em cada barra centralizado com duas casas decimais
        for bar in lucro_campeonato.index:
            plt.text(bar, lucro_campeonato.loc[bar][0], f'R${lucro_campeonato.loc[bar][0]:.2f}',horizontalalignment='center',fontsize=10, color='black', weight='bold')
        #titulo do grafico
        plt.title('Lucro por campeonato')
        #nome das colunas
        plt.xlabel('Campeonato')
        plt.ylabel('Lucro')
        #ajustar grafico para o tamanho da tela
        plt.tight_layout()
        #exibir grafico
        plt.show()
        
    def grafico_mercado (self:object) -> None:
        #Criar um dataframe com os lucros de cada mercado
        lucro_mercado = self.dataframe.groupby('Mercado').sum()['Lucro']
        #criar cada mercado como uma coluna
        lucro_mercado = lucro_mercado.to_frame()
        for mercado in lucro_mercado.index:
            #criar um grafico de barras para cada mercado
            plt.bar(mercado, lucro_mercado.loc[mercado][0])
        #colocar valor de lucro em cada barra centralizado com duas casas decimais
        for bar in lucro_mercado.index:
            plt.text(bar, lucro_mercado.loc[bar][0], f'R${lucro_mercado.loc[bar][0]:.2f}',horizontalalignment='center',fontsize=10, color='black', weight='bold')
        #titulo do grafico
        plt.title('Lucro por mercado')
        #nome das colunas
        plt.xlabel('Mercado')
        plt.ylabel('Lucro')
        #ajustar grafico para o tamanho da tela
        plt.tight_layout()
        #exibir grafico
        plt.show()
        
    def grafico_diario (self:object) -> None:
        #Criar um dataframe com os lucros de cada mês
        lucro_mes = self.dataframe.groupby('Data').sum()['Lucro']
        #criar cada mês como uma coluna
        lucro_mes = lucro_mes.to_frame()
        for mes in lucro_mes.index:
            #criar um grafico de barras para cada mês
            plt.bar(mes, lucro_mes.loc[mes][0])
        #colocar valor de lucro em cada barra centralizado com duas casas decimais
        for bar in lucro_mes.index:
            plt.text(bar, lucro_mes.loc[bar][0], f'R${lucro_mes.loc[bar][0]:.2f}',horizontalalignment='center',fontsize=10, color='black', weight='bold')
        #titulo do grafico
        plt.title('Lucro por dia')
        #nome das colunas
        plt.xlabel('Dia')
        plt.ylabel('Lucro')
        #ajustar grafico para o tamanho da tela
        plt.tight_layout()
        #exibir grafico
        plt.show()
    
    
#classe para controle da banca

class Banca(object):
    #construtor
    def __init__(self, dataframe:pd.DataFrame):
        self.dataframe = dataframe 
        
    def banca_inical(self:object) -> float:
        #retornar o valor inicial da banca
        banca_inical = 70
        return banca_inical

    def lucro_total(self:object) -> float:
        #calcular o lucro total da banca
        lucro_total = self.dataframe.sum()['Lucro']
        return lucro_total
    
    def banca_total(self:object) -> float:
        #calcular o valor total da banca
        banca_atual = self.banca_inical() + self.lucro_total()
        return banca_atual
    
    def sugestao_stakes(self:object) -> float:
        #calcular a sugestão de stakes
        if self.banca_total() < 100:
            big = 2
            mid = 1.5
            small = 1
            return big, mid, small

        elif self.banca_total() >= 100:
            big = self.banca_total()*(2/100)
            mid = self.banca_total()*(1.5/100)
            small = self.banca_total()*(1/100)
            return big, mid, small
    
    def alterar_banca(self:object, valor:float) -> None:
        #alterar o valor da banca
        self.banca_inical = valor
    
    def info_banca(self:object) -> None:
        #exibir informações da banca
        print(f'Banca inicial: R${self.banca_inical()}')
        print(f'Lucro total: R${self.lucro_total():.2f}')
        print(f'Banca total: R${self.banca_total():.2f}')
        print(f'Sugestão de stakes: Big: R${self.sugestao_stakes()[0]:.2f}, Mid: R${self.sugestao_stakes()[1]:.2f}, Small: R${self.sugestao_stakes()[2]:.2f}')
        


