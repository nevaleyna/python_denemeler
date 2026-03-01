# -*- coding: utf-8 -*-
"""
Created on Sun Dec 14 12:42:36 2025

@author: PC
"""

books = []             
next_book_no = [0]     


def add_book():
    print("KİTAP EKLE")
    name = input("Kitap adı: ")
    author = input("Yazar adı: ")
    book_type = input("Tür: ")
    shelf = input("Kitaplık adı: ")
    row = input("Raf numarası: ")

    no = next_book_no[0]

   
    book = [no, name, author, book_type, shelf, row, True]
    books.append(book)

    print("Kitap eklendi! Kitap numarası:", no)

    next_book_no[0] += 1


def list_books():
    print("KİTAP LİSTESİ")

    if books == []:
        print("Hiç kitap yok.")
        return

    for b in books:
        if b[6] == True:
            durum = "Mevcut"
        else:
            durum = "Ödünçte"

        print("No:", b[0], "|", b[1], "-", b[2],
              "| Tür:", b[3], "|", b[4], "/ Raf:", b[5], "| Durum:", durum)


def search_book():
    print("KİTAP ARA")
    no = int(input("Kitap numarası: "))

    for b in books:
        if b[0] == no:
            if b[6] == True:
                durum = "Mevcut"
            else:
                durum = "Ödünçte"

            print("Kitap bulundu!")
            print("Ad:", b[1])
            print("Yazar:", b[2])
            print("Tür:", b[3])
            print("Yer:", b[4], "Raf:", b[5])
            print("Durum:", durum)
            return

    print("Bu numarada kitap yok.")


def borrow_book():
    print("KİTAP ÖDÜNÇ AL")
    no = int(input("Kitap numarası: "))

    for b in books:
        if b[0] == no:
            if b[6] == True:     
                b[6] = False      
                print("Kitap ödünç alındı:", b[1])
            else:
                print("Bu kitap zaten ödünçte.")
            return

    print("Bu numarada kitap yok.")


def return_book():
    print("KİTAP İADE ET")
    no = int(input("Kitap numarası: "))

    for b in books:
        if b[0] == no:
            if b[6] == False:    
                b[6] = True       
                print("Kitap iade edildi:", b[1])
            else:
                print("Bu kitap zaten kütüphanede.")
            return

    print("Bu numarada kitap yok.")



while True:
    print("KÜTÜPHANE MENÜ")
    print("1 - Kitap Ekle")
    print("2 - Kitapları Listele")
    print("3 - Kitap Ara")
    print("4 - Kitap Ödünç Al")
    print("5 - Kitap İade Et")
    print("0 - Çıkış")

    secim = input("Seçim: ")

    if secim == "1":
        add_book()
    elif secim == "2":
        list_books()
    elif secim == "3":
        search_book()
    elif secim == "4":
        borrow_book()
    elif secim == "5":
        return_book()
    elif secim == "0":
        print("Program kapatıldı.")
        break
    else:
        print("Hatalı seçim!")