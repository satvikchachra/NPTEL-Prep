# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 00:29:57 2019

@author: Satvik Chachra
"""

# =============================================================================
# Programming Assignment-1: Marks distribution
# Due on 2019-10-17, 23:59 IST
# Given a list A of n elements, representing the marks. There are m students and you have to distribute the marks from the list A to m students such that:
# 
# 1) Each student gets marks.
# 2) The difference between the maximum marks and minimum marks given to the students is minimised.
# 
# Input Format:
# The first line contains the value n and m respectively separated by a space.
# The second line contains the elements of list A separated by a space
# 
# Output Format:
# Print the minimum difference
# 
# Example:
# 
# Input:
# 7 3
# 7 3 2 4 8 12 56
# 
# Output:
# 2
# 
# Explanation:
# We need to pick 3 marks for three students (m=3). If we pick 2, 3 and 4, the difference is minimum which is 2.
# 
# =============================================================================

n,m = map(int, input().split())
lst = list(map(int,input().split()))
lst.sort()
print(lst[m-1]-lst[0])
    
    