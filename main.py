#!/usr/bin/env python

from rsa.rsa import RSA
from util.factory import Factory
from util.files import Archivos
from util.operaciones import Opera

carpeta = "claves"

if __name__ == '__main__':
    rsa = RSA()
    print ""
    print "++++++++++ Algoritmo de encriptacion RSA ++++++++++"
    print ""
    print "Generando numeros primos aleatorios (1024-bits)..."
    print ""
    print "Generando clave publica y privada..."    
    publica, privada = rsa.generar_claves()
    opera = Opera(publica,privada)
    opera.imprimirClavesP()
    opera.leerFormatoClaves()
    opera.probarEncDesc()







