# -*- coding: utf-8 -*-
"""
0H02014 岸本和哉
"""
a=[]
for cnt in range(1,82):
    import random
    a.append(random.randint(0,2))
    print(a[cnt-1], end = " ")
    if cnt % 9 == 0:
        print("")
        
print("縦位置を入力してください->",end = "")
t = int(input())
print("横位置を入力してください->",end = "")
y = int(input())

i = t * 9 + y
x = a[i]
flg = 0

while flg == 0:
    for cnt in range(1,5):
        if i + cnt <= 81 and x != a[i + cnt]:
            break
        if cnt == 4:
            print("右5連続がありました")
            flg = flg + 1
            break
        
    for cnt in range(1,5):
        if i + cnt * 8 <= 81 and x != a[i + cnt * 9]:
            break
        if cnt == 4:
            print("縦5連続がありました")
            flg = flg + 1
            break
        
    for cnt in range(1,5):
        if i + cnt * 9 <= 81 and x != a[i + cnt * 10]:
            break
        if cnt == 4:
            print("右下5連続がありました")
            flg = flg + 1
            break
    if flg == 0:
        print("ありませんでした")
        flg = flg + 1
