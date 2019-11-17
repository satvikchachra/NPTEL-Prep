# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 14:55:24 2019

@author: Satvik Chachra
"""
n = int(input())
l = []
for i in range(n):
    x = list(map(int,input().split()))
    l.append(x)

def printMat(l):
    for i in range(n):
        for j in range(n):
            print(l[i][j],end = " ")
        print()
    
for i in range(n):
    for j in range(n):
        if(j>i):
            l[i][j] = 0

printMat(l)

