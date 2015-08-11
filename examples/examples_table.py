#-------------------------------------------------------------------------------
# Name:        examples_table.py
# Version:     0.1
#
# Purpose:     Examples for using table.py
#
# Author:      Ken Tong
#
# Created:     10/08/2015
#-------------------------------------------------------------------------------

# Querying a SQLite table and printing to the interpreter
import sqlite3
from table import Table
conn = sqlite3.connect('customers_db.sqlite')
cur = conn.cursor()
cur.execute('SELECT FirstName, LastName, Address FROM customers')

#Print Left Justified
print Table(cur.fetchall(), tuple(item[0] for item in cur.description), 'left')