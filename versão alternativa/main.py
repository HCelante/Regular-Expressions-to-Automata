import os
from model.expressao_to_afnd import *
from model.AFND.util.infixa_posfixa import *
from model.afnd_to_afd import *
import time
import subprocess

# from os import popen


def main():
    print("Expressão regular para automato - APS LFAC")
    expressao_regular = ''
    AFND = ''
    AFD = ''
    AFD_minimizado = ''
    arquivo_AFD_MINIMO = 'AFD_MINIMO.txt'
    opcao = -1
    arquivo_AFD_para_minimizar = 'AFD_minimizar.txt'
    arquivo_AFND = 'AFND.txt'
    arquivo_AFD = 'AFD.txt'
    palavra_teste = ''

    while(opcao != '0'):

        print("\n")
        print("___________________________")
        print(" Opcoes:")
        print(" (1) Inserir ER;")
        print(" (2) Gerar ER;")
        print(" (3) Gerar AFND;")
        print(" (4) Gerar AFD;")
        print(" (5) Gerar AFD minimizado;")
        print(" (0) Sair do programa;")
        print("___________________________")
        print("\n")

        opcao = input("\n  >> ")
        if(opcao == '1'):
            expressao_regular = input('\n >> Insira a ER desejada : ')
            expressao_regular = analise_expressao(expressao_regular)
            print("\n|Passo 1 - A expressão foi analisada.")
            AFND = convert_ER_to_AFND(expressao_regular)
            print("\n|Passo 2 - A expressão foi convertida em um AFND.")
            AFD = conversao_AFND_AFD(AFND)
            print("\n|Passo 3 - O AFND foi convertido em um AFD.")
            AFND.criar_arquivo(arquivo_AFND, 'NDFA')
            AFD.criar_arquivo(arquivo_AFD, 'DFA')
            AFD.criar_arquivo_AFD_MINIZAR(arquivo_AFD_para_minimizar)
            print("\n|Passo 4 - Os arquivos com os respectivos automatos foram criados.")

            processo = subprocess.Popen(
                ['python3', 'min-AFD.py', arquivo_AFD_para_minimizar, arquivo_AFD_MINIMO])
            if processo.wait() != 0:
                print(" Erro no processo!", processo.errors)

            # popen('python3 min-AFD.py '+arquivo_AFD_para_minimizar+' '+arquivo_AFD_MINIMO+' > res.txt')
            # popen('python3 fla/main.py' +arquivo_AFD_MINIMO+' >'+arquivo_resposta_aceitacao)

        if(opcao == '2'):
            os.system('cls' if os.name == 'nt' else 'clear')
            print("\n EXPRESSÃO: ", expressao_regular)
            input()

        if(opcao == '3'):
            os.system('cls' if os.name == 'nt' else 'clear')
            AFND.imprimir_automato()
            testar_automato(arquivo_AFND, expressao_regular, AFND)

        if(opcao == '4'):
            os.system('cls' if os.name == 'nt' else 'clear')
            AFD.imprimir_automato()
            testar_automato(arquivo_AFD, expressao_regular, AFD)

        if(opcao == '5'):
            os.system('cls' if os.name == 'nt' else 'clear')
            arquivo = open(arquivo_AFD_MINIMO, 'r')
            dados = arquivo.readlines()
            for i in dados:
                print(i, end="")
            print("\n")
            arquivo.close()
            testar_automato(arquivo_AFD_MINIMO, expressao_regular, AFD)


def testar_automato(arquivo_automato, exp_reg, automato):

    testar = input("\nGostaria de testar o automato?  [ 's' ] : ")
    if testar == 's':
        arquivo_resposta_aceitacao = 'resposta.txt'
        criar_arq = open(arquivo_resposta_aceitacao, 'w')
        criar_arq.close()

        testar_novamente = 's'
        while(testar_novamente == 's'):

            print("\n EXPRESSÃO: ", exp_reg)
            palavra_teste = verificar_teste(automato)
            processo = subprocess.Popen(
                ['python3', 'fla/main.py', arquivo_automato, palavra_teste, ' >', arquivo_resposta_aceitacao])
            if processo.wait() != 0:
                print(" Erro no processo!")
            arquivo = open(arquivo_resposta_aceitacao, 'r')
            resposta = arquivo.readlines()
            print()
            for i in resposta:
                print(i)
            arquivo.close()
            testar_novamente = input("Testar de novo ?  [ 's' ] : ")


def verificar_teste(automato):
    palavra_teste = ''
    continuar = True
    while(continuar):
        palavra_teste = input(">> Insira uma palavra para testar: ")
        for i in range(len(palavra_teste)):
            if palavra_teste[i] in automato.alfabeto:
                continuar = False
            else:
                continuar = True
                print("\n A palavra não faz parte!")
                print("Alfabeto aceito: ", automato.alfabeto)
                break
    return palavra_teste


if __name__ == '__main__':
    main()
