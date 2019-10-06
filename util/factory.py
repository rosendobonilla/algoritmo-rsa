#!/usr/bin/env python

from formats.der import DER
from formats.pem import PEM

class Factory:

    def salidaFormato(self, formatoSalida):
        formato = {"der": DER(), "pem": PEM()}

        return formato[formatoSalida]
