# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 23:04:06 2024

@author: ASUS
"""
chu = input("Nhập chữ cái: ")
if chu.islower():
    print("Kết quả: ", chu.upper())
elif chu.isupper():
    print("Kết quả: ", chu.lower())
else:
    print("Không phải chữ cái!")
