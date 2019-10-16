# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 23:01:36 2019

@author: Satvik Chachra
"""
def magic_square(n):
    ms = []
    for i in range(n):
        l=[]
        for j in range(n):
            l.append(0)
        ms.append(l)
    
    
    
    #position of 1
    i = n//2
    j = n-1
    
    
    mat = n*n
    count = 1
    while(count<=mat):
        if(j==n and i == -1):
            i=0
            j=n-2
        elif(j==n):
            j=0
        elif(i<0):
            i=n-1
        if(ms[i][j]!=0):
            i = i+1
            j = j-2
            continue
        else:
            ms[i][j] = count
            count = count+1
            
        i = i-1
        j = j+1 
    pr(n,ms)
            
        
            

def pr(n,ms):
    for i in range(n):
        for j in range(n):
            print(ms[i][j],end=" ")
        print()

n = int(input("Enter the order of square matrix: "))
m = int((n*((n*n)+1))/2)
print("matrix constant = ",m)

magic_square(n)
