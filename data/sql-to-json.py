#!/usr/bin/env python3

import sqlite3
import json

connection = sqlite3.connect('microbe-directory.sql')
cursor = connection.cursor()

query = cursor.execute('SELECT * FROM Microbe;')
rows = cursor.fetchall()
columns = next(zip(*cursor.description))

data = {row[0]: dict(zip(columns, row)) for row in rows}
with open('microbe-directory.json', 'w') as file:
    file.write(json.dumps(data))
