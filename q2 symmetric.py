# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 15:07:31 2019

@author: Satvik Chachra
"""

n = int(input())
def check():
    for i in range(n):
        for j in range(n):
            if(l[i][j]!=l[j][i]):
                return False
    return True
    
l = []
for i in range(n):
    x = list(map(int,input().split()))
    l.append(x)

print(check())


