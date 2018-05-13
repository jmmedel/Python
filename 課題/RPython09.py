# -*- coding: utf-8 -*-
"""
0H02014 岸本和哉
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
