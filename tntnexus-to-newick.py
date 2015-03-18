#-*- coding: utf-8 -*-
#! /usr/bin/python

print """
	Convert nexus tree files to Newick format
	Generally, programs as Figtree require an input file written in newick format, thus it is expecting a ".nwk" or ".tre" file
	"""
	
#Importo módulo para manejo de directorio

import glob

directory = glob.glob("*.nex")

print directory

#para todos los archivos i que estén en directory, les voy a abrir un puntero de escritura en formato newick y los voy a abrir y leer como nexusfile.

for i in range(0, len(directory)):
	arbol_tre = open ((str(directory[i]) + ".nwk"), 'w')
	with open (directory[i]) as nexusfile:
			arbol_nex = nexusfile.readlines()
	print str(len(arbol_nex))
	
	arbolnexcont = len(arbol_nex)

#voy a extraer todo lo que comprende el arbol con el soporte o el tree_tagged del archivo nexus de tnt

	for position in range(0, (arbolnexcont)):
		
		position1 = arbol_nex [position].find (";")
		
		position2 = arbol_nex [position].find ("(")
		
		arbol1 = arbol_nex[position][position2:position1]
		
		if arbol1 !='': 
			
			arbol2= arbol1.replace("\'","")
			print(arbol2)
			arbol_tre.write (arbol2)
			arbol_tre.write (' ;')	
			
	arbol_tre.close ()

#Imprimo mensaje de salida para el usuario

print '\n'
print '\n'	
print "Files successfully converted into newick format"
print '\n'
print '\n'
			
		
			



