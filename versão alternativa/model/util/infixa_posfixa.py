import re
from pilha import *

def busca_dados(pilha):
    return len(pilha) and pilha[len(pilha) - 1]


operador_precedente = {'+': 0,'.': 1,'*': 2}


def analise_expressao(expressao):
    pilha_expressao1 = Pilha()
    pilha_expressao2 = Pilha()
    expressao = list(re.sub("[a-zA-Z0-9][a-zA-Z0-9]+", lambda x: '.'.join(x.group()), expressao))
    for i in expressao:
        if i == '(':
            pilha_expressao1.inserir_pilha(i)
        if i == ')':
            pilha_expressao2.inserir_pilha(i)
    resultado = pilha_expressao1.tamanho - pilha_expressao2.tamanho
    while(1):
        if resultado == 0:
            break
        if resultado > 0:           # tem algo sobrando na pilha 1
            expressao.append(')')
            resultado -=1
        if resultado < 0:           # tem algo sobrando na pilha 2
            expressao.insert(0,'(')
            resultado +=1
    return ''.join(expressao)


def converter_infixa_posfixa(expressao):
    # expressao = re.sub("[a-zA-Z0-9][a-zA-Z0-9]+", lambda x: '.'.join(x.group()), expressao)
    # expressao = re.sub("\w\w+", lambda x: '.'.join(x.group()), expressao) # também funciona assim. \w significa qualquer palavra incluindo numeros
    expressao = analise_expressao(expressao)
    saida = ''
    operador_pilha = []
    for token in expressao:
        if (token == '.' or token == '+' or token == '*'):
            while(len(operador_pilha) and busca_dados(operador_pilha) != '(' and operador_precedente[busca_dados(operador_pilha)] >= operador_precedente[token]):
                saida += operador_pilha.pop()
            operador_pilha.append(token)
        elif (token == '(' or token == ')'):
            if(token == '('):
                operador_pilha.append(token)
            else:
                while(busca_dados(operador_pilha) != '('):
                    saida += operador_pilha.pop()
                operador_pilha.pop()
        else:
            saida += token
    while(len(operador_pilha)):
        saida += operador_pilha.pop()
    return saida

