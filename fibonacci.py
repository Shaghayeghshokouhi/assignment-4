# -*- coding: utf-8 -*-
"""
Created on Mon Jan 23 23:15:28 2023

@author: 2022
"""
n1 = 0
n2 = 1
counter = 0
n = int(input("enter n:"))
if n == 1:
    print("0")
else :
    while counter < n:
        print(n1)
        number = n1+n2
        n1=n2
        n2=number
        counter += 1              