#!/usr/bin/env python3

import sqlite3

# [JG] Pense à rajouter toujours dans le module, un moyen de changer "l'origine" : c-à-d le chemin 
# Certaines classes d'exception existent dans Python dont celle-là : https://docs.python.org/3/library/exceptions.html#FileNotFoundError  

CheminLocal = "." # "." = dossier courant, tel que "./" 

class ManageDB:

	def __init__(self, database_name):
		global CheminLocal 
		self.database_name = database_name 
		self.chemin = f"{CheminLocal}/{self.database_name}" 
		if not os.path.isfile( self.chemin ): 
			raise FileNotFoundError( 
				f"la base n'existe pas à '{self.chemin}' : impossible d'utiliser une base non-initialisée" 
			) 
		self.con = sqlite3.connect(self.database_name)
	
	def cursor(self):
		return self.con.cursor()

	def commit(self):
		self.con.commit()

	def close(self):
		self.con.close()