#!/usr/bin/env python

from util.factory import Factory
from util.files import Archivos
from rsa.rsa import RSA

class Opera:

    def __init__(self, publica, privada):
        self.publica = publica
        self.privada = privada

    def leerFormatoClaves(self):
        carpeta = "claves"
        factory = Factory()
        archivo = Archivos()
        archivo.crearCarpeta(carpeta)
        opFormat = 'x'
        while opFormat != 'p' and opFormat != 'd':
            opFormat = raw_input("Formato de salida [p] PEM o [d] DER: ")
            if opFormat == 'p':
                pemSalida = factory.salidaFormato("pem")
                publicaPEM = pemSalida.crearPubK(self.publica)
                archivo.crearArchivo("./"+carpeta+"/clave_rsa.pub", publicaPEM)
                print publicaPEM
                privadaPEM = pemSalida.crearPrivK(self.privada)
                archivo.crearArchivo("./"+carpeta+"/clave_rsa.priv", privadaPEM)
                print privadaPEM
                print ""
                if False:   
                    print "Leyendo archivo..."
                    contenido = archivo.leerArchivo("./claves/clave_rsa.pub")
                    print pemSalida.cargarPubK(contenido, "RSA PUBLIC KEY")
                    print ""
                    contenido = archivo.leerArchivo("./claves/clave_rsa.priv")
                    print pemSalida.cargarPubK(contenido, "RSA PRIVATE KEY")        
            elif opFormat == 'd':
                derSalida = factory.salidaFormato("der")
                publicaDER = derSalida.crearPubK(self.publica)
                archivo.crearArchivo("./"+carpeta+"/clave_rsa.pub", publicaDER)
                print "No se muestra clave publica porque se creo en binario."
                privadaDER = derSalida.crearPrivK(self.privada)
                archivo.crearArchivo("./"+carpeta+"/clave_rsa.priv", privadaDER)
                print "No se muestra clave privada porque se creo en binario."
                if False:
                    print "Leyendo archivo..."
                    contenido = archivo.leerArchivo("./claves/clave_rsa.pub")
                    print derSalida.cargarPubK(contenido)
                    print ""
                    contenido = archivo.leerArchivo("./claves/clave_rsa.priv")
                    print derSalida.cargarPubK(contenido)  

    def imprimirClavesP(self):
        print ""
        print "Tu clave publica sin formato es (e,n): "
        print self.publica
        print ""
        print "Tu llave privada sin formato es (d,n): "
        print ""
        print self.privada
        print ""

    def probarEncDesc(self):
        rsa = RSA()
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

        m_encriptado = rsa.encriptar(self.publica, mensaje, tipo)

        print ""
        print "El mensaje encriptado es: "
        if tipo == 0:
            print ''.join(map(lambda x: str(x), m_encriptado))
        else:
            print m_encriptado   
        
        self.probarDesencriptacion(m_encriptado,tipo)

    def probarDesencriptacion(self,mensaje,tipo):
        rsa = RSA()
        (_,n,d,_,_) = self.privada
        print ""
        raw_input("Presiona ENTER para probar la desencriptacion...")
        print ""
        print "Desencriptando mensaje con su llave privada..."
        print ""
        print "El mensaje en texto plano es: ", rsa.desencriptar((d,n), mensaje, tipo) 