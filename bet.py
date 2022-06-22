from helper import Conversor_Date, Arquivo
import pandas as pd

#classe para cadastrar apostas
class Bet: 
    def __init__(self, data: str, esporte: str, campeonato: str, mandante: str, visitante: str, mercado: str, stake: float, odd: float, resultado: str) -> None:
        self.data = Conversor_Date().str_para_date(data)
        self.esporte = esporte
        self.campeonato = campeonato
        self.mandante = mandante
        self.visitante = visitante
        self.mercado = mercado
        self.stake = stake
        self.odd = odd
        self.resultado = resultado
        self.lucro = self.calcular_lucro()
        
    def calcular_lucro(self) -> float:
        if self.resultado.lower() == 'green':
            green = ((self.stake * self.odd) - self.stake)
            #return green com 2 casas decimais
            return round(green, 2)

        elif self.resultado.lower() == 'red':
            red =  -self.stake
            return round(red, 2)
        elif self.resultado.lower() == 'half red':
            half_red = -(self.stake / 2)
            return round(half_red, 2)
        elif self.resultado.lower() == 'half green':
            half_green = ((self.stake * self.odd) - self.stake) / 2
            return round(half_green, 2)
        elif self.resultado.lower() == 'void':
            return 0
        elif self.resultado.lower() == 'pendente':
            return 0
        else:
            return 0
            
    
    def __str__(self) -> str:
        return f'Data: {Conversor_Date().date_para_str(self.data)}\nEsporte: {self.esporte}\nCampeonato: {self.campeonato}\nMandante: {self.mandante}\nVisitante: {self.visitante}\nMercado: {self.mercado}\nStake: {self.stake}\nOdd: {self.odd}\nResultado: {self.resultado}\nLucro: R${self.lucro:.2f}'
    
    #metodo para salvar aposta no arquivo
    def salvar_aposta(self, dataframe: pd.DataFrame) -> None:
        dataframe.loc[len(dataframe)] = [Conversor_Date().date_para_str(self.data), self.esporte, self.campeonato, self.mandante, self.visitante, self.mercado, self.stake, self.odd, self.resultado, self.lucro]
        Arquivo('gestao_banca.csv').escrita(dataframe)
        
        
        
#Testar classe Bet
'''bet = Bet('01/01/2020', 'Futebol', 'Brasileirao', 'Palmeiras', 'Santos', 'Over', 10, 1.52, 'Green')
print(bet)
bet1 = Bet('01/01/2020', 'Futebol', 'Brasileirao', 'Palmeiras', 'Santos', 'Over', 10, 1.5, 'Red') 
bet2 = Bet('01/01/2020', 'Futebol', 'Brasileirao', 'Palmeiras', 'Santos', 'Over', 10, 1.50, 'Half Red') 
bet3 = Bet('01/01/2020', 'Futebol', 'Brasileirao', 'Palmeiras', 'Santos', 'Over', 10, 1.33, 'Half Green')
bet4 = Bet('01/01/2020', 'Futebol', 'Brasileirao', 'Palmeiras', 'Santos', 'Over', 10, 1.5, 'Void')
bet5 = Bet('01/01/2020', 'Futebol', 'Brasileirao', 'Palmeiras', 'Santos', 'Over', 10, 1.5, 'Pendente')

#adicionar aposta no arquivo
bet.salvar_aposta(Arquivo('gestao_banca.csv').leitura())
bet1.salvar_aposta(Arquivo('gestao_banca.csv').leitura())
bet2.salvar_aposta(Arquivo('gestao_banca.csv').leitura())
bet3.salvar_aposta(Arquivo('gestao_banca.csv').leitura())
bet4.salvar_aposta(Arquivo('gestao_banca.csv').leitura())
bet5.salvar_aposta(Arquivo('gestao_banca.csv').leitura())

#printar todas as apostas
print(Arquivo('gestao_banca.csv').leitura())'''


