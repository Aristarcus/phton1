# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 18:37:45 2018

@author: 1898716
"""

#Lists

mylist01 =[1,2,3,4,5,6,7,8,9,10]
mylist02 = [1,3,5,2,4,7]
mylist03 = [4,'ASI',4.6, 'B']
mylist04 = [1,2,'a',[2,3,4],'b']

element01 = mylist01[3]
print (element01)

element02 = mylist04[3]
print(element02)

myvar = mylist01[2:6]
print(myvar)
print(myvar[1])

mylist = []
secondlist = []

for i in range(4):
    name = input ("Enter a name: ")
    mylist.append(name)
    
mylist.sort()

secondlist.append(mylist.pop())

print (mylist)
print (secondlist)

    
    