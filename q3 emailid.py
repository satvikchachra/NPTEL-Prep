# -*- coding: utf-8 -*-
"""
Created on Sat Nov 16 14:30:54 2019

@author: Satvik Chachra
"""
# =============================================================================
# 
# Programming Assignment-3: Email ID
# Due on 2019-10-03, 23:59 IST
# Assuming that we have some email addresses in the "username@companyname.com" format, please write program to print the company name of a given email address. Both user names and company names are composed of letters only.
# 
# Input Format:
# The first line of the input contains an email address.
# 
# Output Format:
# Print the company name in single line.
# 
# Example;
# 
# Input:
# john@google.com
# 
# Output:
# google
# =============================================================================
import re
email = input()
pat = "(\w+)@(\w+)\.(com)"
ans = re.match(pat,email)
print(ans.group(2))