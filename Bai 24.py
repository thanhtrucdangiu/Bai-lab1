# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 17:17:32 2024

@author: ASUS
"""
a = int(input("Nhập giờ:"))
b = int(input("Nhập phút:"))
c = int(input("Nhập giây:"))
if 0<= a <= 23 and 0<= b <= 59 and 0<= c <= 59:
    print("Thời gian hợp lệ.")
else:
    print("Thời gian Không hợp lệ.")

