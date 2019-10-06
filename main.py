#!/usr/bin/env python

from rsa.rsa import generar_claves,encriptar,desencriptar
from util.factory import Factory
from util.files import Archivos

carpeta = "claves"

if __name__ == '__main__':
    factory = Factory()
    archivo = Archivos()
    archivo.crearCarpeta(carpeta)
    print ""
    print "++++++++++ Algoritmo de encriptacion RSA ++++++++++"
    print ""
    print "Generando numeros primos aleatorios (1024-bits)..."
    print ""
    print "Generando clave publica y privada..."
    publica, privada = generar_claves()
    (_,n,d,_,_) = privada
    print ""
    print "Tu clave publica sin formato es (e,n): "
    print publica
    print ""
    print "Tu llave privada sin formato es (d,n): "
    print ""
    print privada
    print ""
    opFormat = 'x'
    while opFormat != 'p' and opFormat != 'd':
        opFormat = raw_input("Formato de salida [p] PEM o [d] DER: ")
        if opFormat == 'p':
            pemSalida = factory.salidaFormato("pem")
            publicaPEM = pemSalida.crearPubK(publica)
            archivo.crearArchivo("./"+carpeta+"/clave_rsa.pub", publicaPEM)
            print publicaPEM
            privadaPEM = pemSalida.crearPrivK(privada)
            archivo.crearArchivo("./"+carpeta+"/clave_rsa.priv", privadaPEM)
            print privadaPEM
        elif opFormat == 'd':
            derSalida = factory.salidaFormato("der")
            publicaDER = derSalida.crearPubK(publica)
            archivo.crearArchivo("./"+carpeta+"/clave_rsa.pub", publicaDER)
            print "No se muestra clave publica porque se crep en binario."
            privadaDER = derSalida.crearPrivK(privada)
            archivo.crearArchivo("./"+carpeta+"/clave_rsa.priv", publicaDER)
            print "No se muestra clave privada porque se crep en binario."

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
    print "El mensaje en texto plano es: ", desencriptar((d,n), m_encriptado, tipo)




