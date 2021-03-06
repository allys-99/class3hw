#!/usr/bin/env python

import os

def getTestFile():
    retLine=""
    with open("testfile.txt", "r") as f2:
        for line2 in f2.readlines():
            retLine += line2
    return retLine

def printFeatureFile():
    print ("\n\n  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~ ")
    with open("feature.txt", "r") as f3r:
        for lines in f3r.readlines():
            print(lines)

def writeFeatureFile():
    print()
    testcol = getTestFile()
    testcollist = list(testcol.split(" "))
    with open("feature.txt", "r") as f3r:
        line3 = f3r.readline()
        if not line3:
            for i in range(len(testcollist)):
                #print("testcollist[",i,"]= ", testcollist[i])
                with open("feature.txt", "a") as f3a:
                    f3a.write(testcollist[i])
                    f3a.write("\n")
        else:
            f3r.seek(0)
            lines3 = f3r.readlines()
            open('feature.txt', 'w').close()
            #print (lines3)
            lines3len = len(lines3)
            for i in range(len(lines3)):
                lineFinal = "" 
                lineFinal =(lines3[i].strip() + '{:>10}'.format(testcollist[i].strip()) + "\n")
#                if len(lineFinal.strip()) > 2:
#                    print("lineFinal=",lineFinal)
                with open("feature.txt", "a") as f3a:
                        f3a.write(lineFinal)


print ("  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~ ")
# main
myfilename="housing.data.txt"
#if os.path.isfile(myfilename):
	#print("file exists")
#else:
	#print("no file")
open('feature.txt', 'w').close()
with open(myfilename, 'r') as file_handle:
    for line in file_handle.readlines():
        line_clean = line.replace('   ',' ').replace('  ',' ' )
        line_clean =line_clean.strip()
        values = line_clean.split(" ")
        print()
        print ("  ", end="")
        open('testfile.txt', 'w').close()
        for value in values:
            if '.' not in value:
                print(int(value), end="  ")
            else:
                print (float(value), end="  ")
            with open("testfile.txt", "a") as f2:
                f2.write(value)
                f2.write(" ")
        writeFeatureFile()
    printFeatureFile()

                

# identify what type of data each value is and cast it
# to the appropriate type, then print the new, properly-typed
# list to the screen
#  1', '273.0', '21.00', ==> 1, 273.0, 21.00

