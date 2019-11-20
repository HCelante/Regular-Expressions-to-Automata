from AFND.modelo_afnd import *

def conversao_AFND_AFD(AFND):
    todos_estados = dict()
    eclosure = dict()
    closures = {}
    contador = 0
    estado1 = AFND.get_estados_epsilon(AFND.inicio)
    eclosure[AFND.inicio] = estado1
    AFD = Automato()
    # AFND.inicio = contador
    estados = [[estado1,contador]]
    todos_estados[contador] = estado1
    contador +=1

    while len(estados) != 0:
        [estado, origem]= estados.pop()
        for palavra in AFND.alfabeto:
            destinos = AFND.get_transicao_destino(estado, palavra)
            for s in list(destinos)[:]:
                if s not in eclosure:
                    eclosure[s] = AFND.get_estados_epsilon(s)
                destinos = destinos.union(eclosure[s])
            if len(destinos) != 0:
                if destinos not in todos_estados.values():
                    estados.append([destinos, contador])
                    todos_estados[contador] = destinos
                    destino = AFD.letra_estado+str(contador)
                    contador +=1
                else:
                    destino = [k for k, v in todos_estados.items() if v  ==  destinos][0]
                AFD.add_transicao(AFD.letra_estado+str(origem), palavra, destino)
    for valor, estado in todos_estados.items():
        if AFND.lista_fim[0] in estado:
            estado_final = AFD.letra_estado+str(valor)
            if estado_final not in AFD.lista_fim:
                AFD.lista_fim.append(estado_final)

    AFD.lista_fim.sort(key = lambda x: x[1:])
    return AFD
