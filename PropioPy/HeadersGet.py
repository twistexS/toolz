#!/usr/bin/env python
#_*_ coding: utf8_*_


import requests
import argparse

parser = argparse.ArgumentParser(description="Lector Cabeceras HTTP *metodo GET* ")
parser.add_argument('-t','--target',help="objetivo en formato http://DomainOrIP")
parser = parser.parse_args()



def main():
    if parser.target:
        print(parser.target)
        try:
            url = requests.get(url=parser.target)
            cabeceras = url.headers
            for i in cabeceras:
                print(i + " = " + cabeceras[i])
        except:
            print("no me pude conectar al objetivo")
    else:
        print("debe intoducir una IP o URL")



if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("salida [o_o]...")
