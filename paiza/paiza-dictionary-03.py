# coding: utf-8
# your code here!

# 辞書の基本操作
enemies = { "ザコ":"スライム", "中ボス":"ドラゴン", "ラスボス":"魔王"}
print(enemies)
print(enemies["中ボス"])
print(len(enemies))

enemies["中ボス"] = "レッドドラゴン"
print(enemies)
print(len(enemies))

del enemies["ザコ"]
print(enemies)
print(len(enemies))

#演習課題

# 辞書の長さを出力する

skills = {"職業":"戦士", "体力":100, "魔法力":200, "ゴールド":380}
# この下で、辞書の長さを出力してみよう
print(len(skills))

#演習課題２

skills2 = {"職業":"戦士", "体力":100, "魔法力":200, "ゴールド":380}
skills2["属性"] = "炎"
print(skills2)

#演習課題3

# 辞書に要素を更新する

skills3 = {"職業":"戦士", "体力":100, "魔法力":200, "ゴールド":380}
print(skills3)
# この下で、ハッシュを更新してみよう
skills3["職業"] = "魔法使い"
print(skills3)


#演習課題4

# 辞書の要素を削除する

skills4 = {"職業" : "戦士", "体力" : 100, "魔法力" : 200, "ゴールド" : 380}
print(skills4)
# この下で、辞書を削除してみよう
del skills4["体力"]
print(skills4)