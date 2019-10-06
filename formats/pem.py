#!/usr/bin/env python

from base_format import ClaseBaseFormato
import base64

class PEM(ClaseBaseFormato):

    def __init__(self):
        print("")

    def _marcadores(self, marcadorPEM):
        return ('-----BEGIN %s-----' % marcadorPEM,
            '-----END %s-----' % marcadorPEM)

    def _crearPEM(self, contenido, marcadorPEM):
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
        return self._crearPEM(der, 'RSA PUBLIC KEY')

    def crearPrivK(self, datos):
        der = super(PEM,self).crearPrivKDer(datos)
        return self._crearPEM(der, 'RSA PRIVATE KEY')  


    def cargarPubK(self,contenido,marcador):
        (pem_start, pem_end) = self._marcadores(marcador)

        lineas_pem = []
        in_pem_part = False

        for line in contenido.split('\n'):
            line = line.strip()

            # Validar el marcador de inicio
            if line == pem_start:
                if in_pem_part:
                    raise ValueError('Marcador de inicio repetido"%s"' % pem_start)

                in_pem_part = True
                continue

            # Ignorar lo que haya antes del marcador de inicio
            if not in_pem_part:
                continue

            # Validar el marcador de fin
            if in_pem_part and line == pem_end:
                in_pem_part = False
                break

            lineas_pem.append(line)

        if not lineas_pem:
            raise ValueError('No se encontro el marcador de inicio "%s"' % pem_start)

        if in_pem_part:
            raise ValueError('No se encontro el marcador de fin "%s"' % pem_end)

        # Decode del contenido en base 64
        pem = ''.join(lineas_pem)
        pem64 = base64.decodestring(pem) 

        return super(PEM,self).cargarPubKDer(pem64)
