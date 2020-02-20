# coding: utf-8
# Your code here!

#　リストのおさらい
enemyArray = ["スライム", "モンスター", "ドラゴン"]
print(enemyArray)
print(enemyArray[0])

# 辞書の具体例
enemyDictionary = {"ザコ":"スライム", "中ボス":"ドラゴン", "ラスボス":"魔王"}
print(enemyDictionary)
print(enemyDictionary["中ボス"])

level = "ザコ"
print(enemyDictionary[level])

#print(enemyDictionary["敵"])

#演習問題

skills = {"職業":"戦士", "体力":100, "魔法力":200, "ゴールド":380}
print(skills)

#演習問題2

skills2 = {"魔法力":200, "体力":100, "職業":"戦士", "ゴールド":380}
print(skills2)

#演習問題3

# 辞書の特定の値を出力してみよう

skills = {"職業":"戦士", "体力":100, "魔法力":200, "ゴールド":380}
# この下で、辞書から出力してみよう
print(skills["職業"])