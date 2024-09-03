# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 22:54:38 2024

@author: ASUS
"""
import math
a= float(input("Nhập a:"))
b= float(input("Nhập b:"))
if a<=0 or b<=0 or a==b:
    print("a,b phải là số lớn hơn 0 và a,b khác nhau.")
else:
    x=(a+b)/(math.pow(a,1/3) + math.pow(b,1/3)) - math.pow(a*b,1/3)
    y=(math.pow(a,1/3) - math.pow(b,1/3))**2
    print("Gia trị biểu thức = ", x/y)
