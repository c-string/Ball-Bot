# CSV Translation lib
# This lib contains functions to convert CSV files into usable python data structures.

import csv

def CSV_To_Dict(csv_file):
    # Takes in a CSV file and translates it to a dict
    # Works for two column CSVs
    with open(csv_file, mode='r') as infile:
        reader = csv.reader(infile,quotechar='"', delimiter=',',quoting=csv.QUOTE_ALL, skipinitialspace=True)
        csv_dict = {rows[0]:rows[1] for rows in reader}
    print('Loaded %s' % csv_file)
    return csv_dict

def CSV_To_List(csv_file):
    # Takes in a CSV file and traslates it to a list
    # Works for single column CSVs
    with open(csv_file, mode='r') as infile:
        reader = csv.reader(infile,quotechar='"', delimiter=',',quoting=csv.QUOTE_ALL, skipinitialspace=True)
        csv_list = [rows[0] for rows in reader]
    print('Loaded %s' % csv_file)
    return csv_list