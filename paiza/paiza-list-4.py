# coding: utf-8
# リストの要素を操作する

team = ["勇者", "魔法使い"]
print(team)
print(team[1])
print(len(team))

team.append("戦士")
print(team)
print(len(team))

team[2] = "ドラゴン"
print(team)
print(len(team))

team.pop(2)
print(team)
print(len(team))

# 演習課題１

weapon = ["木の棒", "鉄の棒", "鉄の剣", "銅の剣"]
weapon.append("石斧")
print(weapon)

# 演習課題２
weapon2 = ["木の棒", "鉄の棒", "鉄の剣", "銅の剣"]
weapon2[3] = "サビた剣"
print(weapon2) 

# 演習課題3
weapon3 = ["木の棒", "鉄の棒", "鉄の剣", "銅の剣"]
weapon3.pop(2)
print(weapon3)