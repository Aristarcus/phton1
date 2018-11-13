# -*- coding: utf-8 -*-
"""
Created on Mon Nov 12 20:19:16 2018

@author: 1898716
"""

# Ecercises 6

# Execrcise 6.1

import os

directoy = os.getcwd()

print (os.listdir())


# Exercise 6.3

import os

file = open ("archivo_tres.txt", "w+")

while True:
    text = input (" Enter text to add to the file: ")
    if text.lower() == 'q':
        break
    file.write (text + '\n')
    
file.seek(0)

print ("This is what we have in the file")
print ()

allfile = file.read()

print (allfile)

file.close()


# Excercise 6.4

import os

file = open ("words.txt", "r")

dictionary = {}

for string in file:
    
    list = string.split()
    
    for word in list:
        word = word.lower()
        dictionary[word] =  dictionary.get(word,0) + 1
        
for word,value in sorted(dictionary.items()):
    print (word, ":", value)

file.close()

       