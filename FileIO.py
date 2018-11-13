# -*- coding: utf-8 -*-
"""
Created on Mon Nov 12 18:31:35 2018

@author: 1898716
"""

# File IO system

import os

print (os.getcwd())


myfiles = os.listdir()

print (myfiles)

if os.path.isfile ("turtlegraphs.py"):
    print ("File exists")
    

# Change directory using an absolute path

import os

os.chdir ("C:\\Users\\1898716\\new_dir")

print (os.getcwd())
print (os.listdir())

filehandle = open ("archivo_uno.txt", "r")

for line in filehandle:
    print (line, end ='')

filehandle. close()

# Writing in a file

import os

file = open("archivo_dos.txt", "r+")

file.write ("This is how we create a file in phyton\n")
file.write ("we will see how writing works\n")
file.write ("then we are going to read it\n")

file.seek (0)

s = file.read()

print (s)

file.seek (0)

while True:

    fileline = file.readline ()
    if fileline:
        print (fileline, end ='')
    else:
        break
    
file.seek (0)
    
filelines = file.readlines()

print (filelines)

file.close()


# Append mode

import os

file = open("archivo_dos.txt", "a")

file.write ("and now we are adding another line to it\n")

file.close()
