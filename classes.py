import sqlite3
import datetime
import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from statsmodels.tsa.arima.model import ARIMA

class Aposta:
    def __init__(self, Date:str, Casa_de_apostas:str, Esporte:str, Campeonato:str, Metodo_de_aposta:str, Status:str, Mandante:str, Visitante:str,Valor_apostado:float , Odd:float, Resultado:str , lucro:float=0, Observacao:str=''):
        #Date deve ser uma string no formato 'dd/mm/aaaa'
        self.Date = datetime.datetime.strptime(Date, '%d/%m/%Y').date()
        
        self.Casa_de_apostas = Casa_de_apostas
        self.Esporte = Esporte
        self.Campeonato = Campeonato
        self.Metodo_de_aposta = Metodo_de_aposta
        self.Status = Status
        self.Mandante = Mandante
        self.Visitante = Visitante
        self.Resultado = str(Resultado)
        self.Odd = Odd
        self.Valor_apostado = Valor_apostado
        #Lucro é calculado automaticamente com base no resultado da aposta
        self.Lucro =  lucro
        self.Observacao = Observacao
        
    def cadastrar_aposta(self):
        try:
            # Criação da base de dados
            banco_de_dados = sqlite3.connect('bd_gestao_banca.db')
            cursor = banco_de_dados.cursor()
            
            
            #Inserir dados na tabela
            cursor.execute("""
            INSERT INTO Apostas (Data, Casa_de_apostas, Esporte, Campeonato, Metodo_de_aposta, status, Mandante, Visitante, Stake, Odd, Resultado, Lucro, Observacao)
            VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)
            """, (self.Date, self.Casa_de_apostas, self.Esporte, self.Campeonato, self.Metodo_de_aposta, self.Status, self.Mandante, self.Visitante, self.Valor_apostado, self.Odd, self.Resultado, self.Lucro, self.Observacao))
        
            banco_de_dados.commit()
            banco_de_dados.close()
            print('Aposta cadastrada com sucesso!')
        except:
            print('Erro ao cadastrar aposta!')
            

def alterar_aposta_pendente():
    banco_de_dados = sqlite3.connect('bd_gestao_banca.db')
    cursor = banco_de_dados.cursor()
    cursor.execute("PRAGMA foreign_keys = ON")

    cursor.execute("SELECT * FROM Apostas WHERE Resultado == 'pendente'")  
    pendentes = cursor.fetchall()
    
    if not pendentes:
        print('Não há apostas pendentes!')
        return
    
    print('Apostas pendentes:')
    for aposta in pendentes:
        print(aposta)
    
    # Solicitar o ID da aposta a ser alterada
    id_aposta = int(input("Digite o ID da aposta que deseja alterar: "))

    # Receber o novo resultado
    novo_resultado = int(input("Digite o novo resultado: 1-ganha / 2-perdida / 3-cancelada / 4-meio ganha / 5-meio perdida: "))
    lucro = 0
    if novo_resultado == 1:
        novo_resultado = 'ganha'
        lucro = (aposta[10] - 1) * aposta[9]
    elif novo_resultado == 2:
        novo_resultado = 'perdida'
        lucro = -aposta[10]
    elif novo_resultado == 3:
        novo_resultado = 'cancelada'
        lucro = 0
    elif novo_resultado == 4:
        novo_resultado = 'meio ganha'
        lucro = (aposta[10] - 1) * aposta[9] / 2
    elif novo_resultado == 5:
        novo_resultado = 'meio perdida'
        lucro = -aposta[10] / 2
    else:
        print('Opção inválida!')
        return
    
    # Atualizar o resultado da aposta no banco de dados
    cursor.execute("UPDATE Apostas SET Resultado=?, Lucro=? WHERE Id=?", (novo_resultado, lucro, id_aposta))
    banco_de_dados.commit()
    banco_de_dados.close()
    print('Aposta alterada com sucesso!')
    
def alterar_aposta_finalizada():
    banco_de_dados = sqlite3.connect('bd_gestao_banca.db')
    cursor = banco_de_dados.cursor()
    cursor.execute("PRAGMA foreign_keys = ON")

    cursor.execute("SELECT * FROM Apostas WHERE Resultado != 'pendente'")
    finalizadas = cursor.fetchall()
    
    if not finalizadas:
        print('Não há apostas finalizadas!')
        return
    
    print('Apostas finalizadas:')
    for aposta in finalizadas:
        print(aposta)
        
    # Solicitar o ID da aposta a ser alterada
    id_aposta = int(input("Digite o ID da aposta que deseja alterar: "))
    
    #Pergunta qual dado deseja alterar e recebe o novo valor
    dado = int(input("Digite o número do dado que deseja alterar: 1-data / 2-casa de apostas / 3-esporte / 4-campeonato / 5-método de aposta / 6-status / 7-mandante / 8-visitante / 9-odd / 10-valor apostado / 11-Lucro / 12-observação: "))
    if dado == 1:
        novo_dado = input("Digite a nova data: ")
        cursor.execute("UPDATE Apostas SET Data=? WHERE Id=?", (novo_dado, id_aposta))
    elif dado == 2:
        novo_dado = input("Digite a nova casa de apostas: ")
        cursor.execute("UPDATE Apostas SET Casa_de_apostas=? WHERE Id=?", (novo_dado, id_aposta))
    elif dado == 3:
        novo_dado = input("Digite o novo esporte: ")
        cursor.execute("UPDATE Apostas SET Esporte=? WHERE Id=?", (novo_dado, id_aposta))
    elif dado == 4:
        novo_dado = input("Digite o novo campeonato: ")
        cursor.execute("UPDATE Apostas SET Campeonato=? WHERE Id=?", (novo_dado, id_aposta))
    elif dado == 5:
        novo_dado = input("Digite o novo método de aposta: ")
        cursor.execute("UPDATE Apostas SET Metodo_de_aposta=? WHERE Id=?", (novo_dado, id_aposta))
    elif dado == 6:
        novo_dado = input("Digite o novo status: ")
        cursor.execute("UPDATE Apostas SET Status=? WHERE Id=?", (novo_dado, id_aposta))
    elif dado == 7:
        novo_dado = input("Digite o novo mandante: ")
        cursor.execute("UPDATE Apostas SET Mandante=? WHERE Id=?", (novo_dado, id_aposta))
    elif dado == 8:
        novo_dado = input("Digite o novo visitante: ")
        cursor.execute("UPDATE Apostas SET Visitante=? WHERE Id=?", (novo_dado, id_aposta))
    elif dado == 9:
        novo_dado = float(input("Digite a nova odd: "))
        cursor.execute("UPDATE Apostas SET Odd=? WHERE Id=?", (novo_dado, id_aposta))
    elif dado == 10:
        novo_dado = float(input("Digite o novo valor apostado: "))
        cursor.execute("UPDATE Apostas SET Valor_apostado=? WHERE Id=?", (novo_dado, id_aposta))
    elif dado == 11:
        novo_dado = float(input("Digite o novo lucro: "))
        cursor.execute("UPDATE Apostas SET Lucro=? WHERE Id=?", (novo_dado, id_aposta))
    elif dado == 12:
        novo_dado = input("Digite a nova observação: ")
        cursor.execute("UPDATE Apostas SET Observacao=? WHERE Id=?", (novo_dado, id_aposta))
    else:
        print('Opção inválida!')
        return
    
    banco_de_dados.commit()
    banco_de_dados.close()
    print('Aposta alterada com sucesso!')
        

