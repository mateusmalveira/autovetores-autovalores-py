from numpy import array, ones, matrix, sort, dot, zeros # bibliotecas
import os

#definição de funções

#função q limpa a tela
def limpa_console():
    os.system('cls' if os.name == 'nt' else 'clear')

#-----------------------------------------------------
def menu():  #função menu
    verifica = -1
    resp = -5
    while verifica != 1:
        print("\n\n\tMENU: \n\n\t 1 - Rodar Aplicacao\n\n\t 0 - Abandonar ")
        resp = input('\n\n\tEscolha um opçao:  ')
        if resp is '1' or resp is '0':
            verifica=1
        elif type(resp) is str:
            print("\n\n\tOPÇAO INVALIDA!!!")
            verifica=-1
        else:
            print("\n\n\t OPÇAO INVALIDA!!!")
            verifica=-1

    return resp

#=------------------------------------
def gera_matriz_inicial():

    verifica = -1
    while verifica != 1:
        tam = int(input('\n\n\n\tInforme a Dimensao da Matriz ente 2 e 100:  '))
        if tam >= 2 and tam <=100:
            verifica=1
        else:
            print("\n\n\t OPÇAO INVALIDA!!!")
            verifica=-1


    limpa_console() #invoca a função pra limpar o console

    #define a matriz inicial de zeros(0)
    matriz = zeros((tam,tam))

    #Preenchimento da Matriz
    linha = 0
    while linha < tam:  #loop q controla  as linhas da matriz---------
        for coluna in range(tam): # loop q controla as colunas da matrz
            num = (input("\n\tDigite um numero pra a posicão [%d][%d] da matriz:  "%(linha+1,coluna+1)))
            matriz[linha][coluna]  = int(num)

        linha = linha + 1

    return matriz

#---------------------------------------
def menor_elemento_matriz(matriz):#procura o menor elemento do vetor
    return sort(abs(array(matriz).flatten()))[0]

#-----------------------
def calcular_autovalor(matriz_inicial, matriz_gerada_iteracao):#Calcula o autovalor
    X = array(matriz_gerada_iteracao).flatten()
    A = array(matriz_inicial * matriz_gerada_iteracao).flatten()
    return dot(A, X)/dot(X, X)


def calcula_autovetor(autovalor, matriz_gerada_iteracao):#Calcula o Autovetor
    return autovalor * matriz_gerada_iteracao


def main():
    print('\n\n\n\tUFC-Sobral 2016.1\n\tAlgébra Linear\n\tProf. Miquéias Araújo\n\tAlgoritmo: Cálculo de Autovalor e autovetor\n\tPlataforma: Python 3.4')
    print('\n\n\t @utor: Mateus Malveira\t 356730')
    print('\n\t Data: 10 de junho de 2016\n\n\t------------------------------------------------')

    resp = menu()    # chama a função menu
    limpa_console()  # chama a função menu

    if resp is '1':
        A = matrix(gera_matriz_inicial()) # Entrada de dados

        print ("\n\n--------- Matriz de Entrada ---------- \n\n")
        print(A)

        MAX_ITERACOES = 100  #Numero de vezes que se calcula as aproximações
        TAMANHO_MATRIZ = len(A)
        ITERACAO = 1
        matriz_inicial = ones((TAMANHO_MATRIZ, 1))

        while ITERACAO <= MAX_ITERACOES:
            X = A * matriz_inicial
            matriz_inicial = X
            menor_matriz = menor_elemento_matriz(X)
            ITERACAO += 1
        X_normalizado =X/menor_elemento_matriz(X)

        autovalor = calcular_autovalor(A,X_normalizado)

        print('\n---------AutoValor-----------\n')
        print('λ:  ',int(autovalor))
        print('\n---------AutoVetor-----------\n\n')
        auto_vet = calcula_autovetor((autovalor), (X_normalizado))
        print(auto_vet)
        sair = input('\n\nPressione qualquer tecla')
        limpa_console()

        main() # invoca a função principal pra rodar aplicação outra vez
    else:
        print("\n\n\t-----------------\n\n\tFim Algoritmo\n\n\tMateus Malveira Copyright2016\n\n\n")
        exit(0)

#-----------------inicialização do algoritmo---------------------

if __name__ == "__main__": #Inicia  o Programa
    main()