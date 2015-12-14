#!/bin/env python
# -*- coding: utf-8 -*-
import platform
#borrar luego

class Sistema():
	def Tipo(self, Imprime="Opcional"):
		'''Sistema operativo del sistema'''
		tipoSistema = platform.uname()[0]
		return tipoSistema

	def Arq(self, Imprime="Opcional"):
		'''Arquitectura del sistema'''
		tipoArq = platform.architecture()[0]
		return tipoArq

	def Version(self, Imprime="Opcional"):
		'''Version del sistema operativo'''
		tipoVersion = platform.release()
		return tipoVersion

	def VersionPy(self, Imprime="Opcional"):
		'''Version del interprete de python'''
		tipoVersionPy = platform.python_version()
		return tipoVersionPy

	def BasadoEn(self, Imprime="Opcional"):
		tipoBasadoEn =  platform.system()
		return tipoBasadoEn


prueba = Sistema()


if prueba.Tipo() == "Windows":
	print "win"
	#os.system("ipconfig")  
elif prueba.Tipo() == "Linux":
	print "Lin"
	#os.system("ifconfig")
	
#print prueba.Tipo.__doc__
#help(prueba.Tipo)
