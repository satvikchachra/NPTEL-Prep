# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 12:02:40 2019

@author: Satvik Chachra
"""
# =============================================================================
# Programming Assignment-1: Max and Min
# Due on 2019-08-22, 23:59 IST
# Given a list of numbers (integers), find second maximum and second minimum in this list.
# 
# Input Format:
# 
# The first line contains numbers separated by a space.
# 
# Output Format:
# 
# Print second maximum and second minimum separated by a space
# 
# Example:
# 
# Input:
# 
# 1 2 3 4 5
# 
# Output:
# 
# 4 2
# =============================================================================
lst = list(map(int,input().split(" ")))
lst.sort()
i = len(lst)-1
while(lst[i] == lst[i-1] and i>=1):
    i = i-1
idx1 = i-1
print(lst[idx1])

j = 0
while(lst[j] == lst[j+1] and j<=len(lst)-2):
    j = j+1
idx2 = j+1
print(lst[idx2])