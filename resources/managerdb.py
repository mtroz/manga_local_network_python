#!/usr/bin/env python3

import sqlite3

class ManageDB:

	def __init__(self, database_name):
		self.database_name = database_name
		self.con = sqlite3.connect(self.database_name)
	
	def cursor(self):
		return self.con.cursor()

	def commit(self):
		self.con.commit()

	def close(self):
		self.con.close()