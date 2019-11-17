# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 19:28:30 2019

@author: Satvik Chachra
"""

n = int(input())
l = list(map(int,input().split()))
k = int(input())
if(k!=n):
    elem = l[k-1]
else:
    elem = l[n-1]
l.sort()
print(l.index(elem)+1)