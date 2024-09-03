# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 17:39:08 2024

@author: ASUS
"""
gio1 = int(input("Nhập giờ cho khoảng thời gian thứ nhất: "))
phut1 = int(input("Nhập phút cho khoảng thời gian thứ nhất: "))
giay1 = int(input("Nhập giây cho khoảng thời gian thứ nhất: "))
gio2 = int(input("Nhập giờ cho khoảng thời gian thứ hai: "))
phut2 = int(input("Nhập phút cho khoảng thời gian thứ hai: "))
giay2 = int(input("Nhập giây cho khoảng thời gian thứ hai: "))
if gio1 >= gio2 and phut1 >= phut2 and giay1 >= giay2:
    hieu_giay = giay1 - giay2
    hieu_phut = phut1 - phut2
    hieu_gio = gio1 - gio2
    if hieu_giay < 0:
        hieu_giay += 60
        hieu_phut -= 1
    if hieu_phut < 0:
        hieu_phut += 60
        hieu_gio -= 1
    print("Hiệu hai khoảng thời gian là:", hieu_gio, "giờ", hieu_phut, "phút", hieu_giay, "giây")
else:
    print("Khoảng thời gian thứ nhất phải lớn hơn hoặc bằng khoảng thời gian thứ hai.")

