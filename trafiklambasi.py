# -*- coding: utf-8 -*-
"""
# %%
Created on Sun Jan 25 14:18:29 2026


@author: PC
"""
from turtle import Screen, Turtle

import time
w=Screen()
w.bgcolor("lightgray")
w.setup(300,700)
w.title("Trafik ışığı uygulaması")
w.tracer(0)
kalem=Turtle()
kalem.speed(0)
kalem.pensize(4)
kalem.penup()
kalem.goto(0,180)
kalem.pendown()

for i in range (2):
    kalem.forward(80)
    kalem.right(90)
    kalem.forward(250)
    kalem.right(90)
kalem.hideturtle() 

isik=Turtle()
isik.penup()
isik.shape("circle")
isik.shapesize(3)

def isik_yak(renk, y_koordinati):
    isik.clear()
    isik.color(renk)
    isik.goto(40, y_koordinati)
    w.update()

try:
    while True:
    
      isik_yak("green",0)
      
     
      time.sleep(9)
      isik_yak("yellow",70)
     
      time.sleep(3)
      isik_yak("red",140)
     
      time.sleep(9)
except:
    print("program kapatıldı")
w.mainloop()