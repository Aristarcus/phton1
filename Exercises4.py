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
    

# Exercises 5.2

student_marks = {}

while True:
    name = input ("Student name: ")
    
    if name == "Q" or name == 'q':
        break
    
    mark = int(input("Mark received: "))
    
    student_marks [name] = mark

for key,value in student_marks.items():
    print (key,value)

#Exercise 5.3
  
parsed_string = {}

string_to_parse = input ("Give me a string to parse: ")

for letter in string_to_parse:
    letter = letter.lower()
    if letter.strip():
        parsed_string[letter] = parsed_string.get(letter,0) + 1
    
for key,value in sorted(parsed_string.items()):
    print (key, ":", value, end = '')
     
# Exercise 5.4

fruits = {"Apples" : 10, "Bananas" : 20, "Oranges" : 15, "Raisins" : 5, "Apricots" : 8}

while True:
    print ("     Menu")
    print ("1. Display Inventory")
    print ("2. Buy Fruits")
    print ("3. Stock Fruits")
    print ("4. Exit")

    selection = int(input())

    if selection == 1:
        print (fruits)
    elif selection == 2:
        while True:
            fruit_to_buy = input ("Fruit to buy: ")
            if fruit_to_buy not in fruits:
                print ("Fruit not available")
            else:
                break
        while True:
            amount = int (input ("How many: "))
            if amount > fruits.get(fruit_to_buy):
                print ("Only ", fruits.get(fruit_to_buy), " are available")
            else:
                break
        fruits[fruit_to_buy] = fruits.get(fruit_to_buy) - amount
    elif selection == 3:
        fruit_to_stock = input (" What do you want to stock: ")
        amount = int(input(" How many : "))
        if fruit_to_stock in fruits:
            fruits[fruit_to_stock] = fruits.get(fruit_to_stock) + amount
        else:
            fruits[fruit_to_stock] = amount
    elif selection ==4:
        break
    
   
    

    
    

    


    