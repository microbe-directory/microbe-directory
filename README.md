# Quick Start

Download the JSON version of the database at [data/microbe-directory.json](data/microbe-directory.json). The keys of the database are the MetaPhlAn2 species' names, which makes it easy to use the database downstream of taxonomic classifications.

# data/

This directory contains the database itself, as well as the scripts used to generate different versions of the database.

The main database is `microbe-directory.sql`. The JSON and csv versions of the database, `microbe-directory.json` and `microbe-directory.csv`, are generated from the sql database using `sql-to-json.py` and `sql-to-csv.py`, respectively.

# tutorial/

This directory contains a quick python example, `tutorial.py`, which shows users how to use the JSON version of the database given a MetaPhlAn2 output file.
