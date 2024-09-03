# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 13:32:43 2024

@author: ASUS
"""
import math
def tinhchuvivadientichhinhtron():
    Bankinh = float(input("Nhập bán kính đường tròn = "))
    Chuvi = 2 * math.pi * Bankinh
    Dientich = math.pi * Bankinh ** Bankinh
    print("Chu vi hình tròn là :", Chuvi)
    print("Diện tích hình tròn là :", Dientich)
tinhchuvivadientichhinhtron()


