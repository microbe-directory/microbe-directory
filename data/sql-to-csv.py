#!/usr/bin/env python3

import sqlite3
import csv

connection = sqlite3.connect('microbe-directory.sql')
cursor = connection.cursor()

query = cursor.execute('SELECT * FROM Microbe;')
rows = cursor.fetchall()
columns = next(zip(*cursor.description))

with open('microbe-directory.csv', 'w') as file:
    writer = csv.writer(file, delimiter=',')
    writer.writerow(columns)
    writer.writerows(rows)
