# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 19:42:36 2024

@author: ASUS
"""
a = float(input("nhap so nguyen a:"))
b = float(input("nhap so nguyen b:"))
c = float(input("nhap so nguyen c:"))
max = a
min = a
if max < b:
 max = b
if max < c:
 max = c
if min > b:
 min = b
if min > c:
 min = c
print(max,min)
