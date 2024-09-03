# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 17:36:48 2024

@author: ASUS
"""
gio1 = int(input("Nhập giờ cho khoảng thời gian thứ nhất: "))
phut1 = int(input("Nhập phút cho khoảng thời gian thứ nhất: "))
giay1 = int(input("Nhập giây cho khoảng thời gian thứ nhất: "))
gio2 = int(input("Nhập giờ cho khoảng thời gian thứ hai: "))
phut2 = int(input("Nhập phút cho khoảng thời gian thứ hai: "))
giay2 = int(input("Nhập giây cho khoảng thời gian thứ hai: "))
tong_giay = giay1 + giay2
tong_phut = phut1 + phut2 + tong_giay // 60
tong_gio = gio1 + gio2 + tong_phut // 60
tong_giay %= 60
tong_phut %= 60
print("Tổng hai khoảng thời gian là:", tong_gio, "giờ", tong_phut, "phút", tong_giay, "giây")

