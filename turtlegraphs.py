# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 19:42:38 2018

@author: 1898716
"""

from turtle import*

def drawline(x1,y1,x2,y2,color="black"):
    penup()
    goto (x1,y1)
    pendown()
    goto (x2,y2)
    
def square(height,width,x,y,color="black",fill="white"):
    fillcolor(color)
    begin_fill()
    drawline(x,y,x+width,y)
    drawline(x+width,y,x+width,y-height)
    drawline(x+width,y-height,x,y-height)
    drawline(x,y-height,x,y)
    end_fill()
 

def triangle(height,width,x,y,color="black",fill="white"):
    fillcolor(color)
    begin_fill()
    drawline(x,y,x+width,y)
    left(60)
    drawline(x+width,y,x+width/2,y+height)
    left(60)
    drawline(x+width/2,y+height,x,y)
    end_fill()
    
#def circle(radius,color="black",fill="white"):
    
    
    
square (150,150,20,20,"blue")
triangle (150,150,40,40,"red")

exitonclick()

