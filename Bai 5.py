# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 13:27:49 2024

@author: ASUS
"""
def Doithoigian():
    x = input("Nhập vào thời gian cần đổi : ")
    Gio, Phut, Giay = x.split(":")
    tong_giay = int(Gio) * 3600 + int(Phut) * 60 + int(Giay)
    print("Tổng số giây là :", tong_giay)
Doithoigian()

