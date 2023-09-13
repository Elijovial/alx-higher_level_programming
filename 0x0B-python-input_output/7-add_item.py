#!/usr/bin/python3
"""Script that adds all arguments to a Python list, and then save them to a file"""

import sys
from os import path

# Import the functions from the previous tasks
from 5-save_to_json_file import save_to_json_file
from 6-load_from_json_file import load_from_json_file

# The file name to store the list
filename = "add_item.json"

# Check if the file exists and load the list from it
if path.exists(filename):
    my_list = load_from_json_file(filename)
else:
    my_list = []

# Add the arguments to the list
for arg in sys.argv[1:]:
    my_list.append(arg)

# Save the list to the file as a JSON representation
save_to_json_file(my_list, filename)

