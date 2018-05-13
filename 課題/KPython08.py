# -*- coding: utf-8 -*-
"""
0H02014 岸本和哉
"""
a = 0
while a != 1:
    print("略記号を入力:", end = "")
    a = input()
    if a == "FE":
        print("基本情報技術者試験です。")
    elif a == "IP":
        print("ITパスポート試験です。")
    elif a == "AP":
        print("応用情報技術者試験です。")
    elif a == "SG":
        print("情報セキュリティマネジメント試験です。")
    elif a == "ST":
        print("ITストラテジスト試験です。")
    elif a == "SA":
        print("システムアーキテクト試験です。")
    elif a == "PM":
        print("プロジェクトマネージャ試験です。")
    elif a == "NW":
        print("ネットワークスペシャリスト試験です。")
    elif a == "DB":
        print("データベーススペシャリスト試験です。")
    elif a == "ES":
        print("エンぺデッドシステムスペシャリスト試験です。")
    elif a == "SM":
        print("ITサービスマネージャ試験です。")
    elif a == "AU":
        print("システム監査技術者試験です。")
    elif a == "SC":
        print("情報処理安全確保支援士試験です。")
    elif a == "QUIT":
        break