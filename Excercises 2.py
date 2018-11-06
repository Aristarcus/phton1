# -*- coding: utf-8 -*-
"""
Created on Mon Oct 29 19:48:15 2018

@author: 1898716
"""
print ()
# 2.1
print ('{:^30}'.format("Excercise 2.1"))
print ()
for number in range (1,21):
    print ("{:3d} ".format(number), end ='')
print()    
    
#2.2
print ('{:^30}'.format("Excercise 2.2"))
print ()
for number in range (10,31,2):
    print ("{:3d} ".format(number), end ='')

print()

#2.3
print ('{:^30}'.format("Excercise 2.3"))
print ()
for number in range (100, 84, -1):
    print ("{:3d} ".format(number), end ='')
    
print()

#2.4
print ('{:^30}'.format("Excercise 2.4"))

divisible = int(input("Enter a number: "))

for value in range (1, divisible+1):
    if (divisible % value == 0):
        print ("divisible by : {:3d}".format (value))
        
print()

#2.5
print ('{:^30}'.format("Excercise 2.5"))

word = input ("Enter a string: ")

for letter in word:
    print (letter)
    
print () 

#2.6
print ('{:^30}'.format("Excercise 2.6"))

word = input ("Enter a string: ")

size = len(word)

for letter in range(size,0,-1):
    print (word [letter-1], end='')
    
print()

#2.7
print ('{:^30}'.format("Excercise 2.7"))

word = input ("Enter a string: ")
vowels ="aeiou"
i = 0
for letter in word:
    if letter in vowels:
        print (letter)
        i += 1
print (i, "vowels in", word)

#2.8

print ('{:^30}'.format("Excercise 2.8"))

word = input ("Enter a string: ")

i = 0
max = len (word)

while i < max:
    if word[i]!=word[max-i]:
        break
    print (word)
    