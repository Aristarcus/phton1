# -*- coding: utf-8 -*-
"""
Created on Mon Oct 29 20:09:37 2018

@author: 1898716
"""

number = int (input("Enter an integer: "))

for row in range (1, number):
    for col in range (1,11):
        print ('{:5d}'.format(row*col), end ="")
    print ()