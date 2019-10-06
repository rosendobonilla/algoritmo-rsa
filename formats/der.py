#!/usr/bin/env python

from formats.base_format import ClaseBaseFormato

class DER(ClaseBaseFormato):
    def __init__(self):
        print("")
        
    def crearPubK(self, datos):
        return super().crearPubKDer

    def crearPrivK(self, datos):
        return super().crearPrivKDer       
