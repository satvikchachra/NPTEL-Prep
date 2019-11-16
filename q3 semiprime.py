# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 16:07:25 2019

@author: Satvik Chachra
"""

ip = int(input())



def checkp(num):
    temp = num-1
    while(temp!=0 and temp!=1):
        if(num%temp==0):
            return False
        temp-=1
    return True
 
prime = []       
for i in range(200):
    if(checkp(i)):
        prime.append(i)
        
prime.remove(1)

#print(prime)
semiprime = []
for i in range(len(prime)-1):
    for j in range(i+1,len(prime)):
        s = prime[i]*prime[j]
        if(s<=200):
            semiprime.append(s)
#print(semiprime)
sums = []
for i in range(len(semiprime)):
    for j in range(i,len(semiprime)):
        x = semiprime[i] + semiprime[j]
        sums.append(x)
        
if ip in sums:
    print("Yes")
else:
    print("No")
    