# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 15:12:02 2019

@author: Satvik Chachra
"""

n,v1,v2 = map(int,input().split(" "))
d1 = pow(2,1/2)*n
t1 = d1/v1

d2 = 2*n
t2  = d2/v2

if(t1<t2):
    print("Walk")
else:
    print("Cab")