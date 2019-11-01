# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 01:51:35 2019

@author: Satvik Chachra
"""
import random
lst = ["rock","paper","scissor"]


#no of turn
n = 50    

p1 = input("enter your name : ")
p2 = input("enter your name : ")
pp1 = 0
pp2 = 0
turn = 0

def fun(c1,c2,p1,p2,pp1,pp2):
    
    
    if(c1==c2):
        
        return 0
    elif(c1 == "rock" and c2 == "paper"):
        
        return p2
    elif(c1 == "rock" and c2 == "scissor"):
       
        return p1
    elif(c1=="paper" and c2 == "rock"):
        
        return p1
    elif(c1 == "paper" and c2 == "scissor"):
      
        return p2
    elif(c1=="scissor" and c2 == "paper"):
        
        return p1
    elif(c1 == "scissor" and c2 == "rock"):
        
        return p2
    
    

while(turn<n):
    c1 = random.choice(lst)
    c2 = random.choice(lst)
    print("Turn : " ,turn)
    print()
    if(fun(c1,c2,p1,p2,pp1,pp2) == p1):
        pp1+=1
        print(p1 + " : " + c1)
        print(p2 + " : " + c2)
        print("---------------------")
    elif(fun(c1,c2,p1,p2,pp1,pp2) == p2):
        pp2+=1
        print(p1 + " : " + c1)
        print(p2 + " : " + c2)
        print("---------------------")
    else:
        print(p1 + " : " + c1)
        print(p2 + " : " + c2)
        print("---------------------")
    
    turn+=1
print("player 1 " +p1+ " final score : ",pp1)
print("player 2 " +p2+ " final score : ",pp2)


