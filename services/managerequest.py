#!/usr/bin/env python3

import sqlite3

class ManageRequestDB:

	def create_table_ipmanchine(self):
		return '''CREATE TABLE ip_machine
					(machine text, ip text)'''

	def retrieve_all_table_name(self):
		return "SELECT name FROM sqlite_master WHERE type='table';"

	def retrieve_datas_ip_machine(self):
		return "SELECT hostname, ip FROM ip_machine"

	def retrieve_ip_from_machine(self,machine):
		return f"SELECT ip FROM ip_machine WHERE hostname='{machine}'"

	def retrive_machine_from_ip(self,ip):
		return f"SELECT hostname FROM ip_machine WHERE ip='{ip}'"

	def insert_multiple_ip_machine(self):
		return 'INSERT INTO ip_machine(hostname,ip) VALUES (?,?);'