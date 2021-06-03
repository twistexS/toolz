#!/usr/bin/env python
#_*_ coding: utf8_*_

import requests
import argparse
from os import path

parser = argparse.ArgumentParser(description = "subir un archivo *metodo POSTS*")
parser.add_argument('-f','--file',help = "archivo a probar para metodo POSTS")
parser= parser.parse_args()

def main():
    if parser.file:
        if path.exists(parser.file):
            archivos = open(parser.files,'rb')
        else:
            print("El archivo no exite")
    else:
        print("Nesesito un archivo para subir")


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("salida [o_o]...")


