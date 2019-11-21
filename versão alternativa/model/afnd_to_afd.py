from AFND.modelo_afnd import *


def conversao_AFND_AFND(AFND):
    todosEstados = dict()
    eclosure = dict()
    # closures = {}
    contador = 0
    estado1 = AFND.get_estados_epsilon(AFND.inicio)
    eclosure[AFND.inicio] = estado1
    AFND = Automato()
    # AFND.inicio = contador
    estados = [[estado1, contador]]
    todosEstados[contador] = estado1
    contador += 1

    while len(estados) != 0:
        [estado, origem] = estados.pop()
        for palavra in AFND.alfabeto:
            destinos = AFND.get_transicao_destino(estado, palavra)
            for s in list(destinos)[:]:
                if s not in eclosure:
                    eclosure[s] = AFND.get_estados_epsilon(s)
                destinos = destinos.union(eclosure[s])
            if len(destinos) != 0:
                if destinos not in todosEstados.values():
                    estados.append([destinos, contador])
                    todosEstados[contador] = destinos
                    destino = AFND.letraEstado+str(contador)
                    contador += 1
                else:
                    destino = [k for k, v in todosEstados.items()
                               if v == destinos][0]
                AFND.add_transicao(
                    AFND.letraEstado+str(origem), palavra, destino)
    for valor, estado in todosEstados.items():
        if AFND.listaFim[0] in estado:
            estadoFinal = AFND.letraEstado+str(valor)
            if estadoFinal not in AFND.listaFim:
                AFND.listaFim.append(estadoFinal)

    AFND.listaFim.sort(key=lambda x: x[1:])
    return AFND
