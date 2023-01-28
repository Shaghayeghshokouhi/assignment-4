# -*- coding: utf-8 -*-
"""
Created on Mon Jan 23 22:54:01 2023

@author: 2022
"""

import random

n = int(input("enter a number:"))
list1 =[]

for i in range(n):
    i += 1
    num = (random.randint(0,50))
    if num not in list1:
        list1.append(num)
    
print(list1)    