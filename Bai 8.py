# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 13:38:11 2024

@author: ASUS
"""
def TinhBMI():
    Cannang = float(input("Nhập cân nặng của bạn (kg) = "))
    Chieucao = float(input("Nhập chiều cao của bạn (m) = "))
    BMI = Cannang / (Chieucao ** 2)
    BMI = round(BMI, 2)
    print("Chỉ số BMI của bạn là : ", BMI)
TinhBMI()

