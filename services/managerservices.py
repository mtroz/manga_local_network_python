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

	def get_ip_list(self):
		""" 
			Fonction qui gére le service de récupération des Machines ainsi que leurs adresse IP
			----
		"""
		print ("Fonction en cours de développement")

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
		cursordb.executemany(self.managerequest.insert_multiple_ip_machine(),list_output_format)
		self.managedb.commit()
		self.managedb.close()


		return list_output_format
