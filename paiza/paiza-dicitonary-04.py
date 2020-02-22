# coding: utf-8
# Your code here!

# 辞書をループで処理する

# 辞書のおさらい
enemies = {"ザコ":"スライム", "中ボス":"ドラゴン", "ラスボス":"魔王"}
print(enemies)
print(enemies["中ボス"])

for rank in enemies:
    print(enemies[rank] + "が、あらわれた！")
for (rank,enemy) in enemies.items():
    print(rank + "の" + enemy + "が、あらわれた！")

# 演習課題

# ループで辞書の値を出力しよう

skills = {"職業" : "戦士", "体力" : 100, "魔法力" : 200, "ゴールド" : 380}
# この下で、辞書の値をループで出力してみよう
for i in skills:
    print(skills[i])

# 演習課題２

# ループで辞書のキーと値を出力しよう

skills = {"職業" : "戦士", "体力" : 100, "魔法力" : 200, "ゴールド" : 380}
# この下で、ハッシュの値をループで出力してみよう
for (a, i) in skills.items():
    print(a + "は" + str(i) + "です")

# 演習課題3

# ループで合計を計算しよう

points = {"国語" : 70, "算数" : 35, "英語" : 52}
sum = 0
# この下で、辞書の値の合計をループで計算してみよう
for key in points:
    sum += points[key]
print(sum)
