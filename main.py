

import sys


def matchInterval(lista,inicial,final, matichinNumb): # retorna uma lista com o intervalo definido
    outInterval = []
    rig = 0 
    matchinCont = 0
    for charac in lista:
        if(rig == 0):
            if( (charac == inicial)  and (matchinCont == matichinNumb)):
                outInterval.append(charac)
                rig = 1
                matchinCont = 0
            elif(charac == inicial):
                matchinCont += 1 

        elif (rig == 1):
            if((charac == final) and (matichinNumb == matchinCont)):
                outInterval.append(charac)
                return outInterval
            elif(charac == final):
                matchinCont += 1
            else:
                outInterval.append(charac)







def main():
    regularExpresion = input("Ensina a expressão resgular: ")
    regularExpresion = regularExpresion.strip()
    
    # Retira espacos em branco
    rEwB = []
    for re in regularExpresion:
        if(re != ' '):
            rEwB.append(re)
    
    batata = matchInterval(rEwB,'1','0',0)
    print(batata)

main()