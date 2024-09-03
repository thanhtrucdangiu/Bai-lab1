# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 17:29:37 2024

@author: ASUS
"""
import math
hinh= input("Nhập loại hình (v):hình vuông, (n):hình chữ nhật, (t):hình tròn :")
if hinh == "v":
    cạnh = float(input("Nhập độ dài cạnh hình vuông ="))
    chuvi = cạnh*4
    dientich = cạnh**cạnh
    print("Chu vi của hình vuông=:",chuvi)
    print("Diện tích của hình vuông =", dientich)
elif hinh == "n":
    a = float(input("Nhập chiều dài cạnh hình chữ nhật="))
    b = float(input("Nhập chiều rộng cạnh hình chữ nhật="))
    C = (a+b)*2
    S = a*b
    print("Chu vi của hình chữ nhật =",C)
    print("Diện tích của hình chữ nhật=",S)
elif hinh == "t":
    r = float(input("Nhập bán kính hình tròn="))
    C = 2*math.pi*r
    S = math.pi*r**2
    print("Chu vi hình tròn =",C)
    print("Diện tích hình tròn =",S)
else:
    print("Không có loại hình hợp lệ.")
    

