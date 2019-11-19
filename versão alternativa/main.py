
'''
Grupo:
'''
import os # biblioteca pra usar o método de limpar a tela
from model.ER_AFND import *
from model.util.infixa_posfixa import *
from model.AFND_AFD import *
import time
import subprocess

# from os import popen

def main():
    print("EXPRESSÃO REGUAR VS AUTOMATOS")
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

        # limpa a tela no Windows ou Linux
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\n")
        print(" FUNCIONALIDADES: ")
        print(" [1] Inserir ER")
        print(" [2] Emitir ER")
        print(" [3] Emitir AFND")
        print(" [4] Emitir AFD")
        print(" [5] Emitir AFD MINIMIZADO")
        print(" [0] Sair")

        opcao = input("\n  >> ")
        if(opcao == '1'):                                            # 'a*+c*.(q*.w*.e*)+t*+(m*.y*)+o*'
            # expressao_regular = '0+1*.0'  
            expressao_regular = input('\n INSIRA A EXPRESSÃO REGULAR : ')    
            expressao_regular = analise_expressao(expressao_regular)
            AFND = converter__ER__AFND(expressao_regular)
            AFD = conversao_AFND_AFD(AFND)

            AFND.criar_arquivo(arquivo_AFND,'NDFA')
            AFD.criar_arquivo(arquivo_AFD,'DFA')
            AFD.criar_arquivo_AFD_MINIZAR(arquivo_AFD_para_minimizar)

            processo = subprocess.Popen(['python3', 'min-AFD.py', arquivo_AFD_para_minimizar, arquivo_AFD_MINIMO])
            if processo.wait() != 0:
                print(" Erro no processo!", processo.errors)
                

            # popen('python3 min-AFD.py '+arquivo_AFD_para_minimizar+' '+arquivo_AFD_MINIMO+' > res.txt')
            # popen('python3 fla/main.py' +arquivo_AFD_MINIMO+' >'+arquivo_resposta_aceitacao)


        if(opcao == '2'):
            os.system('cls' if os.name == 'nt' else 'clear')
            print("\n ESPRESSÃO: ",expressao_regular)
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
            arquivo = open(arquivo_AFD_MINIMO,'r')
            dados = arquivo.readlines()
            for i in dados:
                print(i,end="")
            print("\n")
            arquivo.close()
            testar_automato(arquivo_AFD_MINIMO,expressao_regular,AFD)


            # palavra_teste = verificar_teste(expressao_regular, AFD)
            # popen('python3 fla/main.py '+arquivo_AFD_MINIMO+' '+palavra_teste+' >'+arquivo_resposta_aceitacao)            
            # arquivo = open(arquivo_resposta_aceitacao)
            # resposta = arquivo.readlines()
            # for i in resposta:
            #     print(i)
            # arquivo.close()



def testar_automato(arquivo_automato, exp_reg, automato):

    testar = input("\n TESTAR AUTOMATO ?  [ SIM == 's' ] : ")
    if testar == 's':
        arquivo_resposta_aceitacao = 'resposta.txt'
        criar_arq = open(arquivo_resposta_aceitacao,'w')
        criar_arq.close()

        testar_novamente = 's'
        while(testar_novamente == 's'):

            print("\n ESPRESSÃO: ",exp_reg)
            palavra_teste = verificar_teste(automato)
            processo = subprocess.Popen(['python3', 'fla/main.py', arquivo_automato, palavra_teste, ' >',arquivo_resposta_aceitacao])
            if processo.wait() != 0:
                print(" Erro no processo!")
            arquivo = open(arquivo_resposta_aceitacao,'r')
            resposta = arquivo.readlines()
            print()
            for i in resposta:
                print(i)
            arquivo.close()
            testar_novamente = input(" TESTAR NOVAMENTE ?  [ SIM == 's' ] : ")
        
    


def verificar_teste(automato):
    palavra_teste = ''
    continuar = True
    while(continuar):
        palavra_teste = input(" INSIRA A PALAVRA DE TESTE: ") 
        for i in range(len(palavra_teste)):
            if palavra_teste[i] in automato.alfabeto:
                continuar = False
            else:
                continuar = True
                print("\n PALAVRA NÃO FAZ PARTE DO ALFABETO DE ENTRADA, TENTE NOVAMENTE!")
                print(" OBS: ALFABETO DE ENTRADA: ",automato.alfabeto)
                break
    return palavra_teste


if __name__ == '__main__':
	main()