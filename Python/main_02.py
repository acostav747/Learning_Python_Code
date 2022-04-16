#! /usr/bin/env python3

#############################
#   L E A R N  C O D : 0 2  #
#############################

class usar:
   
    def codigoA():

        simbolos = "@#$%&"
        codigos = []    

        for simbolo in simbolos:
            codigos.append(ord(simbolo))
        
        return codigos

    def codigoB():

        simbolos = "@#$%&"
        codigos = [ord(simbolo) for simbolo in simbolos]

        return codigos

        
