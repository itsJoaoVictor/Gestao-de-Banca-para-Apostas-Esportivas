import sqlite3


def criar_tabelas():
        try:
                # Criação da base de dados
                banco_de_dados = sqlite3.connect('bd_gestao_banca.db')
                cursor = banco_de_dados.cursor()

                # Criação da tabela
                cursor.execute("""
                CREATE TABLE IF NOT EXISTS Apostas (
                        Id INTEGER NOT NULL PRIMARY KEY ,
                        Data DATE NOT NULL,
                        Casa_de_apostas TEXT NOT NULL,
                        Esporte TEXT NOT NULL,
                        Campeonato TEXT NOT NULL,
                        Metodo_de_aposta TEXT NOT NULL,
                        status TEXT NOT NULL,
                        Mandante TEXT NOT NULL,
                        Visitante TEXT NOT NULL,
                        Stake REAL NOT NULL,
                        Odd REAL NOT NULL,
                        Resultado TEXT NOT NULL,
                        Lucro REAL NOT NULL,
                        Observacao TEXT
                );
                """)

                #Criar tabela Estatisticas_por_Data contendo Data,Total de apostas,Apostas Ganhas,Taxa de acerto,Total investido $,Lucro,ROI%,Odds médias
                cursor.execute("""
                CREATE TABLE IF NOT EXISTS Estatisticas_por_Data (
                        Id INTEGER NOT NULL PRIMARY KEY ,
                        Data DATE NOT NULL,
                        Total_de_apostas INTEGER NOT NULL,
                        Apostas_Ganhas INTEGER NOT NULL,
                        Taxa_de_acerto REAL NOT NULL,
                        Total_investido REAL NOT NULL,
                        Lucro REAL NOT NULL,
                        ROI REAL NOT NULL,
                        Odds_medias REAL NOT NULL
                );
                """)
                #Criar tabela Estatisticas_por_Esporte contendo Esporte,Total de apostas,Apostas Ganhas,Taxa de acerto,Total investido $,Lucro,ROI%,Odds médias
                cursor.execute("""
                CREATE TABLE IF NOT EXISTS Estatisticas_por_Esporte (
                        Id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                        Esporte TEXT NOT NULL,
                        Total_de_apostas INTEGER NOT NULL,
                        Apostas_Ganhas INTEGER NOT NULL,
                        Taxa_de_acerto REAL NOT NULL,
                        Total_investido REAL NOT NULL,
                        Lucro REAL NOT NULL,
                        ROI REAL NOT NULL,
                        Odds_medias REAL NOT NULL
                );
                """)
                #Criar tabela Estatisticas_por_Campeonato contendo Campeonato,Total de apostas,Apostas Ganhas,Taxa de acerto,Total investido $,Lucro,ROI%,Odds médias
                cursor.execute("""
                CREATE TABLE IF NOT EXISTS Estatisticas_por_Campeonato (
                        Id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                        Campeonato TEXT NOT NULL,
                        Total_de_apostas INTEGER NOT NULL,
                        Apostas_Ganhas INTEGER NOT NULL,
                        Taxa_de_acerto REAL NOT NULL,
                        Total_investido REAL NOT NULL,
                        Lucro REAL NOT NULL,
                        ROI REAL NOT NULL,
                        Odds_medias REAL NOT NULL
                );
                """)
                #Criar tabela Estatisticas_por_Metodo_de_aposta contendo Metodo_de_aposta,Total de apostas,Apostas Ganhas,Taxa de acerto,Total investido $,Lucro,ROI%,Odds médias
                cursor.execute("""
                CREATE TABLE IF NOT EXISTS Estatisticas_por_Metodo_de_aposta (
                        Id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                        Metodo_de_aposta TEXT NOT NULL,
                        Total_de_apostas INTEGER NOT NULL,
                        Apostas_Ganhas INTEGER NOT NULL,
                        Taxa_de_acerto REAL NOT NULL,
                        Total_investido REAL NOT NULL,
                        Lucro REAL NOT NULL,
                        ROI REAL NOT NULL,
                        Odds_medias REAL NOT NULL
                );
                """)
                #Criar tabela Estatisticas_por_Casa_de_apostas contendo Casa_de_apostas,Total de apostas,Apostas Ganhas,Taxa de acerto,Total investido $,Lucro,ROI%,Odds médias
                cursor.execute("""
                CREATE TABLE IF NOT EXISTS Estatisticas_por_Casa_de_apostas (
                        Id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                        Casa_de_apostas TEXT NOT NULL,
                        Total_de_apostas INTEGER NOT NULL,
                        Apostas_Ganhas INTEGER NOT NULL,
                        Taxa_de_acerto REAL NOT NULL,
                        Total_investido REAL NOT NULL,
                        Lucro REAL NOT NULL,
                        ROI REAL NOT NULL,
                        Odds_medias REAL NOT NULL
                );
                """)

                #Criar tabela Estatisticas_por_Mandante contendo Mandante,Total de apostas,Apostas Ganhas,Taxa de acerto,Total investido $,Lucro,ROI%,Odds médias
                cursor.execute("""
                CREATE TABLE IF NOT EXISTS Estatisticas_por_Mandante (
                        Id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                        Mandante TEXT NOT NULL,
                        Total_de_apostas INTEGER NOT NULL,
                        Apostas_Ganhas INTEGER NOT NULL,
                        Taxa_de_acerto REAL NOT NULL,
                        Total_investido REAL NOT NULL,
                        Lucro REAL NOT NULL,
                        ROI REAL NOT NULL,
                        Odds_medias REAL NOT NULL
                );
                """)
                #Criar tabela Estatisticas_por_Visitante contendo Visitante,Total de apostas,Apostas Ganhas,Taxa de acerto,Total investido $,Lucro,ROI%,Odds médias
                cursor.execute("""
                CREATE TABLE IF NOT EXISTS Estatisticas_por_Visitante (
                        Id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                        Visitante TEXT NOT NULL,
                        Total_de_apostas INTEGER NOT NULL,
                        Apostas_Ganhas INTEGER NOT NULL,
                        Taxa_de_acerto REAL NOT NULL,
                        Total_investido REAL NOT NULL,
                        Lucro REAL NOT NULL,
                        ROI REAL NOT NULL,
                        Odds_medias REAL NOT NULL
                );
                """)

                #Criar tabela Estatisticas_por_Resultado contendo Resultado,Total de apostas,Apostas Ganhas,Taxa de acerto,Total investido $,Lucro,ROI%,Odds médias
                cursor.execute("""
                CREATE TABLE IF NOT EXISTS Estatisticas_por_Resultado (
                        Id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                        Resultado TEXT NOT NULL,
                        Total_de_apostas INTEGER NOT NULL,
                        Apostas_Ganhas INTEGER NOT NULL,
                        Taxa_de_acerto REAL NOT NULL,
                        Total_investido REAL NOT NULL,
                        Lucro REAL NOT NULL,
                        ROI REAL NOT NULL,
                        Odds_medias REAL NOT NULL
                );
                """)

                #Criar tabela Estatisticas_por_Stake contendo Stake,Total de apostas,Apostas Ganhas,Taxa de acerto,Total investido $,Lucro,ROI%,Odds médias
                cursor.execute("""
                CREATE TABLE IF NOT EXISTS Estatisticas_por_Stake (
                        Id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                        Stake TEXT NOT NULL,
                        Total_de_apostas INTEGER NOT NULL,
                        Apostas_Ganhas INTEGER NOT NULL,
                        Taxa_de_acerto REAL NOT NULL,
                        Total_investido REAL NOT NULL,
                        Lucro REAL NOT NULL,
                        ROI REAL NOT NULL,
                        Odds_medias REAL NOT NULL
                );
                """)
                
                cursor.execute("""
                CREATE TABLE IF NOT EXISTS Status (
                        Id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                        Status TEXT NOT NULL,
                        Total_de_apostas INTEGER NOT NULL,
                        Apostas_Ganhas INTEGER NOT NULL,
                        Taxa_de_acerto REAL NOT NULL,
                        Total_investido REAL NOT NULL,
                        Lucro REAL NOT NULL,
                        ROI REAL NOT NULL,
                        Odds_medias REAL NOT NULL
                );
                """)
                
                #Criar tabela Estatisticas_Banca contendo Banca inicial, Banca Atual,Total de apostas,Apostas Ganhas,Taxa de acerto,Total investido $,Lucro,ROI%,Odds médias
                cursor.execute("""
                CREATE TABLE IF NOT EXISTS Estatisticas_Banca (
                        Id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                        Banca_inicial REAL NOT NULL,
                        Banca_atual REAL NOT NULL,
                        Total_de_apostas INTEGER NOT NULL,
                        Apostas_Ganhas INTEGER NOT NULL,
                        Taxa_de_acerto REAL NOT NULL,
                        Total_investido REAL NOT NULL,
                        Lucro REAL NOT NULL,
                        ROI REAL NOT NULL,
                        Odds_medias REAL NOT NULL
                );
                """)
                
                
                
                #fechar a função de criar tabelas 
                cursor.close()
                #fechar a conexão com o banco de dados
                banco_de_dados.close()
                
                
        except:
                #printar mensagem de erro
                print("Erro ao criar tabelas!")
                


