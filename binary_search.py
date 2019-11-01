# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 14:21:33 2019

@author: Satvik Chachra
"""

def lnr_s(a,x):
    for i in range(0,len(a)):
        if(a[i]==x):
            return i
    return -1

def bnry_s(a,x):
    first_pos = 0 
    last_pos = len(a)-1
    flag = 0
    
    while(first_pos<=last_pos and flag == 0):
        mid = (first_pos+last_pos)//2
        if(x==a[mid]):
            flag = 1
            print("element is at position ",mid)
            return 
        else:
            if(x<a[mid]):
                last_pos = mid-1
            else:
                first_pos = mid+1
                

    print("element not present in the given array")

    
def sort_a(a):
    n = len(a)
    for i in range(n):
        for j in range(len(a)-i-1):
            if(a[j]>a[j+1]):
                temp = a[j]
                a[j] = a[j+1]
                a[j+1] = temp

a = []
noe = int(input("enter no of elements : "))
for i in range(noe):
    e = int(input("enter element : "))
    a.append(e)
sort_a(a)
print("sorted array : ",a)
x = int(input("enter the element to search in the given array : "))

bnry_s(a,x)