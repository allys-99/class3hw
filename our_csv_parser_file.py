#!/usr/bin/env python

import os

myfilename="housing.data.txt"

if os.path.isfile(myfilename):
	print("file exists")
else:
	print("no file")
with open(myfilename, 'r') as file_handle:
	line = file_handle.readline()
	for line in file_handle.readlines():
		line_clean = line.replace('   ',' ').replace('  ',' ' )
		line_clean =line_clean.strip()
		values = line_clean.split(" ")
		print(values)
		for value in values:
			print (value)
# identify what type of data each value is and cast it
# to the appropriate type, then print the new, properly-typed
# list to the screen
#  1', '273.0', '21.00', ==> 1, 273.0, 21.00