def atualizar_estatisticas_por_data():
    banco_de_dados = sqlite3.connect('bd_gestao_banca.db')
    cursor = banco_de_dados.cursor()

    cursor.execute("PRAGMA foreign_keys = ON")

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Apostas (
            Id INTEGER PRIMARY KEY AUTOINCREMENT,
            Data DATE NOT NULL,
            Casa_de_apostas TEXT NOT NULL,
            Esporte TEXT NOT NULL,
            Campeonato TEXT NOT NULL,
            Metodo_de_aposta TEXT NOT NULL,
            Status TEXT NOT NULL,
            Mandante TEXT NOT NULL,
            Visitante TEXT NOT NULL,
            Stake REAL NOT NULL,
            Odd REAL NOT NULL,
            Resultado TEXT NOT NULL,
            Lucro REAL NOT NULL,
            Observacao TEXT
        )
    """)
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Estatisticas_por_Data (
            Data DATE PRIMARY KEY,
            Total_de_apostas INTEGER NOT NULL,
            Apostas_Ganhas INTEGER NOT NULL,
            Taxa_de_acerto REAL NOT NULL,
            Total_investido REAL NOT NULL,
            Lucro REAL NOT NULL,
            ROI REAL NOT NULL,
            Odds_medias REAL NOT NULL,
            FOREIGN KEY (Data) REFERENCES Apostas (Data)
        )
    """)

    cursor.execute("""
        SELECT Data FROM Estatisticas_por_Data
    """)
    datas_existentes = cursor.fetchall()
    datas_existentes = [data[0] for data in datas_existentes]

    cursor.execute("""
        SELECT
            Data,
            COUNT(*) AS Total_de_apostas,
            SUM(CASE WHEN Resultado = 'ganha' THEN 1 ELSE 0 END) AS Apostas_Ganhas,
            ROUND(CAST(SUM(CASE WHEN Resultado = 'ganha' THEN 1 ELSE 0 END) AS REAL) / COUNT(*) * 100, 2) AS Taxa_de_acerto,
            ROUND(SUM(Stake), 2) AS Total_investido,
            ROUND(SUM(Lucro), 2) AS Lucro,
            ROUND(SUM(Lucro) / SUM(Stake) * 100, 2) AS ROI,
            ROUND(AVG(Odd), 2) AS Odds_medias
        FROM Apostas
        GROUP BY Data
    """)
    estatisticas = cursor.fetchall()

    for estatistica in estatisticas:
        data = estatistica[0]
        if data not in datas_existentes:
            cursor.execute("""
                INSERT INTO Estatisticas_por_Data (Data, Total_de_apostas, Apostas_Ganhas, Taxa_de_acerto, Total_investido, Lucro, ROI, Odds_medias)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """, estatistica)
        else:
            cursor.execute("""
                UPDATE Estatisticas_por_Data
                SET Total_de_apostas=?, Apostas_Ganhas=?, Taxa_de_acerto=?, Total_investido=?, Lucro=?, ROI=?, Odds_medias=?
                WHERE Data=?
            """, estatistica[1:] + (data,))

    #imprimir tabela de estatisticas data por data
    cursor.execute("""
        SELECT * FROM Estatisticas_por_Data
    """)
    estatisticas = cursor.fetchall()
    for estatistica in estatisticas:
        print(f'Data: {estatistica[1]}')
        print(f'Total de apostas: {estatistica[2]}')
        print(f'Apostas ganhas: {estatistica[3]}')
        print(f'Taxa de acerto: {estatistica[4]}%')
        print(f'Total investido: R${estatistica[5]}')
        print(f'Lucro: R${estatistica[6]}')
        print(f'ROI: {estatistica[7]}%')
        print(f'Odd média: {estatistica[8]}')
        print('----------------------------------------')
        
    banco_de_dados.commit()
    banco_de_dados.close()


