#!/usr/bin/env python3

""" 
	Appli de gestion de mon réseaux 
	---
	Ce script à pour but pour le moment de lister les machines de son réseau
	---
	1.0 
""" 
from apyzme import api, lancer
from services.managerservices import ManagerService

class GestionNetwork:

	def __init__(self):
		self.manager_service = ManagerService()

	@api( "actions","listip" )
	def action_command_list_ip( self, arguments ):
		"""Récupérer la liste des machines
		---
		Récupérer la liste des machines retour de l'action [{nom_machine, ip_machine}]"""

		#En cours de développeme

	@api( "actions", "mapping" )
	def action_command_scan_lan( self, arguments ):
		"""Lance un scan du réseau local, récupération des machines et de leurs ip
		---
		Action dans l'objectif est de faire un mapping du réseau et d'alimenter la base de donnée avec les informations"""

		print(self.manager_service.start_mapping_network())



########-----------------------------------------------
if __name__=="__main__":
	lancer(GestionNetwork)