#!/usr/bin/env python
#_*_ coding: utf8_*_

#TwisterxS repaso argparse
#encontrar numeros primos scripting python

import argparse

parser = argparse.ArgumentParser(description="Encontrar Numeros Primos ")
parser.add_argument('-m','--maximun',help="Limite para encontrar los primos anteriores ")
parser = parser.parse_args()



def main():
    if parser.maximun:

        n=int(parser.maximun)
        if n > 0 :
            for i in range (2,n):
                creciente = 2
                EsPrimo = True
                while EsPrimo and creciente < i :
                    if i % creciente == 0 :
                        EsPrimo = False
                    else:
                        creciente += 1
                if EsPrimo :
                    print (i,"Primo! ┬┴┬┴┤･ω･)ﾉº")

        else :
            print ("intente de nuevo (∩╹□╹∩) ")
            print ("nota!:numeros mayores a 2")

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("salida [o_o]...")


