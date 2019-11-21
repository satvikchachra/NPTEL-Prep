# -*- coding: utf-8 -*-
"""
Created on Sat Nov 16 14:36:25 2019

@author: Satvik Chachra
"""
# =============================================================================
# 
# Programming Assignment-1: Special Character
# Due on 2019-10-10, 23:59 IST
# Given a string S, check whether it contains any special character or not. Print 'YES' if it does else 'NO'.
# 
# Input Format:
# 
# The first line contains the string S
# 
# Output Format:
# 
# Print 'YES' or 'NO'
# 
# Example:
# 
# Input:
# Hi$my*name
# 
# Output:
# YES
# =============================================================================

import string
specialchar = list(string.punctuation)
ip = input()
def check(ip):
    for i in range(len(ip)):
        if ip[i] in specialchar:
            return True
    return False
 
print(check(ip))

       
    
