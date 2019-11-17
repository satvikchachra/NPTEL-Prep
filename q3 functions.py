# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 14:51:01 2019

@author: Satvik Chachra
"""


def printDict():
    n = int(input())
    d = dict()
    for i in range(1,n+1):
        d[i] = pow(i,2)
        
    print(d)
        
printDict()