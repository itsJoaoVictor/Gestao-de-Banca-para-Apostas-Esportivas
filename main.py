from Banco_Dados import criar_tabelas
import sqlite3
from classes import Aposta, deletar_aposta, listar_apostas, alterar_aposta_pendente, alterar_aposta_finalizada,atualizar_estatisticas_por_data,atualizar_estatisticas_por_esporte,atualizar_estatisticas_por_campeonato,atualizar_estatisticas_por_metodo_aposta,atualizar_estatisticas_por_casa_de_apostas,atualizar_estatisticas_por_mandante,atualizar_estatisticas_por_visitante,atualizar_estatisticas_por_resultado,atualizar_estatisticas_por_stake,atualizar_estatisticas_por_status,atualizar_estatisticas_banca,gerar_grafico_estatisticas_por_data,gerar_grafico_estatisticas_por_esporte,gerar_grafico_estatisticas_por_campeonato,gerar_grafico_estatisticas_por_metodo_de_aposta,prever_lucro_por_data
import time 

def main():
    print("\n")
    criar_tabelas()
    print("Seja Bem Vindo ao programa de Gestão de Banca e Estatísticas de Apostas Esportivas!")
    print("Escolha uma das opções abaixo:")
    print("1 - Cadastrar uma aposta")
    print("2 - Editar uma aposta")
    print("3 - Deletar uma aposta")
    print("4 - Listar todas as apostas")
    print("5 - Estatísticas")
    print("6 - Gráficos")
    print("7 - Previsão de Banca")
    

    opcao = int(input("Digite a opção desejada: "))
    if opcao == 1:
        data = input("Digite a data da aposta: ")
        casa_de_apostas = input("Digite a casa de apostas: ")
        esporte = input("Digite o esporte: ")
        campeonato = input("Digite o campeonato: ")
        metodo_de_aposta = input("Digite o método de aposta: ")
        status = input("Digite o status da aposta: ")
        mandante = input("Digite o mandante: ")
        visitante = input("Digite o visitante: ")
        stake = float(input("Digite a stake: "))
        odd = float(input("Digite a odd: "))
        print("Selecione o resultado da aposta:")
        print("1 - Ganha")
        print("2 - Perdida")
        print("3 - Cancelada")
        print("4 - Pendente")
        print("5 - Meio ganha")
        print("6 - Meio perdida")
        resultado = int(input("Digite a opção desejada: "))
        if resultado == 1:
            resultado = "ganha"
            lucro = (odd-1)*stake
        elif resultado == 2:
            resultado = "perdida"
            lucro = stake*(-1)
        elif resultado == 3:
            resultado = "cancelada"
            lucro = 0
        elif resultado == 4:
            resultado = "pendente"
            lucro = 0
        elif resultado == 5:
            resultado = "meio ganha"
            lucro = (odd-1)*stake*(1/2)
        elif resultado == 6:
            resultado = "meio perdida"
            lucro = stake*(-1)*(1/2)
        else:
            print("Opção inválida!\n")
            
            main()
            
        # o lucro tem que ter 2 casas decimais
        lucro = round(lucro, 2)
 
        observacao = input("Digite uma observação: ")
        aposta = Aposta(data, casa_de_apostas, esporte, campeonato, metodo_de_aposta, status, mandante, visitante, stake, odd, resultado, lucro, observacao)
        aposta.cadastrar_aposta()
        print("\n")
        main()
        
    elif opcao == 2:
        print("Deseja editar uma aposta Pendente ou uma aposta Finalizada?")
        print("1 - Pendente")
        print("2 - Finalizada")
        opcao = int(input("Digite a opção desejada: "))
        if opcao == 1:
            alterar_aposta_pendente()
            print("\n")
            main()
        elif opcao == 2:
            alterar_aposta_finalizada()
            print("\n")
            main()
        else:
            print("Opção inválida!")
            main()
        
        
    elif opcao == 3:
        deletar_aposta()
        print("\n")
        main()
        
    elif opcao == 4:
        listar_apostas()
        print("\n")
        main()
    
    elif opcao == 5:
        atualizar_estatisticas_por_mandante()
        atualizar_estatisticas_por_visitante()
        atualizar_estatisticas_por_resultado()
        atualizar_estatisticas_por_stake()
        print("\n")
        atualizar_estatisticas_banca()
        
        #Esperar 2 segundos
        time.sleep(2)
        print("\nEstatiticas por data \n")
        atualizar_estatisticas_por_data()
        print("\n")
        #Esperar 2 segundos
        time.sleep(2)
        print("Estatiticas por Esporte \n")
        atualizar_estatisticas_por_esporte()
        print("\n")
        #Esperar 2 segundos
        time.sleep(2)
        print("Estatiticas por Campeonato \n")
        atualizar_estatisticas_por_campeonato()
        print("\n")
        #Esperar 2 segundos
        time.sleep(2)
        print("Estatiticas por Método de Aposta \n")
        atualizar_estatisticas_por_metodo_aposta()
        print("\n")
        #Esperar 2 segundos
        time.sleep(2)
        print("Estatiticas por Casa de Apostas \n")
        atualizar_estatisticas_por_casa_de_apostas()
        print("\n")
        #Esperar 2 segundos
        time.sleep(2)        
        main()
    
    elif opcao == 6:
        gerar_grafico_estatisticas_por_data()
        gerar_grafico_estatisticas_por_esporte()
        gerar_grafico_estatisticas_por_campeonato()
        gerar_grafico_estatisticas_por_metodo_de_aposta()
        main()
    
    elif opcao == 7:
        prever_lucro_por_data()
        print("\n")
        main()
        
        
    else:
        print("Opção inválida!")
        main()
        
        
if __name__ == '__main__':
    main()