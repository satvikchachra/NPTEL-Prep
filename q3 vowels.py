# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 23:51:58 2019

@author: Satvik Chachra
"""

# =============================================================================
# Programming Assignment-3: Vowels
# Due on 2019-09-25, 23:59 IST
# Given a string S of lowercase letters, remove consecutive vowels from S. After removing, the order of the list should be maintained.
# 
# Input Format:
# 
# Sentence S in a single line
# 
# Output Format:
# Print S after removing consecutive vowels
# 
# Example:
# 
# Input:
# your article is in queue
# 
# Output:
# yor article is in qu
# 
# Explanation:
# 
# In the first word, 'o' and 'u' are appearing together, hence the second letter 'u' is removed. In the fifth word, 'u', 'e', 'u' and 'e' are appearing together, hence 'e', 'u', 'e' are removed.
# 
# =============================================================================
s = input()
s = s.lower()
s = list(s)

vowels = ['a','e','i','o','u']
i = 0
arbitrary = 0
while(i<len(s)-1):
    if(s[i] == s[i+1]):
        if s[i] in vowels:
            arbitrary+=1
    else:
        print(s[i],end ="")
    i +=1
 
   