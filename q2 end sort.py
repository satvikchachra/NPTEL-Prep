# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 15:19:58 2019

@author: Satvik Chachra
"""

l = list(map(int,input().split()))
b = sorted(l)
count = 0
for i in range(len(l)):
    if(l[i]==b[count]):
        count = count+1
print(len(l) - count)