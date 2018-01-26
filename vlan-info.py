#!/usr/bin/env python3

# CLEAN UP REMARKS AND REFACTOR CODE.
"""
This file parses through a VLAN report provided from Solar
Winds that provides a list of every VLAN in an enterprise, then creates a
folder for each location based on the first 4 characters of the NODE_NAME.
In this folder, a CSV is created for each VLAN, the CSV lists every node
that a particular VLAN is located on and provides the info in the
column_headers listed below.
Enumeration of CSV headers show index and column headers as:
0 VLAN_ID
1 VLAN_NAME
2 NODE_NAME
3 NODE_IP_ADDRESS
"""

import csv, sys, os

def make_new_folder(folder):
    """To make a new folder"""
    if os.path.isdir(folder):
        pass
    else:
        os.mkdir(folder)

def write_csv(input, output, vlan):
    """
    Create a CSV file for each VLAN by location code.  Output will show each
    switch that the VLAN is on at that location.
    """
    with open(input) as file1:
        reader = csv.reader(file1)
        header_row = next(reader)
        new_header_row = (
            header_row[0].upper(),
            header_row[1].upper(),
            header_row[2].upper(),
            header_row[3].upper(),
            )
        with open(output, 'w', newline='') as file2:
            writer = csv.writer(file2)
            writer.writerow(new_header_row)
            for row in reader:
                new_row = (
                    row[0],
                    row[1],
                    row[2],
                    row[3],
                )    
                if row[0] == vlan and row[2][0:4] == site_code:
                    writer.writerow(new_row)
               
input_file = sys.argv[1]
site_code = sys.argv[2]
root_folder = sys.argv[3]
folder_path = root_folder + "//" +site_code

with open(input_file) as file1:
    reader = csv.reader(file1)
    header_row = next(reader)
    vlans = []
    for row in reader:
        vlans.append(row[0])
        vlan_list = set(vlans) # Remove duplicates from the list
        if row[2][0:4] == site_code: #match 1st 4 characters from row 2
            make_new_folder(site_code)
    
    for vlan in vlan_list:
        output_file = site_code + '\\vlan-' + vlan + '.csv'
        write_csv(input_file, output_file, vlan) # call the write_csv function