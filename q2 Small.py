# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 09:16:05 2019

@author: Satvik Chachra
"""
# =============================================================================
# Programming Assignment-2: Small
# Due on 2019-08-22, 23:59 IST
# Given two numbers (integers) as input, print the smaller number.
# 
# Input Format:
# The first line of input contains two numbers separated by a space
# 
# Output Format:
# Print the smaller number
# 
# Example:
# 
# Input:
# 2 3
# 
# Output:
# 2
# =============================================================================

a,b = input().split(" ")
a = int(a)
b = int(b)
if(a<b):
    print(a)
else:
    print(b)

