from AFND.util.infixa_posfixa import *
from AFND.util.pilha import *
from AFND.controle_afnd import *


def convert_ER_to_AFND(alfabetoEntrada):
    
    pilhaAlfabeto = Pilha()    
    alfabetoPosFixo = converter_infixa_posfixa(alfabetoEntrada)    

    for i in range(len(alfabetoPosFixo)):
        if(alfabetoPosFixo[i] != '.' and alfabetoPosFixo[i] != '+' and alfabetoPosFixo[i] != '*'):
            automato = Automato(alfabetoPosFixo[i])
            pilhaAlfabeto.inserir_pilha(automato)
        else:
            if(alfabetoPosFixo[i] == '.'):
                dado2 = pilhaAlfabeto.get_pilha()
                dado1 = pilhaAlfabeto.get_pilha()
                pilhaAlfabeto.inserir_pilha(concatenacao(dado1, dado2))
            if(alfabetoPosFixo[i] == '+'):
                dado2 = pilhaAlfabeto.get_pilha()
                dado1 = pilhaAlfabeto.get_pilha()
                pilhaAlfabeto.inserir_pilha(uniao(dado1,dado2))
            if(alfabetoPosFixo[i] == '*'):
                dado = pilhaAlfabeto.get_pilha()
                pilhaAlfabeto.inserir_pilha(fecho_kleene(dado))

    return pilhaAlfabeto.get_pilha()
        