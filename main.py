#!/usr/bin/env python

from rsa.rsa import RSA
from util.factory import Factory
from util.files import Archivos
from util.operaciones import Opera

carpeta = "claves"

if __name__ == '__main__':
    rsa = RSA()
    publica, privada = rsa.generar_claves()

    opera = Opera(publica,privada)
    opera.imprimirPres()
    opera.imprimirClavesP()
    opera.leerFormato()

    opera.probarEncDesc()







