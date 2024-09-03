# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 20:06:03 2024

@author: ASUS
"""
a = float(input("nhap so bat ky: "))
switcher = {
  0: "khong",
  1: "mot",
  2: "hai",
  3: "ba",
  4: "bon",
  5: "nam",
  6: "sau",
  7: "bay",
  8: "tam",
  9: "chin"
}
if a >= 0 and a < 10:
 print(switcher.get(a))
else:
 print('Khong doc duoc')
