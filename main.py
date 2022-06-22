from time import sleep
from bet import Bet
from helper import Arquivo, Informacoes, Listar, Graficos

def main () -> None:
    menu()
    
def menu () -> None:
    print('Bem vindo ao sistema de Gestão de Banca')
    print('\n')
    print('Selecione uma das opções abaixo:')
    print('1 - Listar Esportes')
    print('2 - Listar Campeonatos')
    print('3 - Listar Mercados')
    print('4 - Cadastrar aposta')
    print('5 - Listar Apostas')
    print('6 - Detalhamendo mensal')
    print('7 - Detalhamento diario')
    print('8 - Detalhamento por esporte')
    print('9 - Detalhamento por campeonato')
    print('10 - Detalhamento por mercado')
    print('11 Exibir Gráficos')
    print('12 - Sair')
    
    opcao = int(input('\nDigite a opção desejada: '))
    
    #opção 1 - listar esportes
    if opcao == 1:
        arquivo = Arquivo('gestao_banca.csv')
        dataframe = arquivo.leitura()
        listar = Listar(dataframe)
        listar.esportes()
        print('\n')
        menu()
        
    #opção 2 - listar campeonatos
    elif opcao == 2:
        arquivo = Arquivo('gestao_banca.csv')
        dataframe = arquivo.leitura()
        listar = Listar(dataframe)
        listar.campeonatos()
        print('\n')
        menu()

    
    #opção 3 - listar mercados
    elif opcao == 3:
        arquivo = Arquivo('gestao_banca.csv')
        dataframe = arquivo.leitura()
        listar = Listar(dataframe)
        listar.mercados()
        print('\n')
        menu()
        
    #opção 4 - cadastrar aposta
    elif opcao == 4:
        print('\n')
        print('Informe os dados da aposta:')
        data = input('Data (dd/mm/aaaa): ')
        esporte = input('Esporte: ')
        campeonato = input('Campeonato: ')
        mandante = input('Mandante: ')
        visitante = input('Visitante: ')
        mercado = input('Mercado: ')        
        stake = float(input('Stake: '))
        odd = float(input('Odd: '))
        resultado = input('Resultado (Green, Red, Half Red, Half Green, Void, Pendente): ')
        #Criar objeto da classe Bet
        bet = Bet(data, esporte, campeonato, mandante, visitante, mercado, stake, odd, resultado)
        print('\n')
        print('Dados da aposta:')
        print(bet)
        #Cadastrar aposta no arquivo
        bet.salvar_aposta(Arquivo('gestao_banca.csv').leitura())
        print('\n')
        print('Aposta cadastrada com sucesso!')
        menu()

    
    elif opcao == 5:
        arquivo = Arquivo('gestao_banca.csv')
        dataframe = arquivo.leitura()
        print('1 - Listar todas as apostas')
        print('2 - Listar apostas por esporte')
        print('3 - Listar apostas por campeonato')
        print('4 - Listar apostas por mercado')
        print('5 - Listar apostas por data')
        print('6 - Listar ultima aposta feita')
        opcao = int(input('\nDigite a opção desejada: '))
        if opcao == 1:
            listar = Listar(dataframe)
            listar.apostas()
            print('\n')
            menu()
        elif opcao == 2:
            listar = Listar(dataframe)
            listar.apostas_esporte(input('Digite o esporte: '))
            print('\n')
            menu()
        elif opcao == 3:
            listar = Listar(dataframe)
            listar.apostas_campeonato(input('Digite o campeonato: '))
            print('\n')
            menu()
        elif opcao == 4:
            listar = Listar(dataframe)
            listar.apostas_mercado(input('Digite o mercado: '))
            print('\n')
            menu()
        elif opcao == 5:
            listar = Listar(dataframe)
            listar.aposta_data(input('Digite a data (dd/mm/aaaa): '))
            print('\n')
            menu()
        elif opcao == 6:
            listar = Listar(dataframe)
            listar.ultima_aposta()
            print('\n')
            menu()
    
    elif opcao == 6:
        print('\n')
        print('Qual o mês desejado?')
        print('1 - Janeiro')
        print('2 - Fevereiro')
        print('3 - Março')
        print('4 - Abril')
        print('5 - Maio')
        print('6 - Junho')
        print('7 - Julho')
        print('8 - Agosto')
        print('9 - Setembro')
        print('10 - Outubro')
        print('11 - Novembro')
        print('12 - Dezembro')
        mes = int(input('\nDigite o mês desejado: '))
        print('\n')
        print('Detalhamento mensal:')
        mensal = Informacoes(Arquivo('gestao_banca.csv').leitura())
        if mes == 1:
            mensal.info_mes_janeiro()
            sleep(2)
            print('\n')
            menu()
        elif mes == 2:
            mensal.info_mes_fevereiro()
            sleep(2)
            print('\n')
            menu()
        elif mes == 3:
            mensal.info_mes_marco()
            sleep(2)
            print('\n')
            menu()
        elif mes == 4:
            mensal.info_mes_abril()
            sleep(2)
            print('\n')
            menu()
        elif mes == 5:
            mensal.info_mes_maio()
            sleep(2)
            print('\n')
            menu()
        elif mes == 6:
            mensal.info_mes_junho()
            sleep(2)
            print('\n')
            menu()
        elif mes == 7:
            mensal.info_mes_julho()
            sleep(2)
            print('\n')
            menu()
        elif mes == 8:
            mensal.info_mes_agosto()
            sleep(2)
            print('\n')
            menu()
        elif mes == 9:
            mensal.info_mes_setembro()
            sleep(2)
            print('\n')
            menu()
        elif mes == 10:
            mensal.info_mes_outubro()
            sleep(2)
            print('\n')
            menu()
        elif mes == 11:
            mensal.info_mes_novembro()
            sleep(2)
            print('\n')
            menu()
        elif mes == 12:
            mensal.info_mes_dezembro()
            sleep(2)
            print('\n')
            menu()
        else:
            print('Mês inválido!')
            sleep(2)
            print('\n')
            menu()

    elif opcao == 7:
        dia = Informacoes(Arquivo('gestao_banca.csv').leitura()).info_lucro_dia()
        sleep(2)
        print('\n')
        menu()

    elif opcao == 8:
        esporte = Informacoes(Arquivo('gestao_banca.csv').leitura()).info_esporte()
        sleep(2)
        print('\n')
        menu()

    elif opcao == 9:
        campeonato = Informacoes(Arquivo('gestao_banca.csv').leitura()).info_campeonato()
        sleep(2)
        print('\n')
        menu()

    elif opcao == 10:
        mercado = Informacoes(Arquivo('gestao_banca.csv').leitura()).info_mercado()
        sleep(2)
        print('\n')
        menu()
    
    elif opcao == 11:
        print('\n')
        print('Qual opção deseja realizar?')
        print('1 - Grafico por esporte')
        print('2 - Grafico por campeonato')
        print('3 - Grafico por mercado')
        print('4 - Grafico Diario')
        opcao = int(input('\nDigite a opção desejada: '))
        
        if opcao == 1:
            grafico = Graficos(Arquivo('gestao_banca.csv').leitura())
            grafico.grafico_esporte()
            sleep(2)
            print('\n')
            menu()
        elif opcao == 2:
            grafico = Graficos(Arquivo('gestao_banca.csv').leitura())
            grafico.grafico_campeonato()
            sleep(2)
            print('\n')
            menu()
        elif opcao == 3:
            grafico = Graficos(Arquivo('gestao_banca.csv').leitura())
            grafico.grafico_mercado()
            sleep(2)
            print('\n')
            menu()
        elif opcao == 4:
            grafico = Graficos(Arquivo('gestao_banca.csv').leitura())
            grafico.grafico_diario()
            sleep(2)
            print('\n')
            menu()
    
    elif opcao == 12:
        print('\n')
        print('Fechando programa...')
        sleep(2)
        exit()
        

            
if __name__ == '__main__':
    main()