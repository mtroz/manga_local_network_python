#!/usr/bin/env python3

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
		new_ip_format=[
				item for item in ip
		]
		return new_ip_format