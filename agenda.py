#!/bin/env python
# -*- coding: utf-8 -*-
import sys
if '../librerias/' not in sys.path:
	sys.path.append('../')
from librerias.ConexionPyMySQL import run_query
from librerias.SSH_Forward import TunelSSH

import unicodedata

def elimina_tildes(cadena):
	'''
	http://guimi.net/blogs/hiparco/funcion-para-eliminar-acentos-en-python/
	Cambiamos caracteres modificados (áüç...) por los caracteres base (auc...)
	'''
	s = ''.join((c for c in unicodedata.normalize('NFD',unicode(cadena)) if unicodedata.category(c) != 'Mn'))
	return s.decode()
	#return ''.join((c for c in unicodedata.normalize('NFD', cadena) if unicodedata.category(c) != 'Mn'))


inicio = '''<?xml version="1.0" encoding="utf-8"?>
<root_group>
	<group display_name="All Contacts" ring="" />
	<group display_name="Blacklist" ring="" />
</root_group>
<root_contact>
'''


tunel = TunelSSH('SERVER', 22, 'USERNAME', 'PASSWORD', '127.0.0.1', 3306)

query = '''SELECT firstname, lastname, phonenumber, mobilenumber
FROM CONTACTOS
WHERE firstname IS NOT NULL AND phonenumber IS NOT NULL'''
a = run_query('localhost', 'root', 'PASSWORD', 'TABLA_CONTACTOS', query, DB_PORT=tunel.Iniciar())

tunel.Cerrar()


listaC = list()
for i in a:
	texto = '\t<contact display_name="%s %s" office_number="%s" mobile_number="%s" other_number="" line="3" ring="Auto" group_id_name="All Contacts" />'%(i['firstname'], i['lastname'], i['phonenumber'], i['mobilenumber'])
	listaC.append(elimina_tildes(texto).replace('None','').replace('  ',' '))

with open("myfile.xml", 'w') as f:
	f.write(inicio)
	f.write("\n".join(map(lambda x: str(x), listaC)))
	f.write('\n</root_contact>')
#f.write("\n".join(map(lambda x: str(x), listaC)) + "\n")
