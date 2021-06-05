#!/usr/bin/env python3

import sqlite3

class ManageRequestDB:

	def create_table_ipmanchine():
		return '''CREATE TABLE ip_machine
					(machine text, ip text)'''

	def retrieve_all_table_name():
		return "SELECT name FROM sqlite_master WHERE type='table';"

	def retrieve_datas_ip_machine():
		return "SELECT machine, ip FROM ip_machine"

	def retrieve_ip_from_machine(machine):
		return f"SELECT ip FROM ip_machine WHERE machine='{machine}'"

	def retrive_machine_from_ip(ip):
		return f"SELECT machine FROM ip_machine WHERE ip='{ip}'"

	def insert_multiple_ip_machine():
		return 'INSERT INTO ip_machine VALUES (?,?);'

class ManageDB:

	def __init__(self, database_name):
		self.database_name = database_name
		self.con = sqlite3.connect(self.database_name)
	
	def cursor():
		return self.con.cursor()

	def commit():
		self.con.commit()

	def close():
		self.con.close()