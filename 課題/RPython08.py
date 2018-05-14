# -*- coding: utf-8 -*-
"""
Python 3
0H01007 加賀屋　ジャンメデル
"""
print("国語の得点を入力してください->", end="")
kokugo = int(input())
print("数学の得点を入力してください->", end="")
sugaku = int(input())
if kokugo >= 50:
    print("国語は50点以上でした")
    if sugaku >= 50:
        print("数学も５０点以上でした")