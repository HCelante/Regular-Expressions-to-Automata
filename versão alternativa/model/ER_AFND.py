from infixa_posfixa import *
from pilha import *
from AFND_controle import *


def converter__ER__AFND(alfabeto_entrada):
    
    pilha_alfabeto = Pilha()    
    alfabeto_pos_fixo = converter_infixa_posfixa(alfabeto_entrada)    

    for i in range(len(alfabeto_pos_fixo)):
        if(alfabeto_pos_fixo[i] != '.' and alfabeto_pos_fixo[i] != '+' and alfabeto_pos_fixo[i] != '*'):
            automato = Automato(alfabeto_pos_fixo[i])
            pilha_alfabeto.inserir_pilha(automato)
        else:
            if(alfabeto_pos_fixo[i] == '.'):
                dado2 = pilha_alfabeto.get_pilha()
                dado1 = pilha_alfabeto.get_pilha()
                pilha_alfabeto.inserir_pilha(concatenacao(dado1, dado2))
            if(alfabeto_pos_fixo[i] == '+'):
                dado2 = pilha_alfabeto.get_pilha()
                dado1 = pilha_alfabeto.get_pilha()
                pilha_alfabeto.inserir_pilha(uniao(dado1,dado2))
            if(alfabeto_pos_fixo[i] == '*'):
                dado = pilha_alfabeto.get_pilha()
                pilha_alfabeto.inserir_pilha(fecho_kleene(dado))

    return pilha_alfabeto.get_pilha()
        

# alfabeto_entrada = '1
# '
# automato = converter__ER__AFND(alfabeto_entrada)
# automato.imprimir_automato()

