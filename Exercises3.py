# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 19:36:48 2018

@author: 1898716
"""

#Exercises 3

#Exercise 3.1

countries = ['Canada', 'Rusia', 'Mexico', 'Poland']

print(countries)

countries.reverse()

print (countries)

countries.sort()

print (countries)

countries_02 = countries[:]

del countries_02[len(countries_02)-1]

OneCountry = countries_02.pop(0)

print (countries_02)

countries.append('Spain')

countries.extend (countries_02)

print (countries)
        
print ("Mexico is ", countries.count('Mexico'), " times in the list")

#Excercise 3.2

a = [1,1,2,3,5,8,13,21,34,55,89]

for i in range(len(a)):
    if a[i] < 5:
        print(a[i])
        
#Exercise 3.3

numberlist = []

for i in range (10):
    number = int(input("Enter a number: "))
    numberlist.append(number)
    
print (numberlist)

#Exercise 3.4

mylist = [5,10,15,20,25]
secondlist = []

secondlist.append (mylist[0])
secondlist.append(mylist[-1])

print (secondlist)

#Exercise 3.5

numberlist = []
listtocompare = [10,5,3]

for i in range (10):
    number = int(input("Enter a number: "))
    numberlist.append(number)
  
print (numberlist)
    

for i in range (len(numberlist)):
    if numberlist[i] in listtocompare:
        print (numberlist[i]," is in the list ", end = '')
        
print ()

    
#Execrise 3.6

numberlist = []

for i in range (10):
    number = int(input("Enter a number: "))
    numberlist.append(number)
  
print (numberlist)
    

for i in range (len(numberlist)):
    if numberlist[i] < 10:
        print ('{:3d}'.format(numberlist[i]), end = '')
        
print ()    
    
#Exercise 3.7

numberlist = []
secondlist = []

for i in range (10):
    number = int(input("Enter a number: "))
    numberlist.append(number)
  
print (numberlist)

for i in range (len(numberlist)):
    if numberlist[i] not in secondlist:
        secondlist.append(numberlist[i])
        
        
print (secondlist)

#Exercise 3.8

wordlist = []
quit = ['q', 'Q']

while True:
    word = input ("Enter a word (Q or q to finish): ")
    if word in quit:
        break
    wordlist.append(word)
    
print (wordlist)
wordlist.reverse()
print (wordlist)
                  
#Exercise 3.9

list_a = [1,1,2,3,5,8,13,21,34,55]
list_b = [1,2,3,4,5,6,7,8,9,10,11,12,13]
list_ab = list_a[:]
list_ab.extend(list_b)
list_c = []

for i in range (len(list_a)):
    if list_a[i] in list_b and list_ab.count(list_a[i]) == 1:
        list_c.append(list_a[i])
        
print (list_a)
print (list_b)
print (list_c)
        

