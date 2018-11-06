# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 19:42:38 2018

@author: 1898716
"""

from turtle import*

def drawline(x1,y1,x2,y2):
    penup()
    goto (x1,y1)
    pendown()
    goto (x2,y2)
    
def square(x1,y1,sidelenght):
    drawline(x1,y1,sidelenght,y1)
    drawline(sidelenght,y1,sidelenght,y1-sidelenght)
    drawline(sidelenght,y1-sidelenght,x1,y1-sidelenght)
    drawline(x1,y1-sidelenght,x1,y1)
    
square (20,30,150)

exitonclick()

