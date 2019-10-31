# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 01:14:19 2019

@author: Satvik Chachra
"""
import random
doors = [0]*3
goatdoor = []

swap = 0
dont_swap = 0 
x = random.randint(0,2)
doors[x] = "car"
for i in range (0,3):
    if(i==x):
        continue
    else:
        doors[i] = "goat"
        goatdoor.append(i)
        
choice = int(input("enter your choice : "))
#open goat door
door_open = random.choice(goatdoor)
#door open should not be equal to the choice made by user
while(door_open == choice):
    door_open = random.choice(goatdoor)

ch = input("do you want to swap ? y/n")
if(ch=='y'):
    if(doors[choice]=="goat"):
        print("player wins")
        swap +=1
    else:
        print("player lost")
if(ch=='n'):
    if(doors[choice]=="goat"):
        print("player lost")
    else:
        print("player won")
        dont_swap +=1
    
print("n swap : ",swap)
print("n dont swap : ",dont_swap)
    
