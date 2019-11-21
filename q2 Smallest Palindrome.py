# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 23:07:46 2019

@author: Satvik Chachra
"""
# =============================================================================
# 
# Programming Assignment-2: Smallest Palindrome
# Due on 2019-10-24, 23:59 IST
# Given a string S having characters from English alphabets ['a' - 'z'] and '.' as the special character (without quotes). 
# Write a program to construct the lexicographically smallest palindrome by filling each of the faded character ('.') with a lower case alphabet.
# 
# Definition:
# The smallest lexicographical order is an order relation where string s is smaller than t, given the first character of s (s1 ) is smaller than the first character of t (t1 ), or in case they
# are equivalent, the second character, etc.
# 
# For example "aaabbb" is smaller than "aaac" because although the first three characters
# are equal, the fourth character b is smaller than the fourth character c. 
# 
# Input Format: 
# String S
# 
# Output Format: 
# Print lexicographically smallest palindrome after filling each '.' character, if it
# possible to construct one. Print -1 otherwise.
# 
# Example-1
# 
# Input:
# a.ba
# 
# Output:
# abba
# 
# 
# Example-2:
# 
# Input:
# a.b
# 
# Output:
# -1
# 
# Explanation: 
# In example 1, you can create a palindrome by filling the '.' character by 'b'.
# In example 2, it is not possible to make the string s a palindrome.
# 
# =============================================================================

import string


ip = input()

lst = list(ip)
rlst = lst[::-1]

alpha = list(string.ascii_lowercase)

dot = '.'

def check_pal(lst,rlst):
    if(lst == rlst):
        return 1
    else:
        return 0
   
   
def place_alpha(lst,rlst,alphabet):
    idx1 = None
    idx2 = None
    for i in range(len(lst)):
        if (dot == lst[i]):
            lst[i] = alphabet
            idx1 = i
           
    for j in range(len(rlst)):
        if (dot == rlst[j]):
            rlst[j] = alphabet
            idx2 = j
           
    value = check_pal(lst,rlst)
    if(value==1):
        return 1
    else:
        lst[idx1] = '.'
        rlst[idx2] = '.'
        return 0
       
for x in range(0,len(alpha)):
    val = place_alpha(lst,rlst,alpha[x])
    if(val==1):
        print(lst)
        break
    else:
        print(-1)