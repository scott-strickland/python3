#!/usr/bin/env python3
"""
The purpose of this file is to aggregate CIDR ranges in to the longest
inclusive range.  It does this by reading in a single column CSV file with
the CIDR ranges listed.  Written in python 3.6.2
"""
import csv
import sys
import netaddr

def get_prefix_list():
    """
    Read in the csv file that is passed as argument.  Iterate through rows to
    create a list of unique CIDR range that is returned as prefix_list.
    """
    try:
        with open(filename) as file_object:
            reader = csv.reader(file_object)
            prefix_list, used_networks = [], []
            for row in reader:
                if row not in used_networks:
                    used_networks.append(row[0])
            for network in used_networks:
                prefix_list.append(network)
            return prefix_list            
    except FileNotFoundError:
            print("That file doesn't exist...Please provide a valid file.")

def get_cidr_range():
    """
    Iterate through the prefix_list to return a list of aggregated CIDR summaries.
    """
    cidr_range = netaddr.IPSet(prefix_list)
    for cidr in cidr_range.iter_cidrs():
        print(cidr)
    
if __name__ == '__main__':
    if len(sys.argv) > 1:
        filename = sys.argv[1]
        prefix_list = get_prefix_list()
        get_cidr_range()
    else:
        print("python prod-prefixes.py filename")