def atualizar_estatisticas_por_esporte():
    banco_de_dados = sqlite3.connect('bd_gestao_banca.db')
    cursor = banco_de_dados.cursor()

    cursor.execute("PRAGMA foreign_keys = ON")

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Apostas (
            Id INTEGER PRIMARY KEY AUTOINCREMENT,
            Data DATE NOT NULL,
            Casa_de_apostas TEXT NOT NULL,
            Esporte TEXT NOT NULL,
            Campeonato TEXT NOT NULL,
            Metodo_de_aposta TEXT NOT NULL,
            Status TEXT NOT NULL,
            Mandante TEXT NOT NULL,
            Visitante TEXT NOT NULL,
            Stake REAL NOT NULL,
            Odd REAL NOT NULL,
            Resultado TEXT NOT NULL,
            Lucro REAL NOT NULL,
            Observacao TEXT
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Estatisticas_por_Esporte (
            Id INTEGER PRIMARY KEY AUTOINCREMENT,
            Esporte TEXT NOT NULL,
            Total_de_apostas INTEGER NOT NULL,
            Apostas_Ganhas INTEGER NOT NULL,
            Taxa_de_acerto REAL NOT NULL,
            Total_investido REAL NOT NULL,
            Lucro REAL NOT NULL,
            ROI REAL NOT NULL,
            Odds_medias REAL NOT NULL
        )
    """)

    cursor.execute("""
        SELECT Esporte FROM Estatisticas_por_Esporte
    """)
    esportes_existentes = cursor.fetchall()
    esportes_existentes = [esporte[0] for esporte in esportes_existentes]

    cursor.execute("""
        SELECT
            Esporte,
            COUNT(*) AS Total_de_apostas,
            SUM(CASE WHEN Resultado = 'ganha' THEN 1 ELSE 0 END) AS Apostas_Ganhas,
            ROUND(CAST(SUM(CASE WHEN Resultado = 'ganha' THEN 1 ELSE 0 END) AS REAL) / COUNT(*) * 100, 2) AS Taxa_de_acerto,
            ROUND(SUM(Stake), 2) AS Total_investido,
            ROUND(SUM(Lucro), 2) AS Lucro,
            ROUND(SUM(Lucro) / SUM(Stake) * 100, 2) AS ROI,
            ROUND(AVG(Odd), 2) AS Odds_medias
        FROM Apostas
        GROUP BY Esporte
    """)
    estatisticas = cursor.fetchall()

    for estatistica in estatisticas:
        esporte = estatistica[0]
        if esporte not in esportes_existentes:
            cursor.execute("""
                INSERT INTO Estatisticas_por_Esporte (Esporte, Total_de_apostas, Apostas_Ganhas, Taxa_de_acerto, Total_investido, Lucro, ROI, Odds_medias)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """, estatistica)
        else:
            cursor.execute("""
                UPDATE Estatisticas_por_Esporte
                SET Total_de_apostas=?, Apostas_Ganhas=?, Taxa_de_acerto=?, Total_investido=?, Lucro=?, ROI=?, Odds_medias=?
                WHERE Esporte=?
            """, estatistica[1:] + (esporte,))
            
    #imprimir tabela de estatisticas esporte por esporte
    cursor.execute("""
        SELECT * FROM Estatisticas_por_Esporte
    """)
    estatisticas = cursor.fetchall()
    for estatistica in estatisticas:
        print(f'Esporte: {estatistica[1]}')
        print(f'Total de apostas: {estatistica[2]}')
        print(f'Apostas ganhas: {estatistica[3]}')
        print(f'Taxa de acerto: {estatistica[4]}%')
        print(f'Total investido: R${estatistica[5]}')
        print(f'Lucro: R${estatistica[6]}')
        print(f'ROI: {estatistica[7]}%')
        print(f'Odd média: {estatistica[8]}')
        print('----------------------------------------')

    banco_de_dados.commit()
    banco_de_dados.close()


def atualizar_estatisticas_por_campeonato():
    banco_de_dados = sqlite3.connect('bd_gestao_banca.db')
    cursor = banco_de_dados.cursor()

    cursor.execute("PRAGMA foreign_keys = ON")

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Apostas (
            Id INTEGER PRIMARY KEY AUTOINCREMENT,
            Data DATE NOT NULL,
            Casa_de_apostas TEXT NOT NULL,
            Esporte TEXT NOT NULL,
            Campeonato TEXT NOT NULL,
            Metodo_de_aposta TEXT NOT NULL,
            Status TEXT NOT NULL,
            Mandante TEXT NOT NULL,
            Visitante TEXT NOT NULL,
            Stake REAL NOT NULL,
            Odd REAL NOT NULL,
            Resultado TEXT NOT NULL,
            Lucro REAL NOT NULL,
            Observacao TEXT
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Estatisticas_por_Campeonato (
            Id INTEGER PRIMARY KEY AUTOINCREMENT,
            Campeonato TEXT NOT NULL,
            Total_de_apostas INTEGER NOT NULL,
            Apostas_Ganhas INTEGER NOT NULL,
            Taxa_de_acerto REAL NOT NULL,
            Total_investido REAL NOT NULL,
            Lucro REAL NOT NULL,
            ROI REAL NOT NULL,
            Odds_medias REAL NOT NULL
        )
    """)

    cursor.execute("""
        SELECT Campeonato FROM Estatisticas_por_Campeonato
    """)
    campeonatos_existentes = cursor.fetchall()
    campeonatos_existentes = [campeonato[0] for campeonato in campeonatos_existentes]

    cursor.execute("""
        SELECT
            Campeonato,
            COUNT(*) AS Total_de_apostas,
            SUM(CASE WHEN Resultado = 'ganha' THEN 1 ELSE 0 END) AS Apostas_Ganhas,
            ROUND(CAST(SUM(CASE WHEN Resultado = 'ganha' THEN 1 ELSE 0 END) AS REAL) / COUNT(*) * 100, 2) AS Taxa_de_acerto,
            ROUND(SUM(Stake), 2) AS Total_investido,
            ROUND(SUM(Lucro), 2) AS Lucro,
            ROUND(SUM(Lucro) / SUM(Stake) * 100, 2) AS ROI,
            ROUND(AVG(Odd), 2) AS Odds_medias
        FROM Apostas
        GROUP BY Campeonato
    """)
    estatisticas = cursor.fetchall()

    for estatistica in estatisticas:
        campeonato = estatistica[0]
        if campeonato not in campeonatos_existentes:
            cursor.execute("""
                INSERT INTO Estatisticas_por_Campeonato (Campeonato, Total_de_apostas, Apostas_Ganhas, Taxa_de_acerto, Total_investido, Lucro, ROI, Odds_medias)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """, estatistica)
        else:
            cursor.execute("""
                UPDATE Estatisticas_por_Campeonato
                SET Total_de_apostas=?, Apostas_Ganhas=?, Taxa_de_acerto=?, Total_investido=?, Lucro=?, ROI=?, Odds_medias=?
                WHERE Campeonato=?
            """, estatistica[1:] + (campeonato,))

    #imprimir tabela de estatisticas campeonato por campeonato
    cursor.execute("""
        SELECT * FROM Estatisticas_por_Campeonato
    """)
    estatisticas = cursor.fetchall()
    for estatistica in estatisticas:
        print(f'Campeonato: {estatistica[1]}')
        print(f'Total de apostas: {estatistica[2]}')
        print(f'Apostas ganhas: {estatistica[3]}')
        print(f'Taxa de acerto: {estatistica[4]}%')
        print(f'Total investido: R${estatistica[5]}')
        print(f'Lucro: R${estatistica[6]}')
        print(f'ROI: {estatistica[7]}%')
        print(f'Odd média: {estatistica[8]}')
        print('----------------------------------------')
    
    banco_de_dados.commit()
    banco_de_dados.close()


