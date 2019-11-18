class Pilha(object):
    def __init__(self):
        self.tamanho  =  0
        self.dado     =  list()

    def get_pilha(self):
        self.tamanho -=1
        return self.dado.pop()

    def inserir_pilha(self, elemento):
        self.dado.append(elemento)
        self.tamanho +=1

    def imprimir_pilha_automato(self):
        for i in self.dado:
            i.imprimir_automato()

    def imprimir_pilha_expressao():
        print(dado)