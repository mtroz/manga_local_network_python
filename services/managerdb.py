#!/usr/bin/env python3

import sqlite3, os, yaml 
# [JG] Pense à rajouter toujours dans le module, un moyen de changer "l'origine" : c-à-d le chemin 
# Certaines classes d'exception existent dans Python dont celle-là : https://docs.python.org/3/library/exceptions.html#FileNotFoundError  

# Exemple YAML : 

DB = {} 

def charger( chemin, classes_authorisees=(,) ): 
	global CheminLocal 
	with open( chemin, "r" ) as f: 
		doc_config = yaml.load_all( f, Loader=yaml.FullLoader ) 
		for item in doc_config: 
			if item["class"] in classes: 
				try: 
					DB[ item["class"] ] = ManageDB( 
						"{}/{}/{}" % ( 
							CheminLocal, # à modifier, voir conf 
							item["path"], 
							item["destination"] 
						) 
					) 
				except FileNotFoundError: 
					pass # initialiser ici depuis et gérer un initialisation 
					# avec un fichier un squelette (exécuter SQL) 
					# exemple ManageDB.methode_statique( ..., ... ) 

# charger( "./config/databases.yml" ) 

class ManageDB: 

	def methode_statique( chemin, sql ): 
		pass 

	### ----------------- 

	def __init__(self, chemin ): 
		self.chemin = chemin
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