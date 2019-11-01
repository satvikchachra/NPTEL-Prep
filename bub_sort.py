# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 12:02:31 2019

@author: Satvik Chachra
"""
def bub(a):
    n = len(a)
    for i in range(n):
        for j in range(n-i-1):
            if(a[j]>a[j+1]):
                tmp = a[j]
                a[j] = a[j+1]
                a[j+1] = tmp

a = [9,2,5,1,4,5]
bub(a)
print(a)
                