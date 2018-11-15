# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 18:55:04 2018

@author: 1898716
"""

# Excercises 7

#Exercises 7.1
 
try:
    number = int(input (" Please give me an integer number :"))
    print (number)
except ValueError:
    print (" You gave a string ")
else:
    print (" The integer is ", number)
    
# Exercises 7.3

divisor = int(input( " We are dividing 250, give me the divisor :"))

try:
    result = 250/divisor
except:
    print ("A number cannot be divided by zero")
else:
    print (result)
    
# Exercise 7.4

