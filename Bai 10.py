# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 17:31:02 2024

@author: ASUS
"""
so = int(input("Nhập vào biển số xe gồm 4 số: "))
ngan = so // 1000
tram = so // 100 % 10
chuc = so // 10 % 10
donvi = so % 10
nut = tram + ngan + chuc + donvi
a = nut // 10
b = nut % 10
c = a+b
print("Biển số xe của bạn được: (nút)", c)



