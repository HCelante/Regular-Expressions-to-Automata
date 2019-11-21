from modelo_afnd import *

def renomeia_estados_automato(incremento, automato2):
 
        automato = Automato()
        for i in automato2.lista_transicao:
            automato.add_transicao(automato.letra_estado+str(incremento + int(i.origem[1:])), i.nome, automato.letra_estado+str(incremento + int(i.destino[1:])))
        automato.inicio = automato.letra_estado + str(incremento + int(automato2.listaEstado[0][1:]))
        return automato


def organizar(automato): # atualiza o próprio automato
    j = 0
    n = max(automato.lista_transicao, key=lambda t: max(int(t.origem[1:]), int(t.destino[1:])))
    n = int(max(n.origem, n.destino)[1:])
    for i in range(n+1):
        filtrado = [t for t in automato.lista_transicao if t.origem == automato.letra_estado+str(i) or t.destino == automato.letra_estado+str(i)]
        if filtrado:
            if j == i:
                continue
            for t in filtrado:
                
                if t.origem == automato.letra_estado+str(i):
                    t.origem = automato.letra_estado+str(j)
                if t.destino == automato.letra_estado+str(i):
                    t.destino = automato.letra_estado+str(j)
            j += 1
    automato.listaEstado = [automato.letra_estado+str(i) for i in range(j)]
    automato.inicio = automato.listaEstado[0]
    automato.listaFim[0] = automato.listaEstado[-1]



def concatenacao(automato1, automato2):
    if(type(automato1) is Automato) and (type(automato2) is Automato):
        automato = Automato()
        for i in automato1.lista_transicao:
            automato.add_transicao(i.origem, i.nome, i.destino)
        automato2 = renomeia_estados_automato(len(automato.listaEstado), automato2)
        automato.add_transicao(automato1.listaFim[0], automato.epsilon(), automato2.inicio)
        for i in automato2.lista_transicao:
            automato.add_transicao(i.origem, i.nome, i.destino)
        return automato
    print("\n\n erro, não é autômato\n\n")
    return False


def uniao(automato1, automato2): 
    if(type(automato1) is Automato) and (type(automato2) is Automato):
        automato = Automato()
        automato1 = renomeia_estados_automato(1,automato1)
        automato.add_transicao(automato.inicio, automato.epsilon(), automato1.inicio)
        for i in automato1.lista_transicao:
            automato.add_transicao(i.origem, i.nome, i.destino)
        automato2 = renomeia_estados_automato(len(automato.listaEstado), automato2)
        automato.add_transicao(automato.inicio, automato.epsilon(),automato2.inicio)
        for i in automato2.lista_transicao:
            automato.add_transicao(i.origem, i.nome, i.destino)
        automato.add_estado(automato.letra_estado + str(1+int(automato2.listaFim[0][1:])))
        automato.add_transicao(automato1.listaFim[0], automato.epsilon(), automato.listaFim[0])
        automato.add_transicao(automato2.listaFim[0], automato.epsilon(), automato.listaFim[0])            
        return automato
    print("\n\n erro, não é autômato\n\n")
    return False


def fecho_kleene(automato1):
    if(type(automato1) is Automato):
        automato = Automato()
        automato1 = renomeia_estados_automato(1, automato1)
        automato.add_transicao(automato.inicio, automato.epsilon(), automato1.inicio)
        for i in automato1.lista_transicao:
            automato.add_transicao(i.origem, i.nome, i.destino)
        automato.add_transicao(automato1.listaFim[0], automato.epsilon(), automato1.inicio)
        automato.add_estado(automato.letra_estado + str(1+(int(automato1.listaFim[0][1:]))))
        automato.add_transicao(automato1.listaFim[0], automato.epsilon(), automato.listaFim[0])
        automato.add_transicao(automato.inicio, automato.epsilon(), automato.listaFim[0])
        return automato
    print("\n\n erro, não é autômato\n\n")
    return False

