# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 18:38:36 2019

@author: Satvik Chachra
"""
# Flames

#User Input Of Name

name1 = input('Enter your  name ')
name2 = input('Enter your crush''s  name ')

name1 = name1.lower()
name2 = name2.lower()

name1 = name1.replace(" ","")
name2 = name2.replace(" ","")

l1 = list(name1)
l2 = list(name2)

duplicate = set()

for i in range(len(l1)):
    for j in range(len(l2)):
        if l1[i] == l2[j]:
            duplicate.add(l1[i])
  
fl1 = list()
fl2 = list()          
for i in range(len(l1)):
    if l1[i] not in duplicate:
        fl1.append(l1[i])

for i in range(len(l2)):
    if l2[i] not in duplicate:
        fl2.append(l2[i])
        
len1 = len(fl1)
len2 = len(fl2)
tl = len1 + len2

l = ['Friends','Love','Affection','Marriage','Enemies','Sister']

tl = tl%6

if tl == 0:
    tl = tl-1+6
else:
    tl = tl -1
    
print("Congrats " + l[tl] + "!!!")