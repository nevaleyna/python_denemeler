# -*- coding: utf-8 -*-
"""
Created on Sun Nov  2 20:10:48 2025

@author: PC
"""

def Topla(x,y):
    return x+y
def Cikar(x,y):
    return x-y
def Carp(x,y):
    return x*y
def Bol(x,y):
    return x/y
print("Yapmak istediğiniz işlemi seçiniz")
print("   ")
print("1.işlem",Topla )
print("2.işlem",Cikar )
print("3.işlem",Carp )
print("4.işlem",Bol )
secme=input("Seçtiğiniz işlem(1,2,3,4):")
sayi1=int(input("1.sayı:"))
sayi2=int(input("2.sayı:"))
if secme=="1":
    print(sayi1,"+",sayi2,"=",Topla(sayi1,sayi2))
elif secme=="2":
        print(sayi1,"-",sayi2,"=",Cikar(sayi1,sayi2))
elif secme=="3":
        print(sayi1,"*",sayi2,"=",Carp(sayi1,sayi2))
elif secme=="4":
    if sayi2==0:
        print("Sıfıra bölüm hatası")
    else:
        print(sayi1,"/",sayi2,"=",Bol(sayi1,sayi2))
else:
    print("Geçersiz sayı girdiniz.")
