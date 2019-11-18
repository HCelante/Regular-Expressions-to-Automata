import sys

class Expressoes():
    def math(const):
        constantes = []
        contadorP = 0
        contadorE = 0
        contador = 0
        c = 0
        a = 0
        inicio = 0
        fim = 0

        for i in range(len(const)):
            constantes.append(const[i])
        
        for c in constantes:
            if (c == '(' or c == ')'):
                contadorP = contadorP + 1

        if (contadorP > 0):
            contador = int(contadorP/2)
            while (a <= contador):
                for i in constantes:
                    if (i == '('):
                        contadorE = contadorE + 1
                    if (contadorE == contador):
                        inicio = i
                        print(inicio)
                a = contador
                        

            