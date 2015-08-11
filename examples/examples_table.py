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
print Table(cur.fetchall(), tuple(item[0] for item in cur.description), 'left')

# Saving formatted table to text file
import sqlite3
from table import Table
conn = sqlite3.connect('customers_db.sqlite')
cur = conn.cursor()
cur.execute('SELECT FirstName, LastName, Address FROM customers')
data =  Table(cur.fetchall(), tuple(item[0] for item in cur.description), 'center')
with open(r'customers.txt', 'w') as f:
    for row in data:
        f.write(row + '\n')