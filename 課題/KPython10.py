# -*- coding: utf-8 -*-
"""
0H02014 岸本和哉
"""
print("罫線の本数を入力してください->", end = "")
n = int(input())
if n > 2:
    print("○", end = "")
    print("─┬", end = "")
    for cnt in range(1,n - 2):
        print("──┬", end = "")
    print("──✕")
    m = 1
    b = n - 2
    for cnt in range(1,n - 1):
        print("│",end = "")
        for cnt in range(1,n):
            print("　│", end = "")
        print("")
        print("├", end = "")
        for cnt in range(1,n - 1):
            if b == cnt:
                print("──✕", end = "")

            elif m == cnt:
                print("──○", end = "")

            else:
                print("──┼", end = "")
        if m != b:
            print("─┤")
        else:
            print("──┤")
        m = m + 1
        b = b - 1
    print("│", end = "")
    for cnt in range(1,n):    
        print("　│", end = "")
    
    print("")    
    print("✕",end = "") 
    print("─┴", end = "")   
    for cnt in range(1,n - 2):
        print("──┴", end = "")
    
    print("──○")
elif n == 2:
    print("○──✕")
    print("│　│")
    print("✕──○")

elif n == 1:
    print("○")
    print("│")
    print("✕")
else :
    print("")