def atualizar_estatisticas_por_metodo_aposta():
    banco_de_dados = sqlite3.connect('bd_gestao_banca.db')
    cursor = banco_de_dados.cursor()

    cursor.execute("PRAGMA foreign_keys = ON")

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Apostas (
            Id INTEGER PRIMARY KEY AUTOINCREMENT,
            Data DATE NOT NULL,
            Casa_de_apostas TEXT NOT NULL,
            Esporte TEXT NOT NULL,
            Campeonato TEXT NOT NULL,
            Metodo_de_aposta TEXT NOT NULL,
            Status TEXT NOT NULL,
            Mandante TEXT NOT NULL,
            Visitante TEXT NOT NULL,
            Stake REAL NOT NULL,
            Odd REAL NOT NULL,
            Resultado TEXT NOT NULL,
            Lucro REAL NOT NULL,
            Observacao TEXT
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Estatisticas_por_Metodo_de_aposta (
            Id INTEGER PRIMARY KEY AUTOINCREMENT,
            Metodo_de_aposta TEXT NOT NULL,
            Total_de_apostas INTEGER NOT NULL,
            Apostas_Ganhas INTEGER NOT NULL,
            Taxa_de_acerto REAL NOT NULL,
            Total_investido REAL NOT NULL,
            Lucro REAL NOT NULL,
            ROI REAL NOT NULL,
            Odds_medias REAL NOT NULL
        )
    """)

    cursor.execute("""
        SELECT Metodo_de_aposta FROM Estatisticas_por_Metodo_de_aposta
    """)
    metodos_existentes = cursor.fetchall()
    metodos_existentes = [metodo[0] for metodo in metodos_existentes]

    cursor.execute("""
        SELECT
            Metodo_de_aposta,
            COUNT(*) AS Total_de_apostas,
            SUM(CASE WHEN Resultado = 'ganha' THEN 1 ELSE 0 END) AS Apostas_Ganhas,
            ROUND(CAST(SUM(CASE WHEN Resultado = 'ganha' THEN 1 ELSE 0 END) AS REAL) / COUNT(*) * 100, 2) AS Taxa_de_acerto,
            ROUND(SUM(Stake), 2) AS Total_investido,
            ROUND(SUM(Lucro), 2) AS Lucro,
            ROUND(SUM(Lucro) / SUM(Stake) * 100, 2) AS ROI,
            ROUND(AVG(Odd), 2) AS Odds_medias
        FROM Apostas
        GROUP BY Metodo_de_aposta
    """)
    estatisticas = cursor.fetchall()

    for estatistica in estatisticas:
        metodo = estatistica[0]
        if metodo not in metodos_existentes:
            cursor.execute("""
                INSERT INTO Estatisticas_por_Metodo_de_aposta (Metodo_de_aposta, Total_de_apostas, Apostas_Ganhas, Taxa_de_acerto, Total_investido, Lucro, ROI, Odds_medias)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """, estatistica)
        else:
            cursor.execute("""
                UPDATE Estatisticas_por_Metodo_de_aposta
                SET Total_de_apostas=?, Apostas_Ganhas=?, Taxa_de_acerto=?, Total_investido=?, Lucro=?, ROI=?, Odds_medias=?
                WHERE Metodo_de_aposta=?
            """, estatistica[1:] + (metodo,))
    
    #imprimir tabela de estatisticas metodo de aposta por metodo de aposta
    cursor.execute("""
        SELECT * FROM Estatisticas_por_Metodo_de_aposta
    """)
    estatisticas = cursor.fetchall()
    for estatistica in estatisticas:
        print(f'Método de aposta: {estatistica[1]}')
        print(f'Total de apostas: {estatistica[2]}')
        print(f'Apostas ganhas: {estatistica[3]}')
        print(f'Taxa de acerto: {estatistica[4]}%')
        print(f'Total investido: R${estatistica[5]}')
        print(f'Lucro: R${estatistica[6]}')
        print(f'ROI: {estatistica[7]}%')
        print(f'Odd média: {estatistica[8]}')
        print('----------------------------------------')
    
    banco_de_dados.commit()
    banco_de_dados.close()


def atualizar_estatisticas_por_casa_de_apostas():
    banco_de_dados = sqlite3.connect('bd_gestao_banca.db')
    cursor = banco_de_dados.cursor()

    cursor.execute("PRAGMA foreign_keys = ON")

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Apostas (
            Id INTEGER PRIMARY KEY AUTOINCREMENT,
            Data DATE NOT NULL,
            Casa_de_apostas TEXT NOT NULL,
            Esporte TEXT NOT NULL,
            Campeonato TEXT NOT NULL,
            Metodo_de_aposta TEXT NOT NULL,
            Status TEXT NOT NULL,
            Mandante TEXT NOT NULL,
            Visitante TEXT NOT NULL,
            Stake REAL NOT NULL,
            Odd REAL NOT NULL,
            Resultado TEXT NOT NULL,
            Lucro REAL NOT NULL,
            Observacao TEXT
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Estatisticas_por_Casa_de_apostas (
            Id INTEGER PRIMARY KEY AUTOINCREMENT,
            Casa_de_apostas TEXT NOT NULL,
            Total_de_apostas INTEGER NOT NULL,
            Apostas_Ganhas INTEGER NOT NULL,
            Taxa_de_acerto REAL NOT NULL,
            Total_investido REAL NOT NULL,
            Lucro REAL NOT NULL,
            ROI REAL NOT NULL,
            Odds_medias REAL NOT NULL
        )
    """)

    cursor.execute("""
        SELECT Casa_de_apostas FROM Estatisticas_por_Casa_de_apostas
    """)
    casas_existentes = cursor.fetchall()
    casas_existentes = [casa[0] for casa in casas_existentes]

    cursor.execute("""
        SELECT
            Casa_de_apostas,
            COUNT(*) AS Total_de_apostas,
            SUM(CASE WHEN Resultado = 'ganha' THEN 1 ELSE 0 END) AS Apostas_Ganhas,
            ROUND(CAST(SUM(CASE WHEN Resultado = 'ganha' THEN 1 ELSE 0 END) AS REAL) / COUNT(*) * 100, 2) AS Taxa_de_acerto,
            ROUND(SUM(Stake), 2) AS Total_investido,
            ROUND(SUM(Lucro), 2) AS Lucro,
            ROUND(SUM(Lucro) / SUM(Stake) * 100, 2) AS ROI,
            ROUND(AVG(Odd), 2) AS Odds_medias
        FROM Apostas
        GROUP BY Casa_de_apostas
    """)
    estatisticas = cursor.fetchall()

    for estatistica in estatisticas:
        casa = estatistica[0]
        if casa not in casas_existentes:
            cursor.execute("""
                INSERT INTO Estatisticas_por_Casa_de_apostas (Casa_de_apostas, Total_de_apostas, Apostas_Ganhas, Taxa_de_acerto, Total_investido, Lucro, ROI, Odds_medias)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """, estatistica)
        else:
            cursor.execute("""
                UPDATE Estatisticas_por_Casa_de_apostas
                SET Total_de_apostas=?, Apostas_Ganhas=?, Taxa_de_acerto=?, Total_investido=?, Lucro=?, ROI=?, Odds_medias=?
                WHERE Casa_de_apostas=?
            """, estatistica[1:] + (casa,))

    #imprimir tabela de estatisticas casa de apostas por casa de apostas
    cursor.execute("""
        SELECT * FROM Estatisticas_por_Casa_de_apostas
    """)
    estatisticas = cursor.fetchall()
    for estatistica in estatisticas:
        print(f'Casa de apostas: {estatistica[1]}')
        print(f'Total de apostas: {estatistica[2]}')
        print(f'Apostas ganhas: {estatistica[3]}')
        print(f'Taxa de acerto: {estatistica[4]}%')
        print(f'Total investido: R${estatistica[5]}')
        print(f'Lucro: R${estatistica[6]}')
        print(f'ROI: {estatistica[7]}%')
        print(f'Odd média: {estatistica[8]}')
        print('----------------------------------------')
    
    banco_de_dados.commit()
    banco_de_dados.close


