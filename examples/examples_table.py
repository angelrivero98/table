#-------------------------------------------------------------------------------
# Name:        examples_table.py
# Version:     0.2
#
# Purpose:     Examples for using table.py
#
# Author:      Ken Tong
#
# Created:     10/08/2015
#-------------------------------------------------------------------------------
# Querying a SQLite table and printing to the interpreter
# Specify None (leave out argument) for alignment
import sqlite3
from table import Table
conn = sqlite3.connect('customers_db.sqlite')
cur = conn.cursor()
cur.execute('SELECT Name, Network, Rating FROM shows')
print Table(cur.fetchall(), tuple(item[0] for item in cur.description))

# Querying a SQLite table and printing to the interpreter
# Specify center using 'c' for alignment
import sqlite3
from table import Table
conn = sqlite3.connect('customers_db.sqlite')
cur = conn.cursor()
cur.execute('SELECT FirstName, LastName, Address FROM customers')
print Table(cur.fetchall(), tuple(item[0] for item in cur.description), 'c')

# Saving formatted table to text file
# Specify left for alignment
import sqlite3
from table import Table
conn = sqlite3.connect('customers_db.sqlite')
cur = conn.cursor()
cur.execute('SELECT FirstName, LastName, Address FROM customers')
data =  Table(cur.fetchall(), tuple(item[0] for item in cur.description), 'left')
with open(r'customers.txt', 'w') as f:
    for row in data:
        f.write(row + '\n')