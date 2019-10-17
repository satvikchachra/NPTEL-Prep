# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 19:15:17 2019

@author: Satvik Chachra
"""
import string
import random

card1 = [0]*5
card2 = [0]*5

symbols = []
symbols = list(string.ascii_letters)

samesymbol = random.choice(symbols)
symbols.remove(samesymbol)

pos1 = random.randint(0,4)
pos2=  random.randint(0,4)

card1[pos1]=samesymbol
card2[pos2] = samesymbol
i = 0
while(i<5):
    if(i!=pos1):
        card1[i]=random.choice(symbols)
        symbols.remove(card1[i])
    if(i!=pos2):
        card2[i] = random.choice(symbols)
        symbols.remove(card2[i])
        
    i=i+1
    
print(card1)
print(card2)

ch = input("Enter the similar symbol: ")
if(ch==samesymbol):
    print("Right")
else:
    print("Wrong")