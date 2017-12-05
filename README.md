# Quick Start

Download the JSON version of the database at [data/microbe-directory.json](data/microbe-directory.json). The keys of the database are the MetaPhlAn2 species' names, which makes it easy to use the database downstream of taxonomic classifications.

# data/

This directory contains the database itself, as well as the scripts used to generate different versions of the database.

The main database is [microbe-directory.sql](data/microbe-directory.sql). The JSON and CSV versions of the database, [microbe-directory.json](data/microbe-directory.json) and [microbe-directory.csv](data/microbe-directory.csv), are generated from the sql database using [sql-to-json.py](data/sql-to-json.py) and [sql-to-csv.py](data/sql-to-csv.py), respectively.

We supplemented our manual curation by parsing the Microbe-Wiki for common keywords that could indicate particular features. We found that we could extract useful data for pathogenicity, biofilm formation, microbe shape, halophilicity,  spore formation, and metabolism. We were able to extract some subset of these features for 331 of the microbes that had been manually curated. This supplemental data can be found in CSV format here: [binomial_scraped.csv](data/binomial_scraped.csv).

# tutorial/

This directory contains a quick python example, [tutorial.py](tutorial/tutorial.py), which shows users how to use the JSON version of the database given a MetaPhlAn2 output file.

# Links

1. The Microbe Directory: http://microbe.directory/
2. Data GitHub: https://github.com/microbe-directory/microbe-directory
3. Website BitBucket: https://bitbucket.org/microbedb/microbedb
