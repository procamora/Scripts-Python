#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import platform


class Sistema():
    def Tipo(self, imprime=False):
        '''Sistema operativo del sistema'''
        tipoSistema = platform.uname()[0]
        if imprime:
            print(tipoSistema)
        return tipoSistema

    def Arq(self, imprime=False):
        '''Arquitectura del sistema'''
        tipoArq = platform.architecture()[0]
        if imprime:
            print(tipoArq)
        return tipoArq

    def Version(self, imprime=False):
        '''Version del sistema operativo'''
        tipoVersion = platform.release()
        if imprime:
            print(tipoVersion)
        return tipoVersion

    def VersionPy(self, imprime=False):
        '''Version del interprete de python'''
        tipoVersionPy = platform.python_version()
        if imprime:
            print(tipoVersionPy)
        return tipoVersionPy

    def BasadoEn(self, imprime=False):
        tipoBasadoEn =  platform.system()
        if imprime:
            print(tipoBasadoEn)
        return tipoBasadoEn



if __name__ == '__main__':
    prueba = Sistema()


    if prueba.Tipo() == "Windows":
        print("windows")
        #os.system("ipconfig")  
    elif prueba.Tipo() == "Linux":
        print("Linux")
        #os.system("ifconfig")
        
    #print prueba.Tipo.__doc__
    #help(prueba)
