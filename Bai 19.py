# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 13:58:26 2024

@author: ASUS
"""
def Min():
    a = int(input("Nhập số nguyên a: "))
    b = int(input("Nhập số nguyên b: "))
    c = int(input("Nhập số nguyên c: "))
    d = int(input("Nhập số nguyên d: "))
    min1 = a
    if b < min1:
        min1 = b
    if c < min1:
        min1 = c
    if d < min1:
        min1 = d
    print("Số nhỏ nhất là:", min1)
Min()

