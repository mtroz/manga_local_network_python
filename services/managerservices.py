#!/usr/bin/env python3

from .managerdb import ManageDB
from .managerequest import ManageRequestDB
from .gestionnmap import GestionNmap
import subprocess

class ManagerService:



	def __init__(self):
		self.gestionnmap = GestionNmap()
		self.managedb = ManageDB("./database/mapping_network.db")
		self.managerequest = ManageRequestDB()

#----------------Service listage des machines-------------------

	def get_ip_list(self):
		""" 
			Fonction qui gére le service de récupération des Machines ainsi que leurs adresse IP
			----
		"""
		print ("Fonction en cours de développement")

#----------------Service de Mapping----------------------------

	def start_mapping_network(self):
		"""
			Fonction qui gére le service de mapping du réseau
			----
		"""

		print("Mapping du réseau en cours")

		p = subprocess.run(
			[
				self.gestionnmap.nmap_scan_ips("192.168.1.1")
			],
			stdout=subprocess.PIPE,
			shell=True
		)

		list_line_output = (
			[ item for item in p.stdout.decode( "utf-8" ).split("\n") ]
		)

		list_output_format = self.gestionnmap.format_list_retour_nmap(list_line_output[:-1])
		
		cursordb = self.managedb.cursor()

		list_machines = cursordb.execute(self.managerequest.retrieve_datas_ip_machine()).fetchall()
		
		if(len(list_machines)) > 0:
			self.Insert_or_Update_machines(list_output_format,list_machines,cursordb)	
		else:
			cursordb.executemany(self.managerequest.insert_multiple_ip_machine(),list_output_format)
		

		self.managedb.commit()
		self.managedb.close()


		return list_output_format

	# Fonction à moitier fini il manque la parti update (en cours)
	def Insert_or_Update_machines( self,list_machines_nmap, list_machines_db, cursor ):
		list_update = []
		list_insert = []
	
		list_insert = [
				machine for machine in list_machines_nmap 
				if not self.check_already( machine, list_machines_db )
		]

		if len( list_insert ) > 0:
			cursor.executemany( self.managerequest.insert_multiple_ip_machine(),list_insert )
	
		
		list_update = [
			machine for machine in list_machines_nmap
			if (self.check_already( machine, list_machines_db ) & self.check_needed_update(machine, list_machines_db))	
		]

		if len( list_update ) > 0:
			list_update = [item[::-1] for item in list_update]
			cursor.executemany( self.managerequest.update_up_machine(),list_update )
		
	# Vérifie si la machine et les données existe déjà en base
	def check_already( self,machine, list_machines_db ):
		for item in list_machines_db:
			if machine[0] == item[0]:
				return True
		return False

	# Vérifie si un update est nécessaire pour les données en base (à développer)
	def check_needed_update( self, machine, list_machines_db ):
		for item in list_machines_db:
			if machine[0] == item[0] and machine[1] != item[1]:
				return True
		return False

#-------------------------------------------------------------------------------------