# -*- coding: utf-8 -*-
"""
Created on Tue Dec 23 21:07:39 2025

@author: PC
"""

import random
print("10 soruluk bir çarpım tablosu testi")
basari=0
for i in range(10):
    a=random.randint(1,10)
    b=random.randint(1,10)
    soru=str(a)+"*"+str(b)+"="
    cvp=int(input(soru))
    dogru=a*b
    if cvp==dogru:
        basari+=1
if basari>8:
    print("çok iyisin")
elif basari>6:
    print("iyisin")
elif basari>4:
    print("idare eder")
else:
    print("çalış")
    