# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 15:22:13 2019

@author: Satvik Chachra
"""

r,c = map(int,input().split())
l = []

def check():
    for i in range(r):
        for j in range(c):
            if(l[i][j]!=1 and l[i][j]!=0):
                return False
    return True
    
for i in range(r):
    x = list(map(int,input().split()))
    x = x[:c]
    l.append(x)
print(check())

        
    
