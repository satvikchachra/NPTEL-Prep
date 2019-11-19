# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 22:05:32 2019

@author: Satvik Chachra
"""
# =============================================================================
# Programming Assignment-2: Panagrams
# Due on 2019-09-25, 23:59 IST
# A panagram is a sentence containing every 26 letters in the English alphabet. Given a string S, check if it is panagram or not.
# 
# Input Format:
# The first line contains the sentence S.
# 
# Output Format:
# Print 'YES' or 'NO' accordingly
# 
# Example:
# 
# Input:
# The quick brown fox jumps over the lazy dog
# 
# Output:
# YES
# =============================================================================
import string
s = input()
s = s.lower()
l = list(string.ascii_lowercase)
for i in range(len(s)):
    if s[i] in l:
        l.remove(s[i])
if(len(l)==0):
    print("YES")
else:
    print("NO")
    