def atualizar_estatisticas_por_mandante():
    banco_de_dados = sqlite3.connect('bd_gestao_banca.db')
    cursor = banco_de_dados.cursor()

    cursor.execute("PRAGMA foreign_keys = ON")

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Apostas (
            Id INTEGER PRIMARY KEY AUTOINCREMENT,
            Data DATE NOT NULL,
            Casa_de_apostas TEXT NOT NULL,
            Esporte TEXT NOT NULL,
            Campeonato TEXT NOT NULL,
            Metodo_de_aposta TEXT NOT NULL,
            Status TEXT NOT NULL,
            Mandante TEXT NOT NULL,
            Visitante TEXT NOT NULL,
            Stake REAL NOT NULL,
            Odd REAL NOT NULL,
            Resultado TEXT NOT NULL,
            Lucro REAL NOT NULL,
            Observacao TEXT
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Estatisticas_por_Mandante (
            Id INTEGER PRIMARY KEY AUTOINCREMENT,
            Mandante TEXT NOT NULL,
            Total_de_apostas INTEGER NOT NULL,
            Apostas_Ganhas INTEGER NOT NULL,
            Taxa_de_acerto REAL NOT NULL,
            Total_investido REAL NOT NULL,
            Lucro REAL NOT NULL,
            ROI REAL NOT NULL,
            Odds_medias REAL NOT NULL
        )
    """)

    cursor.execute("""
        SELECT Mandante FROM Estatisticas_por_Mandante
    """)
    mandantes_existentes = cursor.fetchall()
    mandantes_existentes = [mandante[0] for mandante in mandantes_existentes]

    cursor.execute("""
        SELECT
            Mandante,
            COUNT(*) AS Total_de_apostas,
            SUM(CASE WHEN Resultado = 'ganha' THEN 1 ELSE 0 END) AS Apostas_Ganhas,
            ROUND(CAST(SUM(CASE WHEN Resultado = 'ganha' THEN 1 ELSE 0 END) AS REAL) / COUNT(*) * 100, 2) AS Taxa_de_acerto,
            ROUND(SUM(Stake), 2) AS Total_investido,
            ROUND(SUM(Lucro), 2) AS Lucro,
            ROUND(SUM(Lucro) / SUM(Stake) * 100, 2) AS ROI,
            ROUND(AVG(Odd), 2) AS Odds_medias
        FROM Apostas
        GROUP BY Mandante
    """)
    estatisticas = cursor.fetchall()

    for estatistica in estatisticas:
        mandante = estatistica[0]
        if mandante not in mandantes_existentes:
            cursor.execute("""
                INSERT INTO Estatisticas_por_Mandante (Mandante, Total_de_apostas, Apostas_Ganhas, Taxa_de_acerto, Total_investido, Lucro, ROI, Odds_medias)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """, estatistica)
        else:
            cursor.execute("""
                UPDATE Estatisticas_por_Mandante
                SET Total_de_apostas=?, Apostas_Ganhas=?, Taxa_de_acerto=?, Total_investido=?, Lucro=?, ROI=?, Odds_medias=?
                WHERE Mandante=?
            """, estatistica[1:] + (mandante,))

    banco_de_dados.commit()
    banco_de_dados.close()
     

def atualizar_estatisticas_por_visitante():
    banco_de_dados = sqlite3.connect('bd_gestao_banca.db')
    cursor = banco_de_dados.cursor()

    cursor.execute("PRAGMA foreign_keys = ON")

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Apostas (
            Id INTEGER PRIMARY KEY AUTOINCREMENT,
            Data DATE NOT NULL,
            Casa_de_apostas TEXT NOT NULL,
            Esporte TEXT NOT NULL,
            Campeonato TEXT NOT NULL,
            Metodo_de_aposta TEXT NOT NULL,
            Status TEXT NOT NULL,
            Mandante TEXT NOT NULL,
            Visitante TEXT NOT NULL,
            Stake REAL NOT NULL,
            Odd REAL NOT NULL,
            Resultado TEXT NOT NULL,
            Lucro REAL NOT NULL,
            Observacao TEXT
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Estatisticas_por_Visitante (
            Id INTEGER PRIMARY KEY AUTOINCREMENT,
            Visitante TEXT NOT NULL,
            Total_de_apostas INTEGER NOT NULL,
            Apostas_Ganhas INTEGER NOT NULL,
            Taxa_de_acerto REAL NOT NULL,
            Total_investido REAL NOT NULL,
            Lucro REAL NOT NULL,
            ROI REAL NOT NULL,
            Odds_medias REAL NOT NULL
        )
    """)

    cursor.execute("""
        SELECT Visitante FROM Estatisticas_por_Visitante
    """)
    visitantes_existentes = cursor.fetchall()
    visitantes_existentes = [visitante[0] for visitante in visitantes_existentes]

    cursor.execute("""
        SELECT
            Visitante,
            COUNT(*) AS Total_de_apostas,
            SUM(CASE WHEN Resultado = 'ganha' THEN 1 ELSE 0 END) AS Apostas_Ganhas,
            ROUND(CAST(SUM(CASE WHEN Resultado = 'ganha' THEN 1 ELSE 0 END) AS REAL) / COUNT(*) * 100, 2) AS Taxa_de_acerto,
            ROUND(SUM(Stake), 2) AS Total_investido,
            ROUND(SUM(Lucro), 2) AS Lucro,
            ROUND(SUM(Lucro) / SUM(Stake) * 100, 2) AS ROI,
            ROUND(AVG(Odd), 2) AS Odds_medias
        FROM Apostas
        GROUP BY Visitante
    """)
    estatisticas = cursor.fetchall()

    for estatistica in estatisticas:
        visitante = estatistica[0]
        if visitante not in visitantes_existentes:
            cursor.execute("""
                INSERT INTO Estatisticas_por_Visitante (Visitante, Total_de_apostas, Apostas_Ganhas, Taxa_de_acerto, Total_investido, Lucro, ROI, Odds_medias)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """, estatistica)
        else:
            cursor.execute("""
                UPDATE Estatisticas_por_Visitante
                SET Total_de_apostas=?, Apostas_Ganhas=?, Taxa_de_acerto=?, Total_investido=?, Lucro=?, ROI=?, Odds_medias=?
                WHERE Visitante=?
            """, estatistica[1:] + (visitante,))

    banco_de_dados.commit()
    banco_de_dados.close()


def atualizar_estatisticas_por_resultado():
    banco_de_dados = sqlite3.connect('bd_gestao_banca.db')
    cursor = banco_de_dados.cursor()

    cursor.execute("PRAGMA foreign_keys = ON")

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Apostas (
            Id INTEGER PRIMARY KEY AUTOINCREMENT,
            Data DATE NOT NULL,
            Casa_de_apostas TEXT NOT NULL,
            Esporte TEXT NOT NULL,
            Campeonato TEXT NOT NULL,
            Metodo_de_aposta TEXT NOT NULL,
            Status TEXT NOT NULL,
            Mandante TEXT NOT NULL,
            Visitante TEXT NOT NULL,
            Stake REAL NOT NULL,
            Odd REAL NOT NULL,
            Resultado TEXT NOT NULL,
            Lucro REAL NOT NULL,
            Observacao TEXT
        )
    """)
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Estatisticas_por_Resultado (
            Id INTEGER PRIMARY KEY AUTOINCREMENT,
            Resultado TEXT NOT NULL,
            Total_de_apostas INTEGER NOT NULL,
            Apostas_Ganhas INTEGER NOT NULL,
            Taxa_de_acerto REAL NOT NULL,
            Total_investido REAL NOT NULL,
            Lucro REAL NOT NULL,
            ROI REAL NOT NULL,
            Odds_medias REAL NOT NULL
        )
    """)

    cursor.execute("""
        SELECT Resultado FROM Estatisticas_por_Resultado
    """)
    resultados_existentes = cursor.fetchall()
    resultados_existentes = [resultado[0] for resultado in resultados_existentes]

    cursor.execute("""
        SELECT
            Resultado,
            COUNT(*) AS Total_de_apostas,
            SUM(CASE WHEN Resultado = 'ganha' THEN 1 ELSE 0 END) AS Apostas_Ganhas,
            ROUND(CAST(SUM(CASE WHEN Resultado = 'ganha' THEN 1 ELSE 0 END) AS REAL) / COUNT(*) * 100, 2) AS Taxa_de_acerto,
            ROUND(SUM(Stake), 2) AS Total_investido,
            ROUND(SUM(Lucro), 2) AS Lucro,
            ROUND(SUM(Lucro) / SUM(Stake) * 100, 2) AS ROI,
            ROUND(AVG(Odd), 2) AS Odds_medias
        FROM Apostas
        GROUP BY Resultado
    """)
    estatisticas = cursor.fetchall()

    for estatistica in estatisticas:
        resultado = estatistica[0]
        if resultado not in resultados_existentes:
            cursor.execute("""
                INSERT INTO Estatisticas_por_Resultado (Resultado, Total_de_apostas, Apostas_Ganhas, Taxa_de_acerto, Total_investido, Lucro, ROI, Odds_medias)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """, estatistica)
        else:
            cursor.execute("""
                UPDATE Estatisticas_por_Resultado
                SET Total_de_apostas=?, Apostas_Ganhas=?, Taxa_de_acerto=?, Total_investido=?, Lucro=?, ROI=?, Odds_medias=?
                WHERE Resultado=?
            """, estatistica[1:] + (resultado,))

    banco_de_dados.commit()
    banco_de_dados.close()
  

