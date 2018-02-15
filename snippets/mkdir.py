#!/etc/bin/env python3
import os, sys

#path_home = "c:\pm"
#print(path_home)

#new_folder = 'new_stuff'
#print(new_folder)

#new_path = os.path.join(path_home, new_folder)
#print(new_path)

def make_new_folder(folder):
    """To make a new folder"""
    if os.path.isdir(folder):
        print(str(make_new_folder) + ' already exists.')
        pass
    else:
        os.mkdir(folder)

make_new_folder("new_folder")
