#!/usr/bin/env python

from abc import ABCMeta, abstractmethod
from rsa.rsa import RSA

class ClaseBaseFormato:
    __metaclass__ = ABCMeta

    def __init__(self):
        print("")

    def crearPubKDer(self, datos):
        from pyasn1.type import univ, namedtype
        from pyasn1.codec.der import encoder

        e,n = datos

        class AsnPubKey(univ.Sequence):
            componentType = namedtype.NamedTypes(
                namedtype.NamedType('modulus', univ.Integer()),
                namedtype.NamedType('publicExponent', univ.Integer()),
            )

        asn_key = AsnPubKey()
        asn_key.setComponentByName('modulus', n)
        asn_key.setComponentByName('publicExponent', e)

        return encoder.encode(asn_key)

    def cargarPubKDer(self,datos):
        from pyasn1.codec.der import decoder
        (priv, _) = decoder.decode(datos)

        return priv

    def crearPrivKDer(self, datos):
        from pyasn1.type import univ, namedtype
        from pyasn1.codec.der import encoder


        rsa = RSA()
        n,e,d,p,q = datos

        exp1 = long(d % (p - 1))
        exp2 = long(d % (q - 1))
        (_,coef,_) = rsa.egcd(q, p)

        class AsnPrivKey(univ.Sequence):
            componentType = namedtype.NamedTypes(
                namedtype.NamedType('version', univ.Integer()),
                namedtype.NamedType('modulus', univ.Integer()),
                namedtype.NamedType('publicExponent', univ.Integer()),
                namedtype.NamedType('privateExponent', univ.Integer()),
                namedtype.NamedType('prime1', univ.Integer()),
                namedtype.NamedType('prime2', univ.Integer()),
                namedtype.NamedType('exponent1', univ.Integer()),
                namedtype.NamedType('exponent2', univ.Integer()),
                namedtype.NamedType('coefficient', univ.Integer()),
            )

        # Create the ASN object
        asn_key = AsnPrivKey()
        asn_key.setComponentByName('version', 0)
        asn_key.setComponentByName('modulus', n)
        asn_key.setComponentByName('publicExponent', e)
        asn_key.setComponentByName('privateExponent', d)
        asn_key.setComponentByName('prime1', p)
        asn_key.setComponentByName('prime2', q)
        asn_key.setComponentByName('exponent1', exp1)
        asn_key.setComponentByName('exponent2', exp2)
        asn_key.setComponentByName('coefficient', coef)

        return encoder.encode(asn_key)  

    @abstractmethod
    def crearPubK(self, e, n):
        pass

    @abstractmethod
    def cargarPubK(self, contenido, marcador):
        pass
    
    @abstractmethod
    def crearPrivK(self):
        pass

    #@abstractmethod
    #def cargarPrivK(self):
    #    pass