def atualizar_estatisticas_por_stake():
    banco_de_dados = sqlite3.connect('bd_gestao_banca.db')
    cursor = banco_de_dados.cursor()

    cursor.execute("PRAGMA foreign_keys = ON")
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Apostas (
            Id INTEGER PRIMARY KEY AUTOINCREMENT,
            Data DATE NOT NULL,
            Casa_de_apostas TEXT NOT NULL,
            Esporte TEXT NOT NULL,
            Campeonato TEXT NOT NULL,
            Metodo_de_aposta TEXT NOT NULL,
            Status TEXT NOT NULL,
            Mandante TEXT NOT NULL,
            Visitante TEXT NOT NULL,
            Stake REAL NOT NULL,
            Odd REAL NOT NULL,
            Resultado TEXT NOT NULL,
            Lucro REAL NOT NULL,
            Observacao TEXT
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Estatisticas_por_Stake (
            Id INTEGER PRIMARY KEY AUTOINCREMENT,
            Stake TEXT NOT NULL,
            Total_de_apostas INTEGER NOT NULL,
            Apostas_Ganhas INTEGER NOT NULL,
            Taxa_de_acerto REAL NOT NULL,
            Total_investido REAL NOT NULL,
            Lucro REAL NOT NULL,
            ROI REAL NOT NULL,
            Odds_medias REAL NOT NULL
        )
    """)

    cursor.execute("""
        SELECT Stake FROM Estatisticas_por_Stake
    """)
    stakes_existentes = cursor.fetchall()
    stakes_existentes = [stake[0] for stake in stakes_existentes]

    cursor.execute("""
        SELECT
            Stake,
            COUNT(*) AS Total_de_apostas,
            SUM(CASE WHEN Resultado = 'ganha' THEN 1 ELSE 0 END) AS Apostas_Ganhas,
            ROUND(CAST(SUM(CASE WHEN Resultado = 'ganha' THEN 1 ELSE 0 END) AS REAL) / COUNT(*) * 100, 2) AS Taxa_de_acerto,
            ROUND(SUM(Stake), 2) AS Total_investido,
            ROUND(SUM(Lucro), 2) AS Lucro,
            ROUND(SUM(Lucro) / SUM(Stake) * 100, 2) AS ROI,
            ROUND(AVG(Odd), 2) AS Odds_medias
        FROM Apostas
        GROUP BY Stake
    """)
    estatisticas = cursor.fetchall()

    for estatistica in estatisticas:
        stake = estatistica[0]
        if stake not in stakes_existentes:
            cursor.execute("""
                INSERT INTO Estatisticas_por_Stake (Stake, Total_de_apostas, Apostas_Ganhas, Taxa_de_acerto, Total_investido, Lucro, ROI, Odds_medias)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """, estatistica)
        else:
            cursor.execute("""
                UPDATE Estatisticas_por_Stake
                SET Total_de_apostas=?, Apostas_Ganhas=?, Taxa_de_acerto=?, Total_investido=?, Lucro=?, ROI=?, Odds_medias=?
                WHERE Stake=?
            """, estatistica[1:] + (stake,))

    banco_de_dados.commit()
    banco_de_dados.close()

def atualizar_estatisticas_por_status():
    banco_de_dados = sqlite3.connect('bd_gestao_banca.db')
    cursor = banco_de_dados.cursor()

    cursor.execute("PRAGMA foreign_keys = ON")

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Apostas (
            Id INTEGER PRIMARY KEY AUTOINCREMENT,
            Data DATE NOT NULL,
            Casa_de_apostas TEXT NOT NULL,
            Esporte TEXT NOT NULL,
            Campeonato TEXT NOT NULL,
            Metodo_de_aposta TEXT NOT NULL,
            Status TEXT NOT NULL,
            Mandante TEXT NOT NULL,
            Visitante TEXT NOT NULL,
            Stake REAL NOT NULL,
            Odd REAL NOT NULL,
            Resultado TEXT NOT NULL,
            Lucro REAL NOT NULL,
            Observacao TEXT
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Status (
            Id INTEGER PRIMARY KEY AUTOINCREMENT,
            Status TEXT NOT NULL,
            Total_de_apostas INTEGER NOT NULL,
            Apostas_Ganhas INTEGER NOT NULL,
            Taxa_de_acerto REAL NOT NULL,
            Total_investido REAL NOT NULL,
            Lucro REAL NOT NULL,
            ROI REAL NOT NULL,
            Odds_medias REAL NOT NULL
        )
    """)

    cursor.execute("""
        SELECT Status FROM Status
    """)
    status_existentes = cursor.fetchall()
    status_existentes = [status[0] for status in status_existentes]

    cursor.execute("""
        SELECT
            Status,
            COUNT(*) AS Total_de_apostas,
            SUM(CASE WHEN Resultado = 'ganha' THEN 1 ELSE 0 END) AS Apostas_Ganhas,
            ROUND(CAST(SUM(CASE WHEN Resultado = 'ganha' THEN 1 ELSE 0 END) AS REAL) / COUNT(*) * 100, 2) AS Taxa_de_acerto,
            ROUND(SUM(Stake), 2) AS Total_investido,
            ROUND(SUM(Lucro), 2) AS Lucro,
            ROUND(SUM(Lucro) / SUM(Stake) * 100, 2) AS ROI,
            ROUND(AVG(Odd), 2) AS Odds_medias
        FROM Apostas
        GROUP BY Status
    """)
    estatisticas = cursor.fetchall()

    for estatistica in estatisticas:
        status = estatistica[0]
        if status not in status_existentes:
            cursor.execute("""
                INSERT INTO Status (Status, Total_de_apostas, Apostas_Ganhas, Taxa_de_acerto, Total_investido, Lucro, ROI, Odds_medias)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """, estatistica)
        else:
            cursor.execute("""
                UPDATE Status
                SET Total_de_apostas=?, Apostas_Ganhas=?, Taxa_de_acerto=?, Total_investido=?, Lucro=?, ROI=?, Odds_medias=?
                WHERE Status=?
            """, estatistica[1:] + (status,))

    banco_de_dados.commit()
    banco_de_dados.close()


