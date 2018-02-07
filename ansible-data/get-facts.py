#!/usr/bin/env python3
import json, openpyxl, glob, sys
"""
This was written in Python 3.6.  The purpose of this file is to iterate
through JSON files that were created using Ansible ios_facts and nxos_facts
modules and return data that can be used to populate an Excel spreadsheet
using the openpyxl module.
"""

def get_ios_facts(file):
    """
    Read json formatted file that is output of Ansible ios_facts module.
    Returns a list 'ios_facts' that will be used to fill in spreadsheet.
    """
    with open(file) as file_object:
        data = json.load(file_object)
        hostname = str(data['ansible_facts']['ansible_net_hostname'])
        serial_number = str(data['ansible_facts']['ansible_net_serialnum'])
        version = str(data['ansible_facts']['ansible_net_version'])
        for i in data['ansible_facts']['ansible_net_interfaces']['Loopback0']['ipv4']:
            for k, v in i.items():
                if k == 'address':
                    mgmt_ip = v
        ios_facts = [hostname, serial_number, version, mgmt_ip]
        return ios_facts

def get_nxos_facts(file):
    """
    Read json formatted file that is output of Ansible nxos_facts module.
    Returns a list 'nxos_facts' that will be used to fill in spreadsheet.
    """
    with open(file) as file_object:
        data = json.load(file_object)
        hostname = str(data['ansible_facts']['ansible_net_hostname'])
        serial_number = str(data['ansible_facts']['ansible_net_serialnum'])
        version = str(data['ansible_facts']['ansible_net_version'])
        mgmt_ip = str(data['ansible_facts']['ansible_net_interfaces']['loopback0']['ipv4']['address'])
        nxos_facts = [hostname, serial_number, version, mgmt_ip]
        return nxos_facts


def iter_files():
    """
    Used to iterate through specific types of json files and run 
    'get_***_facts' module on each file.  Each local_***_facts list is
    inserted into the global_facts list.  The global_facts list needed
    to have the other local_***_facts  lists nested in order to get the
    openpyxl append feature to work correctly.
    """
    global_facts = []
    for file in sorted(glob.glob('*ios_facts.json')):
        local_ios_facts = get_ios_facts(file)
        global_facts.insert(1, local_ios_facts)

    for file in sorted(glob.glob('*nxos_facts.json')):
        local_nxos_facts = get_nxos_facts(file)
        global_facts.insert(1, local_nxos_facts)
    return(global_facts)


def write_spreadsheet():
    """
    Openpyxl module used to load a template spreadshet ('tempalate.xls')
    and update it with the data returned from the get_ios_facts and
    get_nxos_facts functions.
    """
    wb = openpyxl.load_workbook('template.xlsx')
    ws = wb.active
    ws.title = 'Network Devices'
    global_facts = iter_files()
    for facts in global_facts:
        ws.append(facts)
    wb.save(sys.argv[1])

if __name__ == '__main__':
    if len(sys.argv) > 1:
        write_spreadsheet()
    else:
        print("python get-facts.py filename")