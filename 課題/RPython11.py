# -*- coding: utf-8 -*-
"""
Python 3
0H01007 加賀屋　ジャンメデル
"""
cnt = 1
sun = 0
while cnt <= 5:
    print(str(cnt) + "番目の値を入力して下さい->", end = "")
    d_str = input()
    d_int = int(d_str)
    if d_int < 0 or d_int > 100:
        break
    sum = sum + d_int
    cnt = cnt + 1
else:
    print("平均は" + str(sum / (cnt - 1)) + "です")
print ("このprintは常に実行します")

