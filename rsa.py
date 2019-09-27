#!/usr/bin/env python

from random import randrange, getrandbits

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
	return (g, x - (b // a) * y, y)

def modinv(a,m):
    g,x,y = egcd(a,m)
    if g != 1:
	return None
    else:
	return x%m


def es_primo(n, k=128):
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

def generar_primo_candidato(tamano):
    p = getrandbits(tamano)
    p |= (1 << tamano - 1) | 1
    return p

def generar_primo(tam=1024):
    p = 4
    while not es_primo(p, 128):
        p = generar_primo_candidato(tam)
    return p

    
def generar_claves():
    p = generar_primo()
    q = generar_primo()

    while p == q:
        q = generar_primo()

    n = p * q
    phi = (p-1) * (q-1)
    e = 65537
    #d = mul_inv(e, phi)
    d = modinv(e,phi)    

    return ((e, n), (d, n))

def encriptar(publica, mensaje, tipo):
    e, n = publica
    if tipo == 0:
        texto = [pow(ord(char),e,n) for char in mensaje]
        return texto

    return pow(int(mensaje),e,n)


def desencriptar(privada, cifrado, tipo):
    d, n = privada
    if tipo == 0:
        texto = [chr(pow(char,d,n)) for char in cifrado]
        return ''.join(texto)
    
    return pow(int(cifrado),d,n)

if __name__ == '__main__':
    print ""
    print "++++++++++ Algoritmo de encriptacion RSA ++++++++++"
    print ""
    print "Generando numeros primos aleatorios (1024-bits)..."
    print ""
    print "Generando clave publica y privada..."

    publica, privada = generar_claves()

    print ""
    print "Tu clave publica es (e,n): "
    print publica
    print ""
    print "Tu llave privada es (d,n): "
    print privada
    print ""

    opcion = 'x'
    while opcion != 's' and opcion != 'n':
        opcion = raw_input("Deseas encriptar un mensaje [s] o un numero [n]: ")
        if opcion == 's':
            mensaje = raw_input("Ingresa el mensaje a encriptar (cadena): ")
            tipo = 0
        elif opcion == 'n':
            mensaje = raw_input("Ingresa el numero: ")
            tipo = 1
            if not mensaje.isdigit():
                raise ValueError("Numero invalido")

    m_encriptado = encriptar(publica, mensaje, tipo)

    print ""
    print "El mensaje encriptado es: "
    if tipo == 0:
        print ''.join(map(lambda x: str(x), m_encriptado))
    else:
        print m_encriptado
    print ""
    raw_input("Presiona ENTER para probar la desencriptacion...")
    print ""
    print "Desencriptando mensaje con su llave privada..."
    print ""
    print "El mensaje en texto plano es: ", desencriptar(privada, m_encriptado, tipo)




