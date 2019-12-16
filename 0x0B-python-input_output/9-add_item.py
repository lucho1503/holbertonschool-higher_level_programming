#!/usr/bin/python3
import os.path
import sys

save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json = __import__('8-load_from_json_file').load_from_json_file

my_list = []
if os.path.exists("add_item.json"):
    my_list = load_from_json("add_item.json")

for args in sys.argv[1:]:
    my_list.append(args)

save_to_json_file(my_list, "add_item.json")