def atualizar_estatisticas_banca():
    banco_de_dados = sqlite3.connect('bd_gestao_banca.db')
    cursor = banco_de_dados.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Apostas (
            Id INTEGER PRIMARY KEY,
            Data DATE NOT NULL,
            Casa_de_apostas TEXT NOT NULL,
            Esporte TEXT NOT NULL,
            Campeonato TEXT NOT NULL,
            Metodo_de_aposta TEXT NOT NULL,
            Status TEXT NOT NULL,
            Mandante TEXT NOT NULL,
            Visitante TEXT NOT NULL,
            Stake REAL NOT NULL,
            Odd REAL NOT NULL,
            Resultado TEXT NOT NULL,
            Lucro REAL NOT NULL,
            Observacao TEXT
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Estatisticas_Banca (
            Id INTEGER PRIMARY KEY AUTOINCREMENT,
            Banca_inicial REAL NOT NULL,
            Banca_atual REAL NOT NULL,
            Total_de_apostas INTEGER NOT NULL,
            Apostas_Ganhas INTEGER NOT NULL,
            Taxa_de_acerto REAL NOT NULL,
            Total_investido REAL NOT NULL,
            Lucro REAL NOT NULL,
            ROI REAL NOT NULL,
            Odds_medias REAL NOT NULL
        )
    """)

    cursor.execute("""
        SELECT COUNT(*) FROM Apostas
    """)
    total_de_apostas = cursor.fetchone()[0]

    cursor.execute("""
        SELECT
            SUM(CASE WHEN Resultado = 'ganha' THEN 1 ELSE 0 END) AS Apostas_Ganhas,
            ROUND(CAST(SUM(CASE WHEN Resultado = 'ganha' THEN 1 ELSE 0 END) AS REAL) / COUNT(*) * 100, 2) AS Taxa_de_acerto,
            ROUND(SUM(Stake), 2) AS Total_investido,
            ROUND(SUM(Lucro), 2) AS Lucro,
            ROUND(SUM(Lucro) / SUM(Stake) * 100, 2) AS ROI,
            ROUND(AVG(Odd), 2) AS Odds_medias
        FROM Apostas
    """)
    estatisticas = cursor.fetchone()

    banca_inicial = 50.0
    banca_atual = banca_inicial + estatisticas[3]

    dados_banca = (banca_inicial, banca_atual, total_de_apostas) + estatisticas

    cursor.execute("""
        INSERT OR REPLACE INTO Estatisticas_Banca (Id, Banca_inicial, Banca_atual, Total_de_apostas, Apostas_Ganhas, Taxa_de_acerto, Total_investido, Lucro, ROI, Odds_medias)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (1,) + dados_banca)
    
    #Printando estatisticas da banca
    cursor.execute("""
        SELECT * FROM Estatisticas_Banca
    """)
        
    estatisticas_banca = cursor.fetchall()
    for estatistica_banca in estatisticas_banca:
        print(f"Banca inicial: {estatistica_banca[1]}")
        print(f"Banca atual: {estatistica_banca[2]}")
        print(f"Total de apostas: {estatistica_banca[3]}")
        print(f"Apostas ganhas: {estatistica_banca[4]}")
        print(f"Taxa de acerto: {estatistica_banca[5]}%")
        print(f"Total investido: {estatistica_banca[6]}")
        print(f"Lucro: {estatistica_banca[7]}")
        print(f"ROI: {estatistica_banca[8]}%")
        print(f"Odds medias: {estatistica_banca[9]}")
        print("")
    
    banco_de_dados.commit()
    banco_de_dados.close()



def gerar_grafico_estatisticas_por_data():
    banco_de_dados = sqlite3.connect('bd_gestao_banca.db')
    cursor = banco_de_dados.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Estatisticas_por_Data (
            Id INTEGER PRIMARY KEY,
            Data DATE NOT NULL,
            Total_de_apostas INTEGER NOT NULL,
            Apostas_Ganhas INTEGER NOT NULL,
            Taxa_de_acerto REAL NOT NULL,
            Total_investido REAL NOT NULL,
            Lucro REAL NOT NULL,
            ROI REAL NOT NULL,
            Odds_medias REAL NOT NULL
        )
    """)

    # Consulta SQL para obter os dados da tabela
    cursor.execute("""
        SELECT Data, Lucro
        FROM Estatisticas_por_Data
        ORDER BY Data
    """)

    # Extrai os dados do cursor
    data = []
    lucro = []
    for row in cursor.fetchall():
        data.append(row[0])
        lucro.append(row[1])

    # Fecha a conexão com o banco de dados
    banco_de_dados.close()

    # Cria o gráfico de barras interativo
    fig = go.Figure(data=go.Bar(x=data, y=lucro))

    # Configurações do layout
    fig.update_layout(
        title='Lucro ao longo do tempo',
        xaxis_title='Data',
        yaxis_title='Lucro',
        xaxis_tickangle=-45,
        hovermode='closest'
    )

    # Configurações do hover
    fig.update_traces(hovertemplate='Lucro: %{y}')

    # Exibe o gráfico interativo
    fig.show()

# Chamada da função para gerar o gráfico



def gerar_grafico_estatisticas_por_esporte():
    banco_de_dados = sqlite3.connect('bd_gestao_banca.db')
    cursor = banco_de_dados.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Estatisticas_por_Esporte (
            Id INTEGER PRIMARY KEY AUTOINCREMENT,
            Esporte TEXT NOT NULL,
            Total_de_apostas INTEGER NOT NULL,
            Apostas_Ganhas INTEGER NOT NULL,
            Taxa_de_acerto REAL NOT NULL,
            Total_investido REAL NOT NULL,
            Lucro REAL NOT NULL,
            ROI REAL NOT NULL,
            Odds_medias REAL NOT NULL
        )
    """)

    # Consulta SQL para obter os dados da tabela
    cursor.execute("""
        SELECT Esporte, Lucro
        FROM Estatisticas_por_Esporte
        ORDER BY Lucro DESC
    """)

    # Extrai os dados do cursor
    esportes = []
    lucros = []
    for row in cursor.fetchall():
        esportes.append(row[0])
        lucros.append(row[1])

    # Fecha a conexão com o banco de dados
    banco_de_dados.close()

    # Cria o gráfico de barras interativo
    fig = go.Figure(data=go.Bar(x=esportes, y=lucros))

    # Configurações do layout
    fig.update_layout(
        title='Lucro por Esporte',
        xaxis_title='Esporte',
        yaxis_title='Lucro',
        xaxis_tickangle=-45,
        hovermode='closest'
    )

    # Configurações do hover
    fig.update_traces(hovertemplate='Lucro: %{y}')

    # Exibe o gráfico interativo
    fig.show()



