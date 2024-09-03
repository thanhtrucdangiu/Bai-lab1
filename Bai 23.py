# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 18:31:38 2024

@author: ASUS
"""
import math
a= float(input("Nhap he so a: "))
b= float(input("Nhap he so b: "))
c= float(input("Nhap he so c: "))
delta = b**2 - 4*a*c
if a==0:
    if b==0:
        if c==0:
            print("Phuong trinh vo so nghiem.")
        else:
            print("Phuong trinh vo nghiem.")
    else:
        x = -c / b
        print(f"Nghiem cua phuong trinh la x = {x}")
else:
    if delta > 0:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        print(f"Phuong trinh co hai nghiem phan biet: x1 = {x1} va x2 = {x2}")
    elif delta == 0:
        x = -b / (2 * a)
        print(f"Phuong trinh co nghiem kep: x = {x}")
    else:
        print("Phuong trinh vo nghiem.")