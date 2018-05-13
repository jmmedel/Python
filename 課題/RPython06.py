# -*- coding: utf-8 -*-
"""
0H02014 岸本和哉
"""
str1 = "ITスペシャリスト学科"
str2 = "   aBBcccDDDeee "
print(len(str1))
print(str2.count("c"))
print(str2.count("c",7))
str3 = str2.strip()
str4 = str2.lower()
print(str2)
print(str3)
print(str4)
str5 = str1.replace("スペシャリスト", "エキスパート")
print(str5)
