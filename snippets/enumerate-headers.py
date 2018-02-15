#!/usr/bin/env python3

import csv, sys
"""
Quick script in Python3 to enumerate the header row and provide the index
position of each header.
"""

def csv_headers(filename):
    """Enumerate headers of a CSV file."""
    try:
        with open(filename) as file_object:
            reader = csv.reader(file_object,delimiter=',')
            header_row = next(reader)
    except FileNotFoundError:
        print("That file doesn't exist...Please povide a valid file.")
    else:
        for index, column_header in enumerate(header_row):
            print(index, column_header)
            
if __name__ == '__main__':
    if len(sys.argv) > 1:
        filename = sys.argv[1]
        csv_headers(filename)
    else:
        print("python csv_headers.py filename")
