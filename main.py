import sys
from models.pilha import Pilha
from src.separaExpressoes import Expressoes as ex

def matchInterval(lista,inicial,final, matichinNumb): # retorna uma lista com o intervalo definido
    outInterval = []
    rig         = 0 
    matchinConti = 0
    matchinContf = 0
    for charac in lista:
        if(rig == 0):
            if((str(charac) == str(inicial) ) and (matchinConti == matichinNumb)):
                print("Encontrado o ", inicial, "escolhido!")
                outInterval.append(charac)
                rig             = 1

            elif(str(charac) == str(inicial)):
                matchinConti     += 1 
            elif(str(charac) == str(final)):
                matchinContf += 1
        elif (rig == 1):
            if((str(charac) == str(final)) and (matichinNumb == matchinContf)):
                print("Encontrado o ", final, "escolhido!")
                outInterval.append(charac)
                rig = 2
                return outInterval
            elif(str(charac) == str(final)):
                outInterval.append(charac)
                matchinContf     += 1
            else:
                outInterval.append(charac)
        else:
            print("batata")

def main():
    constMath = input("Insira a expressao regular: ..")
    ex.math(constMath)

main()