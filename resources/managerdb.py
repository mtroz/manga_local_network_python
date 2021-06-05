#!/usr/bin/env python3

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