# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 15:33:09 2019

@author: Satvik Chachra
"""
#import string library
import string
dict={}
data=""
#Declare output file in write mode to display file in encryption form
file=open("op_file.txt","w")
#Assigning current letter to previous letter using for loop to convert in encryption form
for i in range(len(string.ascii_letters)):
    #any logic or pattern of your choice
    dict[string.ascii_letters[i]]=string.ascii_letters[i-1]
    print (dict)
#Open the input file using open keyword
with open("name_of_file.txt") as f:
#Start to fetch the character from file till it reaches end of the file
    while True:
        c=f.read(1)
#If file is empty,displays End of file
        if not c:
            print("End Of File")
            break
#If valid alphabet except special characters is present in the file, then it will assign encryption form of alphabets
        if c in dict:
            data=dict[c]
#It remains special characters as it is,it will convert file into encryption form
        else:
            data=c
        file.write(data)
        print(data)
#Closes the file
file.close()
