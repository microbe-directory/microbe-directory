# data/

This directory contains the database itself, as well as the scripts used to generate different versions of the database.

The main database is `microbe-directory.sql`. The JSON and csv versions of the database, `microbe-directory.json` and `microbe-directory.csv`, are generated from the sql database using `sql-to-json.py` and `sql-to-csv.py`, respectively.
