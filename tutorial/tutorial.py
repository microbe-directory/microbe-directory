#!/usr/bin/env python3

import json
import re

db_path = '../data/microbe-directory.json'
metaphlan2_output_path = 'metaphlan2_merged_abundance_table.txt'

# **************************************************
# Load The Microbe Directory database
# **************************************************

with open(db_path, 'r') as f:
    db = json.loads(f.read()) # contains dict of database

db['Escherichia_coli'] # reference via MetaPhlAn2 species name

# **************************************************
# Parse MetaPhlAn2 and look up results in The Microbe Directory
# **************************************************

with open(metaphlan2_output_path, 'r') as f:
    metaphlan2_output = f.read()

metaphlan2_species_list = re.findall('s__([^\t|]+)', metaphlan2_output) # only match the species name
for metaphlan2_species in metaphlan2_species_list:
    if '_unclassified' in metaphlan2_species: continue # reject those genus' metaphlan2 couldn't classify

    print(db[metaphlan2_species])
