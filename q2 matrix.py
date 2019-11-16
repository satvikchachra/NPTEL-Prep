# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 13:49:00 2019

@author: Satvik Chachra
"""
r,c= map(int,input().split(" "))

lst = []
count =1
for i in range(r):
    lstx = []
    for j in range(c):
        lstx.append(count)
        count = count+1
    lst.append(lstx)
print(lst)