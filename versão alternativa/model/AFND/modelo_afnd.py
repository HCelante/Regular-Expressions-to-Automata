from util.transicao import *
from itertools import chain


class Automato:

    def __init__(self, nome=None):
        self.letra_estado = 'q'
        self.inicio = self.letra_estado+(str(0))
        if(nome != None):
            self.listaFim = [self.letra_estado+(str(1))]
            self.listaEstado = [self.inicio, self.listaFim[0]]
            transicao = Transicao(self.inicio, nome, self.listaFim[0])
            self.lista_transicao = [transicao]
            self.alfabeto = [transicao.nome]
        else:
            self.listaEstado = []
            self.lista_transicao = list()
            self.alfabeto = list()
            self.listaFim = list()

    @staticmethod
    def epsilon():
        return 'E'

    def add_estado(self, nome_estado):
        if(nome_estado in self.listaEstado):
            return False
        self.listaEstado.append(nome_estado)
        self.listaFim = [nome_estado]
        return True

    def get_estado(self, nome_estado):
        for estado in self.listaEstado:
            if estado == nome_estado:
                return estado
        return False

    def add_transicao(self, origem, nome, destino):
        if isinstance(origem, int):
            origem = self.letra_estado+str(origem)
        if isinstance(destino, int):
            destino = self.letra_estado+str(destino)
        if(self.verifica_origem_e_destino_da_transicao(origem, nome, destino) == False):
            if(self.get_estado(origem) == False):
                self.add_estado(origem)
            if(self.get_estado(destino) == False):
                self.add_estado(destino)
            transicao = Transicao(origem, nome, destino)
            self.lista_transicao.append(transicao)
            if(transicao.nome != self.epsilon()):
                if(transicao.nome not in self.alfabeto):
                    self.alfabeto.append(transicao.nome)
            return True
        return False

    def verifica_origem_e_destino_da_transicao(self, origem, nome, destino):
        for transicao in self.lista_transicao:
            if ((transicao.origem == origem) and (transicao.destino == destino) and (transicao.nome == nome)):
                return True
        return False

    def imprimir_automato(self):
        print(self.alfabeto)
        print(self.epsilon())
        print(self.inicio)
        for i in self.listaFim:
            print(f'{i} ', end='')
        print()
        for estados in self.listaEstado:
            print(estados, end=" ")
        print("")
        for i in self.lista_transicao:
            print(f'[{i.origem} {i.nome} {i.destino}]')
        print("\n")

    def get_transicao_destino(self, estado, palavra):

        transicoes = self.get_transicao()
        if isinstance(estado, int):  # mudar pra list
            estado = [estado]
        todos_estados = set()
        for estado in estado:
            if estado in transicoes:
                for transicao in transicoes[estado]:
                    if palavra in transicoes[estado][transicao]:
                        todos_estados.add(transicao)
        return set(todos_estados)

    def get_transicao(self):
        transicoes = {}
        for i in range(len(self.lista_transicao)):
            origem = self.lista_transicao[i].origem
            destino = self.lista_transicao[i].destino
            nome = self.lista_transicao[i].nome
            if not transicoes.get(origem):
                transicoes[origem] = {}
            if not transicoes[origem].get(nome):
                transicoes[origem][destino] = {nome}
            else:
                transicoes[origem][destino].update([nome])
        return transicoes

    def get_estados_epsilon(self, estado_origem):

        transicoes = self.get_transicao()
        todos_estados = set()
        origens = set([estado_origem])
        while len(origens) != 0:
            origem = origens.pop()
            todos_estados.add(origem)
            if origem in transicoes:
                for destino in transicoes[origem]:
                    if Automato.epsilon() in transicoes[origem][destino] and transicoes[origem][destino] not in todos_estados:
                        origens.add(destino)
        return todos_estados

    def criar_arquivo(self, nome_arquivo, titulo):

        arquivo = open(nome_arquivo, 'w')
        arquivo.write(titulo+'\n')
        arquivo.write(' '.join(self.alfabeto) + '\n')
        arquivo.write(self.epsilon()+'\n')
        arquivo.write(' '.join(self.listaEstado) + '\n')
        arquivo.write(self.inicio + '\n')
        arquivo.write(' '.join(self.listaFim) + '\n')
        for i in self.lista_transicao:
            arquivo.write(i.origem + ' ')
            arquivo.write(i.nome + ' ')
            arquivo.write(i.destino + '\n')
        arquivo.close()

        # EXEMPLO:
        # NDFA
        # 0 1
        # E
        # q0 q1
        # q0
        # q1
        # q0 0 q1
        # q0 1 q0

    def criar_arquivo_AFD_MINIZAR(self, nome_arquivo):
        arquivo = open(nome_arquivo, 'w')
        arquivo.write('(\n{' + ','.join(self.listaEstado) + '}\n{')
        arquivo.write(','.join(self.alfabeto))
        arquivo.write('},\n{\n')
        for i in self.lista_transicao:
            arquivo.write('('+i.origem + ',')
            arquivo.write(i.nome+'->')
            arquivo.write(i.destino + ')'+',\n')
        arquivo.write('},\n')
        arquivo.write(self.inicio+',\n')
        arquivo.write('{'+','.join(self.listaFim))
        arquivo.write('}\n)')
        arquivo.close()

    # ideia de como implementar um sistema de aceitação!
    # def acceptsString(self, string):
    #     currentstate = self.dfa.startstate
    #     for ch in string:
    #         if ch==":e:":
    #             continue
    #         st = list(self.dfa.gettransitions(currentstate, ch))
    #         if len(st) == 0:
    #             return False
    #         currentstate = st[0]
    #     if currentstate in self.dfa.finalstates:
    #         return True
    #     return False


'''
Para executar o programa é necessário passar 3 parametros:
- primeiro o arquivo .txt com a representação do automato (arquivo deve existir no diretório);
- segundo o nome do arquivo para a tabela de minimização(será gerado um arquivo com o nome passado);
- terceiro o nome do arquivo onde será salvo o novo automato minimizado (será gerado um arquivo com o nome passádo)

_______________________________________________________________________________
----------MODELO PARA CRIAÇÃO DO ARQUIVO PARA REPRESENTAR UM AUTOMATO----------

LINHA 1 - (
LINHA 2 - {estado1,estado2,estado3,estado4}
LINHA 3 - {0, 1},
LINHA 4 - {
LINHA 5 - (estado1,0->estado2),
LINHA 6 - (estado2,0->estado3),
LINHA 7 - (estado3,1->estado2),
LINHA 8 - (estado3,0->estado4),
LINHA 9 - },
LINHA 10- estado1,
LINHA 11- {estado3,estado4}
LINHA 20- )

--------------------------------------------------------------------------------
obs: atenção para a sintáxe (chaves, parenteses,virgulas)
     linha 2:  lista de estados do automato
     linha 3:  lista de simbolos do automato(alfabeto)
     linha 5:  exemplo de representação de transição no formato:
               (estado_origem,simbolo->estado_destino),
     linha 10: estado inicial
     linha 11: estados finais


'''

# aut = Automato('a')

# aut.add_transicao('q0','E','q2')
# aut.add_transicao('q0','E','q3')
# aut.add_transicao('q0','E','q4')
# aut.add_transicao('q2','E','q5')
# aut.add_transicao('q5','E','q6')
# aut.add_transicao('q5','E','q8')

# aut.imprimir_automato()

# print(aut.get_estados_epsilon2('q0'))
