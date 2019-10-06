#!/usr/bin/env python

from formats.base_format import ClaseBaseFormato

class DER(ClaseBaseFormato):
    def __init__(self):
        print("")
        
    def crearPubK(self, datos):
        return super(DER,self).crearPubKDer(datos)

    def cargarPubK(self,datos):
        return super(DER,self).cargarPubKDer(datos)

    def crearPrivK(self, datos):
        return super(DER,self).crearPrivKDer(datos)       
