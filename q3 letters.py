# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 00:23:53 2019

@author: Satvik Chachra
"""
# =============================================================================
# Programming Assignment-3: Letters
# Due on 2019-10-24, 23:59 IST
# Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
# 
# Input Format:
# The first line of the input contains a statement.
# 
# Output Format:
# Print the number of upper case and lower case respectively separated by a space.
# 
# Example:
# 
# Input:
# Hello world!
# 
# Output:
# 1 9
# =============================================================================
import string
x = input()
l=0
h = 0
for i in range(len(x)):
    if x[i] in list(string.ascii_lowercase):
        l+=1
    elif x[i] in list(string.ascii_uppercase):
        h+=1

print(h,end = " ")
print(l)
