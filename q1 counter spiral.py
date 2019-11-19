# -*- coding: utf-8 -*-
"""
Created on Sat Nov 16 00:22:10 2019

@author: Satvik Chachra
"""
# =============================================================================
# Programming Assignment-1: Counter Spiral
# Due on 2019-10-03, 23:59 IST
# Given a square matrix, you have to write a program to print it in a counter-clockwise spiral form.
# 
# 
# Input Format:
# The first line of the input contains an integer number n which represents the number of rows and columns in the matrix.
# From the second line contains n rows with each row having n elements separated by a space.
# 
# Output Format:
# Print the elements in a single line with each element separated by a space
# 
# Example:
# 
# Input:
# 4
# 25 1 29 7
# 24 20 4 32
# 16 38 29 1
# 48 25 21 19
# 
# Output:
# 25 24 16 48 25 21 19 1 32 7 29 1 20 38 29 4
# 
# Explanation: 
# In the above example, each row, first all the elements of the first column is printed which are 25 24 16 48 after that, remaining elements of the last row is printed which are 25 21 and 19.
# After which the remaining elements of the last column is printed which are 1 32 and 7 and so on...
# =============================================================================
def counterClock(r,c,arr):
    sr = 0
    sc = 0
    er = r-1
    ec = c-1
    total = r*c
    count = 0
    
    while(count<total):
        #if(count == total):
           # break
        
        #first col
        for i in range(sr,er+1):
            if(count > total):
                break
            print(arr[i][sc],end = " ")
            count+=1
        sc+=1
        #last row
        for i in range(sc,ec+1):
            if(count > total):
                break
            print(arr[er][i],end = " ")
            count+=1
        er-=1
        #last col
        for i in range(er,sr-1,-1):
            if(count > total):
                break
            print(arr[i][ec],end = " ")
            count+=1
        ec-=1
        #first row
        for i in range(ec,sc-1,-1):
            if(count > total):
                break
            print(arr[sr][i],end = " ")
            count+=1
        sr+=1
            
            
            
        
            
    
    
 
num = int(input())
R = num
C = num

arr = []
for i in range(1,num+1):    
    l = list(map(int, input ().split ()))
    arr.append(l)
         
counterClock(R, C, arr)         
            
        
        
        

