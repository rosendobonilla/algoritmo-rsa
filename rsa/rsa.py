#!/usr/bin/env python
from random import randrange, getrandbits

class RSA:
    # Implementacion del algoritmo extendido de Euclides para obtener el inverso multiplicativo
    def egcd(self, a, b):
        if a == 0:
            return (b, 0, 1)
        else:
            g, y, x = self.egcd(b % a, a)
            return (g, x - (b // a) * y, y)

    # Calculamos el inverso multiplicativo de e (e*d mod phi = 1)
    def modinv(self, a, m):
        g, x, y = self.egcd(a, m)
        if g != 1:
            return None
        else:
            return x % m

# Verificamos que el numero candidato sea primo con la ayuda del Teorema de Miller Robin


    def es_primo(self, n, k=128):
        if n == 2 or n == 3:
            return True
        if n <= 1 or n % 2 == 0:
            return False
        s = 0
        r = n - 1
        while r & 1 == 0:
            s += 1
            r //= 2
        for _ in range(k):
            a = randrange(2, n - 1)
            x = pow(a, r, n)
            if x != 1 and x != n - 1:
                j = 1
                while j < s and x != n - 1:
                    x = pow(x, 2, n)
                    if x == 1:
                        return False
                    j += 1
                if x != n - 1:
                    return False
        return True

    # Generamos un numero impar de tamano tamano aplicando una mascara para el MSB y LSB (1 y 1)


    def generar_primo_candidato(self,tamano):
        p = getrandbits(tamano)
        p |= (1 << tamano - 1) | 1
        return p

    # Generamos un numero primo
    def generar_primo(self,tam=1024):
        p = 4
        while not self.es_primo(p, 128):
            p = self.generar_primo_candidato(tam)
        return p

    # Generamos la clave publica y la privada


    def generar_claves(self):
        p = self.generar_primo()
        q = self.generar_primo()

        while p == q:
            q = self.generar_primo()

        n = p * q
        phi = (p-1) * (q-1)
        e = 65537
        #d = mul_inv(e, phi)
        d = self.modinv(e, phi)

        #dP = d % p
        #dQ = d % q
        #qInv = pow(q, p - 2, p)

        #privada = pempriv(n,e,d,p,q,dP,dQ,qInv)

        return ((e, n), (e, n, d, p, q))
        # return ((e,n), privada)


    def encriptar(self,publica, mensaje, tipo):
        e, n = publica
        if tipo == 0:
            texto = [pow(ord(char), e, n) for char in mensaje]
            return texto

        return pow(int(mensaje), e, n)

    # Desencriptamos el mensaje con la clave privada


    def desencriptar(self,privada, cifrado, tipo):
        d, n = privada
        if tipo == 0:
            texto = [chr(pow(char, d, n)) for char in cifrado]
            return ''.join(texto)

        return pow(int(cifrado), d, n)