def gerar_grafico_estatisticas_por_campeonato():
    banco_de_dados = sqlite3.connect('bd_gestao_banca.db')
    cursor = banco_de_dados.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Estatisticas_por_Campeonato (
            Id INTEGER PRIMARY KEY AUTOINCREMENT,
            Campeonato TEXT NOT NULL,
            Total_de_apostas INTEGER NOT NULL,
            Apostas_Ganhas INTEGER NOT NULL,
            Taxa_de_acerto REAL NOT NULL,
            Total_investido REAL NOT NULL,
            Lucro REAL NOT NULL,
            ROI REAL NOT NULL,
            Odds_medias REAL NOT NULL
        )
    """)

    # Consulta SQL para obter os dados da tabela
    cursor.execute("""
        SELECT Campeonato, Lucro
        FROM Estatisticas_por_Campeonato
        ORDER BY Lucro DESC
    """)

    # Extrai os dados do cursor
    campeonatos = []
    lucros = []
    for row in cursor.fetchall():
        campeonatos.append(row[0])
        lucros.append(row[1])

    # Fecha a conexão com o banco de dados
    banco_de_dados.close()

    # Cria o gráfico de barras interativo
    fig = go.Figure(data=go.Bar(x=campeonatos, y=lucros))

    # Configurações do layout
    fig.update_layout(
        title='Lucro por Campeonato',
        xaxis_title='Campeonato',
        yaxis_title='Lucro',
        xaxis_tickangle=-45,
        hovermode='closest'
    )

    # Configurações do hover
    fig.update_traces(hovertemplate='Lucro: %{y}')

    # Exibe o gráfico interativo
    fig.show()


def gerar_grafico_estatisticas_por_metodo_de_aposta():
    banco_de_dados = sqlite3.connect('bd_gestao_banca.db')
    cursor = banco_de_dados.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Estatisticas_por_Metodo_de_aposta (
            Id INTEGER PRIMARY KEY AUTOINCREMENT,
            Metodo_de_aposta TEXT NOT NULL,
            Total_de_apostas INTEGER NOT NULL,
            Apostas_Ganhas INTEGER NOT NULL,
            Taxa_de_acerto REAL NOT NULL,
            Total_investido REAL NOT NULL,
            Lucro REAL NOT NULL,
            ROI REAL NOT NULL,
            Odds_medias REAL NOT NULL
        )
    """)

    # Consulta SQL para obter os dados da tabela
    cursor.execute("""
        SELECT Metodo_de_aposta, Lucro
        FROM Estatisticas_por_Metodo_de_aposta
        ORDER BY Lucro DESC
    """)

    # Extrai os dados do cursor
    metodos = []
    lucros = []
    for row in cursor.fetchall():
        metodos.append(row[0])
        lucros.append(row[1])

    # Fecha a conexão com o banco de dados
    banco_de_dados.close()

    # Cria o gráfico de barras interativo
    fig = go.Figure(data=go.Bar(x=metodos, y=lucros))

    # Configurações do layout
    fig.update_layout(
        title='Lucro por Método de Aposta',
        xaxis_title='Método de Aposta',
        yaxis_title='Lucro',
        xaxis_tickangle=-45,
        hovermode='closest'
    )

    # Configurações do hover
    fig.update_traces(hovertemplate='Lucro: %{y}')

    # Exibe o gráfico interativo
    fig.show()



import sqlite3
import pandas as pd
from statsmodels.tsa.arima.model import ARIMA

def prever_lucro_por_data():
    # Conectar ao banco de dados e obter os dados da tabela Estatisticas_por_Data
    banco_de_dados = sqlite3.connect('bd_gestao_banca.db')
    cursor = banco_de_dados.cursor()
    cursor.execute("PRAGMA foreign_keys = ON")
    cursor.execute("""
        SELECT Data, Lucro
        FROM Estatisticas_por_Data
        ORDER BY Data
    """)
    # Ler os dados diretamente do cursor
    dados = cursor.fetchall()
    # Fechar a conexão com o banco de dados
    banco_de_dados.close()
    
    # Colocar os dados em um DataFrame do pandas
    dados_df = pd.DataFrame(dados, columns=['Data', 'Lucro'])
    # Converter a coluna 'Data' para datetime
    dados_df['Data'] = pd.to_datetime(dados_df['Data'])

    # Selecionar as datas já existentes na tabela Estatisticas_por_Data
    datas_existentes = set(dados_df['Data'])
    
    # Gerar as datas para a previsão
    data_inicial = dados_df['Data'].max() + pd.DateOffset(days=1)
    datas_previsao = pd.to_datetime([data_inicial + pd.DateOffset(days=i) for i in range(31)])

    # Filtrar as datas que não estão na tabela Estatisticas_por_Data
    datas_novas = [data for data in datas_previsao if data not in datas_existentes]

    # Se não houver novas datas, encerrar a função
    if not datas_novas:
        print("Não há novas datas para adicionar.")
        return

    # Selecionar a coluna de lucro
    lucro = dados_df['Lucro']

    # Cria o modelo ARIMA
    modelo = ARIMA(lucro, order=(1, 1, 1))  # (p, d, q)

    # Treina o modelo
    modelo_fit = modelo.fit()

    # Faz a previsão para as datas novas
    previsao = modelo_fit.predict(start=len(lucro), end=len(lucro) + len(datas_novas) - 1, typ='levels')

    # Criar um DataFrame com as datas e a previsão
    previsao_df = pd.DataFrame({'Data': datas_novas, 'Lucro': previsao})

    # Salvar os dados da previsão em uma nova tabela no banco de dados
    banco_de_dados = sqlite3.connect('bd_gestao_banca.db')
    cursor = banco_de_dados.cursor()

    cursor.execute("DROP TABLE IF EXISTS Previsao_Lucro")

    # Criar a tabela Previsao_Lucro se ela não existir
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Previsao_Lucro (
        Data DATE PRIMARY KEY,
        Lucro NUMERIC(10, 2)
    )
""")


    # Inserir os dados na tabela Previsao_Lucro
    for data, lucro in previsao_df.itertuples(index=False):
        cursor.execute("INSERT INTO Previsao_Lucro (Data, Lucro) VALUES (?, ROUND(?, 2))", (data.date(), lucro))

    # Commit para salvar as alterações no banco de dados
    banco_de_dados.commit()

    # Fechar a conexão com o banco de dados
    banco_de_dados.close()

    # Exibir a previsão
    for data, lucro in previsao_df.itertuples(index=False):
        print(f"{data.date()}: R$ {lucro:.2f}")
        
    



    


   
        
def deletar_aposta():
        banco_de_dados = sqlite3.connect('bd_gestao_banca.db')
        cursor = banco_de_dados.cursor()
        cursor.execute("PRAGMA foreign_keys = ON")

        # Get all bets from the database
        cursor.execute("SELECT * FROM Apostas")

        # Create a list of bets
        bets = []
        for row in cursor:
            bets.append(row)

        # Print all bets
        for bet in bets:
            print(bet)

        # Choose a bet by id
        id = input("Enter the id of the bet you want to delete: ")

        # Delete the bet from the database
        cursor.execute("DELETE FROM Apostas WHERE Id=?", (id,))

        # Commit the changes to the database
        banco_de_dados.commit()

        # Close the connection to the database
        banco_de_dados.close()
        
        
def listar_apostas():
    banco_de_dados = sqlite3.connect('bd_gestao_banca.db')
    cursor = banco_de_dados.cursor()

    # Get all bets from the database
    cursor.execute("SELECT * FROM Apostas")

    # Create a list of bets
    bets = []
    for row in cursor:
        bets.append(row)

    # Print all bets
    for bet in bets:
        print(bet)

    # Close the connection to the database
    banco_de_dados.close()
        
        


'''
#Confirir o lucro total de todas as apostas
def lucro_total():
    banco_de_dados = sqlite3.connect('bd_gestao_banca.db')
    cursor = banco_de_dados.cursor()

    # Get all bets from the database
    cursor.execute("SELECT * FROM Apostas")

    # Create a list of bets
    bets = []
    for row in cursor:
        bets.append(row)

    # Print all bets
    for bet in bets:
        print(bet)

    # Close the connection to the database
    banco_de_dados.close()
    banca_inical = 50
    lucro_total = 0
    for bet in bets:
        lucro_total += bet[12]
    
    lucro_total = round(lucro_total, 2)
    banca_final = banca_inical + lucro_total
    print(f'O lucro total é de R${lucro_total}')
    print(f'A banca final é de R${banca_final}')
    
    '''


    
    
                