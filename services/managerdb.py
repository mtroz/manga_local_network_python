#!/usr/bin/env python3

import sqlite3, os, yaml 
from subprocess import run as subprocess_run
# [JG] Pense à rajouter toujours dans le module, un moyen de changer "l'origine" : c-à-d le chemin 
# Certaines classes d'exception existent dans Python dont celle-là : https://docs.python.org/3/library/exceptions.html#FileNotFoundError  

# Exemple YAML : 

DB = {} 
CheminLocal = "."

def charger( chemin, classes_authorisees=("machines") ): 
	global CheminLocal 
	with open( chemin, "r" ) as f: 
		doc_config = yaml.load_all( f, Loader=yaml.FullLoader ) 
		for item in doc_config:
			if item["database"]["class"] in classes_authorisees: 
				try: 
					DB[ item["database"]["class"] ] = ManageDB( 
						"{}/{}/{}".format( 
							CheminLocal, 
							item["database"]["path"], 
							item["database"]["destination"] 
						) 
					) 
				except FileNotFoundError: 
					pass # initialiser ici depuis et gérer un initialisation 
					# avec un fichier un squelette (exécuter SQL) 
					# exemple ManageDB.methode_statique( ..., ... )
					ManageDB.methode_statique(
							"{}/{}/{}".format( 
							CheminLocal, # à modifier, voir conf 
							item["database"]["path"], 
							item["database"]["destination"] 
							),
							item["database"]["skel"]
						)

class ManageDB: 

	def methode_statique( chemin, sql ): 
		pass 
		if not os.path.isfile(chemin):
			subprocess_run(
				[
					f"""
						bash -c "\
						touch {chemin}\
						"
					"""
				],shell=True)
		with open(sql,"r") as qry:
			con = sqlite3.connect(chemin)
			cur = con.cursor()
			cur.execute(qry.read())
			con.commit()
			con.close()


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

charger( "./config/databases.yml" )
