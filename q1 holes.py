# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 22:45:14 2019

@author: Satvik Chachra
"""
"""
Let us assume paper as the plane and a letter as a curve on the plane, then each letter divides the plane into regions. For example letters "A", "D", "O", "P", "R" divide the plane into two regions so we say these letters each have one hole. Similarly, letter "B" has two holes and letters such as "C", "E", "F", "K" have no holes. We say that the number of holes in the text is equal to the total number of holes in the letters of the text. Write a program to determine how many holes are in a given text.

Input Format:
The only line contains a non-empty text composed only of uppercase letters of English alphabet.

Output Format:
output a single line containing the number of holes in the corresponding text.

Example-1

Input:
DRINKEATCODE

Output:
5


Explanation:
D R A O D has one hole hence total number of holes in the text is 5.
"""




one_hole = ['A','D','O','P','R','Q']
two_hole = ['B']
str1 = input()



h1 = 0
h2 = 0
for i in range(len(str1)):
    if str1[i] in one_hole:
        h1+=1
    elif str1[i] in two_hole:
        h2+=2
    
        

print(h1+h2)

"""
Test Case 1	
KHUIOPDSHAUPBIPGYUIHDSJIAPGHUIPBJIP
 15
15
Passed
Test Case 2	
JUHJPHJPBJPDSAGJIPHBJIPHUIVHUOYBJIPUUUUFOYUOGBJIPHUIFGYUO
 21
21
Passed
Test Case 3	
HUIGDUSAIOGBHUOGGIDSA
 8
8
Passed
"""

