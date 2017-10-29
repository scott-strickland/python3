#!/usr/bin/env python3
import requests, sys
"""
The purpose of this file is to perform a lookup of the MAC vendor based
on the OID.  The lookup is performed using the API provided by macvendors.com.
Written in Python 3.6.2.
"""

def get_mac_vendor():
    try:
        with open(filename, 'r') as file_object:
            files = file_object.read()
            rows = files.split('\n')
    except FileNotFoundError:
        print("That file doesn't exist...Please provide a valid file.")
    else:
        for row in rows:
            url = 'http://api.macvendors.com/' + row
            r = requests.get(url)
            for i in r:
                print(row + '\t' + i.decode('UTF-8'))

if __name__ == '__main__':
    if len(sys.argv) > 1:
        filename = sys.argv[1]
        get_mac_vendor()
    else:
        print("python mac-lookup.py file_name")