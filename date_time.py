# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 23:03:19 2019

@author: Satvik Chachra
"""

import datetime
import random

birthday=[]

i=0
while(i<50):
    year = random.randint(2018,2019)
    
    if(year%4==0 and(year%100!=0 or year%400==0)):
        leap=1
    else:
        leap=0
        
    month = random.randint(1,12)
    if(month==2 and leap==1):
        day=random.randint(1,29)
    elif(month==2 and leap==0):
        day = random.randint(1,28)
    elif(month%2==0 and month<7):
        day = random.randint(1,30)
    elif(month%2!=0 and month<=7):
        day=random.randint(1,31)
    elif(month%2!=0 and month>7):
        day=random.randint(1,30)
    else:
        day=random.randint(1,31)
    
    dd = datetime.date(year,month,day)
    birthday.append(dd)
    i=i+1
    
birthday.sort()
for i in range(0,50):
    
    print(birthday[i]," ", birthday.count(birthday[i]))


        





# =============================================================================
# 
# 
# print(datetime.date.today())
# #print(datetime.datetime.now("%Y"))
# print("Week No Of Today",datetime.date.today().strftime("%W"))   # prints week no of current day (%W)<br>
# print("weekday of week ",datetime.date.today().strftime("%w"))
# print("day of year ",datetime.date.today().strftime("%j"))
# print("day of week ",datetime.date.today().strftime("%A"))
# 
# 
# 
# =============================================================================
