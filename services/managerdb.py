#!/usr/bin/env python3

import sqlite3
import os
# [JG] Pense à rajouter toujours dans le module, un moyen de changer "l'origine" : c-à-d le chemin 
# Certaines classes d'exception existent dans Python dont celle-là : https://docs.python.org/3/library/exceptions.html#FileNotFoundError  

CheminLocal = "/home/persoen/projets/python/manga_local_network_python/database" # "." = dossier courant, tel que "./" 
DatabseName = "mapping_network.db"

class ManageDB:

	def __init__(self):
		global CheminLocal  
		self.chemin = f"{CheminLocal}/{DatabseName}" 
		if not os.path.isfile( self.chemin ): 
			raise FileNotFoundError( 
				f"la base n'existe pas à '{self.chemin}' : impossible d'utiliser une base non-initialisée" 
			) 
		self.con = sqlite3.connect(self.chemin)
	
	def cursor(self):
		return self.con.cursor()

	def commit(self):
		self.con.commit()

	def close(self):
		self.con.close()
"""
if __name__=="__main__":
	managedb = ManageDB()

	cursorDB = managedb.cursor()

	cursorDB.execute('''CREATE TABLE ip_machine
					(machine text NOT NULL PRIMARY KEY, ip text)''')

	managedb.commit()
	managedb.close()
"""