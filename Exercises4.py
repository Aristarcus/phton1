# -*- coding: utf-8 -*-
"""
Created on Wed Nov  7 19:10:47 2018

@author: 1898716
"""

# Exercises 5

# Exercise 5.1

student_marks = {'Joe' : 15, 'Mary' : 20, 'Ralph' : 18, 'Annita' : 19 }

print (student_marks)

student_marks ['Rob'] = 16

student_marks ['Joe'] = 17   

if 'Mary' in student_marks:
    print ("Mary is included")
else:
    print ("Mary is not included")
    
name = input ("Who are you looking for: ")

if name in student_marks:
    print (name, " is included")
else:
    print (name, " is not included")
    
for key,value in student_marks.items():
    print (key,value)
    

           