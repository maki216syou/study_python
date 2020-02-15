#In [1]:
languages = ['Python', 'Ruby', 'PHP']
print(languages)

# In [3]
emptylist = [] #空のリスト　（要素が一つもないリスト）を定義
print(emptylist) # 出力結果:

# In [4]
strlist = list('Python') #'P', 'y', 't', 'h', 'o', 'n'を要素とするリストを作成
print(strlist)
intlist = list(range(10))# 整数値0~9を要素とするリストを作成
print(intlist)
somelist = list(intlist)# リストからリストを作成
print(somelist)

# In [5]
languages[0]

# In [6]
somelist = ['python', 1, 100.5]
print(somelist)

# In [7]
intlist = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(intlist[1:4])# インデックス1からインデックス3までの3つの要素を取得
print(intlist[:3])# インデックス0からインデックス2までの3つの要素を取得
print(intlist[5:]) # インデックス5以降の要素を取得
print(intlist[1:9:2])# インデックス1~8までの範囲にある要素を1つ飛ばしで取得

#In [8]:
languages = ['Python', 'Ruby', 'PHP']
print(languages)
languages[2] = 'JavaScript'
print(languages)
print(languages[2])

#IN [11]
languages = ['Python', 'Ruby', 'PHP']
languages.append('Perl')
print(languages)

#In [12]
cs = 'C#'
number = 99

languages = languages + [cs, number]
print(languages)

#In [14]
somelist = [0,1,2]
print(id(somelist))
somelist = somelist + [3, 4]
print(id(somelist))
somelist += [5,6]
print(id(somelist))

#In [15]
del languages[5]
print(languages)

#In [17]
intlist = [1, 2 ,3, 1, 2, 3]
intlist.remove(3)
print(intlist)

#In [22]
print([num *2 for num in range(10)])# 0, 2, 4, ...., 18を要素とするリスト
print([num * num for num in range(10) if num %2 == 0])# numが偶数の時に二乗

#In [23]
for row in [[x * y for y in range(1,10)] for x in range(1,10)]:
    print(row)

#In [24]:
result = []
for x in range(1,10):
    # zを計算
    z = []
    for y in range(1, 10):
        z.append(x * y)
    result.append(z)
#In [25]
print(result[0][1])

#In [26]
for row in result:
    for column in row:
        print(f'{column:>3}', end='')
    print()
    
