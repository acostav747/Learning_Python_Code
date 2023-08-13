#! /usr/bin/env python3

#############################
#   L E A R N  C O D : 0 3  #
#############################


class usar:

    def filtroGeneral():

        simbolos = "!@#$%¨&*()"

        codigo = [ord(c) for c in simbolos if ord(c) > 127]

        return codigo

    def FiltroConMapa():

        simbolos = "!@#$%¨&*()"

        codigo = list(filter(lambda c: c > 127, map(ord, simbolos)))
        
        return codigo
