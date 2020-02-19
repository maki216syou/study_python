# coding: utf-8
# ループでリストを処理する

team = ["勇者", "戦士", "魔法使い", "盗賊"]
#print(team)
#print(team[0])

#print("<select name='job'>")
for job in team:
    #print("<option>" + job + "</option>")
#print("</select>")

# 演習課題
enemy = ["スライム", "モンスター", "ゾンビ", "ドラゴン", "魔王"]

for i in enemy: 
    print(i + "が現れた！")

# 演習課題２
numbers = [12, 34, 56, 78, 90]
total = 0
for num in numbers:
    total += num

print(total)