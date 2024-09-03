# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 14:10:00 2024

@author: ASUS
"""
def max():
    a = int(input("Nhập số nguyên a: "))
    b = int(input("Nhập số nguyên b: "))
    c = int(input("Nhập số nguyên c: "))
    Max = a
    if b > Max:
        Max = b
    if c > Max:
        Max = c
    print("Số lớn nhất là:", Max)
max()



