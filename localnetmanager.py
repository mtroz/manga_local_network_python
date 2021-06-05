#!/usr/bin/env python3

""" 
	Appli de gestion de mon réseaux 
	---
	Ce script à pour but pour le moment de lister les machines de son réseau
	---
	1.0 
""" 
from apyzme import api, lancer
from resources.managerservices import ManagerService
import subprocess

class GestionNmap:

	def nmap_scan_ips(self, ip):
		return f"""
				bash -c "\
				nmap -sn {ip}/24\
				| grep Nmap\
				| grep \\)$\
				"
			"""

	def format_list_retour_nmap(self, list_ips):
		list_formated = [
			self.format_retour_ip(item) for item in list_ips
		]

		return list_formated

		

	def format_retour_ip(self, ip):
		new_ip_format = ""
		ip = ip.split(" ")
		ip = ip[len(ip)-2:]
		ip[1] = ip[1][1:-1]
		new_ip_format += " ".join(
			[
				item for item in ip
			]
		)
		return new_ip_format
########-----------------------------------------------
class GestionNetwork:

	def __init__(self):
		self.manage_ip = GestionNmap()

	@api( "actions","listip" )
	def action_command_list_ip( self, arguments ):
		"""Description courte de l'action test
		---
		Description approfondie de l'argument"""
		p = subprocess.run(
			[
				self.manage_ip.nmap_scan_ips("192.168.1.1")
			],
			stdout=subprocess.PIPE,
			shell=True
		)
		list_line_output = (
			[ item for item in p.stdout.decode( "utf-8" ).split("\n") ]
		)
		list_output_format = self.manage_ip.format_list_retour_nmap(list_line_output[:-1])
		print(
			"Listes des adresse ip : \n"
			+ "\n".join(
				[item for item in list_output_format]
			)
		)

########-----------------------------------------------
if __name__=="__main__":
	lancer(GestionNetwork)