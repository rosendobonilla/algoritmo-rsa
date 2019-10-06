#!/usr/bin/env python

import os, errno

class Archivos:
    
    def __init__(self):
        print("Creando archivos con las claves\n")

    def crearCarpeta(self, carpeta):
        if not os.path.exists(carpeta):
            try:
                os.makedirs(carpeta)
            except OSError as e:
                if e.errno != errno.EEXIST:
                    raise

    def crearArchivo(self, ruta, contenido): 
        f = open(ruta,"w+")
        f.write(contenido)
        f.close()