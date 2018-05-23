# -*- coding: utf-8 -*-
"""
Python 3
0H01007 加賀屋　ジャンメデル
"""
list1 = ["あいうえお","かきくけこ","さしすせそ"]
list2 = [123, 456]
tuple1 = ("たちつてと","なにぬねの")
set1 = {"ソフトⅠ","ソフトⅢ"}
dic1 = {1:"ソフトⅠ",2:"ソフトⅡ",3:"ソフトⅢ"}
print("list1の要素数=" + str(len(list1)))
print("list1の要素")
print(list1)
list3 = list1 + list2
print("list3の要素数=" + str(len(list3)))
print("list3の要素")
print(list3)
print("tuple1の要素数=" + str(len(tuple1)))
print("tupleの1番目の要素は" + list1[1])
print("tupleを３回繰り返したタプルは")
print(tuple1 * 3)
list1.append("ABCDE")
print("list1の要素は次のようになりました")
print(list1)
print("set1の要素数=" + str(len(set1)))
print("set1の要素")
print(set1)
set1.add("ソフトⅡ")
print("set1の要素は次のようになりました")
print(set1)
if 4 in dic1:
        print("dic1のキーは４にあります")
else :
        print("dic1のキーに４はありません")
print("キー２の値は" + dic1[2])