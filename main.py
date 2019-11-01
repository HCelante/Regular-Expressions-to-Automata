

import sys


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
    regularExpresion = input("Insira a expressão resgular: ")
    regularExpresion = regularExpresion.strip()
    
    # Retira espacos em branco
    rEwB = []
    for re in regularExpresion:
        if(re != ' '):
            rEwB.append(re)
    
    #batata = matchInterval(rEwB,'(',')',3)
    #print(batata)

main()
