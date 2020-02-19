# coding: utf-8
# 標準入力したデータをリストに格納する

line = input().rstrip().split(",")
print(line)


#　演習問題
# coding: utf-8
#文字列をカンマで分割する

team_str = "勇者,戦士,忍者,魔法使い"
team_array = team_str.split(",")
print(team_array)

# 演習問題２
# coding: utf-8
#英文の単語数を数える

str = "One cold rainy day when my father was a little boy he met an old alley cat on his street"
words = str.split(" ")
print(len(words))

# 演習問題３
url_str = input().rstrip().split("/")