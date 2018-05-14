# -*- coding: utf-8 -*-
"""
Python 3
0H01007 加賀屋　ジャンメデル
"""
cnt = 1
sum = 0
while cnt <= 5:
    print(str(cnt) + "番目の値を入力してください->", end = "")
    d_str = input()
    d_int = int(d_str)
    sum = sum + d_int
    cnt = cnt + 1
print("平均は" + str(sum / (cnt - 1)) + "です")
