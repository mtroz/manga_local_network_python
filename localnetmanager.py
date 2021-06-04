#!/usr/bin/env python3

""" 
	Appli de gestion de mon réseaux 
	---
	Ce script à pour but pour le moment de lister les machines de son réseau
	---
	1.0 
""" 
import os
import subprocess
CODES_RETOUR = {
	"OK": 0, 
	"ACTION_INCONNUE": 1, 
	"ACTION_ALERTE" : 2 
}

API = {
	"actions": {},
	"arguments": {}
}

def api(api_type,api_nom):
	global API
	if api_type not in API:
		API[api_type] = {}
	def decorateur(fct):
		try:
			API[api_type][api_nom] = (fct, fct.__doc__.split("---")[0])
		except Exception as err:
			print(f"Entrez d'api incorrect : {err}")
		return fct
	return decorateur

def lancer():
	import argparse
	m = GestionNetwork()
	app_nom, app_desc, app_version = [
		item.strip() for item in __doc__.split("---")
	]
	parser = argparse.ArgumentParser(
		prog=app_nom,
		description=app_desc
	)
	for argument in API["arguments"]:
		parser.add_argument(
			f"--{argument}", 
			required=False,
			type=API["arguments"][argument][0],  
			action="append", 
			help=API["arguments"][argument][1] 
		)
	parser.add_argument(
		"-v",
		"--version",
		action="version",
		version=f"{app_nom} - {app_version}"
	)
	parser.add_argument(
		'action', 
		help='quelle action entreprendre ? '+", ".join( 
			str(item) for item in API["actions"].keys()
		)
	)
	arguments = parser.parse_args()
	print(arguments)
	if arguments.action in API["actions"]: 
		API["actions"][arguments.action][0]( 
			m, 
			arguments 
		) 
		exit( CODES_RETOUR["OK"] ) # si on est parti avant, on part tranquillement
	else: 
		print( "cette action n'est pas connu !" ) 
		exit( CODES_RETOUR["ACTION_INCONNUE"] ) 
########-----------------------------------------------

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
	lancer()