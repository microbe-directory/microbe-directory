#!/usr/bin/env python3

import sqlite3
import json

connection = sqlite3.connect('microbe-directory.sql')
cursor = connection.cursor()

query = cursor.execute('SELECT * FROM Microbe;')
rows = cursor.fetchall()
columns = next(zip(*cursor.description))

 # row[7] is species name
 # replace ' ' with '_' (consistent w/ metaphlan)
data = {row[7].replace(' ', '_'): dict(zip(columns, row)) for row in rows}

#print(data['Ipomoea_begomovirus_satellite_DNA_beta'])

with open('microbe-directory.json', 'w') as file:
    file.write(json.dumps(data).replace('N/A', 'A')) # replace is bc json.dumps is esacping this for some reason
