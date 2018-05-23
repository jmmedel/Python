# -*- coding: utf-8 -*-
"""
Python 3
0H01007 加賀屋　ジャンメデル
"""
print ("学年を入力してください(1～4)->", end = "")
n_str = input()
n_int = int(n_str)
if n_int == 1:
        print("ソフトⅠコースです")
        print("入学学年です")
elif n_int == 2:
        print("ソフトⅡコースです")
elif n_int == 3:
        print("ソフトⅢコースです")
elif n_int == 4:
        print("ソフトⅣコースです")
        print("最終学年です")
else:
        print("学年は1～4です")
