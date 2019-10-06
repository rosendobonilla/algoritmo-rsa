#!/usr/bin/env python

from base_format import ClaseBaseFormato
from rsa.rsa import egcd
import base64

class PEM(ClaseBaseFormato):

    def __init__(self):
        print("")

    def _marcadores(self, marcadorPEM):
        return ('-----BEGIN %s-----' % marcadorPEM,
            '-----END %s-----' % marcadorPEM)

    def crearPEM(self, contenido, marcadorPEM):
        (pem_inicio, pem_fin) = self._marcadores(marcadorPEM)

        b64 = base64.encodestring(contenido).replace('\n', '')
        lineasPEM = [pem_inicio]

        for block_start in range(0, len(b64), 64):
            block = b64[block_start:block_start + 64]
            lineasPEM.append(block)

        lineasPEM.append(pem_fin)
        lineasPEM.append('')

        return '\n'.join(lineasPEM)       

    def crearPubK(self, datos):
        der = super(PEM,self).crearPubKDer(datos)
        return self.crearPEM(der, 'RSA PUBLIC KEY')

    def crearPrivK(self, datos):
        der = super(PEM,self).crearPrivKDer(datos)
        return self.crearPEM(der, 'RSA PRIVATE KEY')      
