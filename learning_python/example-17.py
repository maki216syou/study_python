# In[2]
intlist = [7, 0, -9, 3, 2, -1, -3, 1, -5, 4]
print(max(intlist)) # 出力:7
print(min(intlist)) # 出力:-9

# In [3]:
intlist = [7, 0, -9, 3, 2, -1, -3, 1, -5, 4]
print('max(abs):', max(intlist, key=abs))
print('min(abs):', min(intlist, key=lambda x: -x if x < 0 else x))

# In [8]:
intlist = [0, 10, 9, 2, -7, -10, -2, -9, -7, 3]
print(intlist.index(-7))
print(intlist.index(-7, 5))
#print(intlist.index(3, 0, 9))

# In [9]:
intlist = [0, 10, 9, 2, -7, -10, -2, -9, -7, 3]

print(intlist.count(1)) #出力:0

idx = -1
count = intlist.count(-7)
for num in range(count):
    idx = intlist.index(-7, idx + 1) #インデックスidx以降を検索範囲とする
    print(f'{idx}: {intlist[idx]}')#インデックスとその要素を表示

#In [10]:
intlist = list(range(5))
intlist.append(5) #　リストの末尾に要素[5]を追加
intlist.append([6,7]) # リストの末尾にリスト[6, 7] を追加
intlist.extend([8,9]) # リストの末尾に要素[8]と要素[9]を追加
print(intlist) # 出力 : [0, 1, 2, 3, 4, 5, [6, 7], 8, 9]

#In [12]:
foo = 'foo'
bar = 'bar'
baz = 'baz'
strlist = [foo, bar, baz]
print(strlist)
del strlist[1] # strlistのインデックス１の要素を削除
print(strlist)# 出力結果:['foo', 'baz'] (リストから要素'bar'が削除された)
print(bar)#　出力結果:bar (変数barが参照している文字列'bar'は削除されていない)

#In[13]
intlist = [-6, 4, 1, 0, -2, 4, 3, 6]
intlist.remove(4)      # 値が[4]に等しい最初の要素を削除
print(intlist)# 出力結果:[-6, 1, 0, -2, 4, 3, 6]
intlist.remove(False)# 値が[False]に等しい最初の要素を削除
print(intlist)#出力結果:[-6, 1, -2, 4, 3, 6]
#intlist.remove(100)#エラー

#In [14]
intlist = list(range(5))

while intlist:
    print(intlist.pop())

#In [15]: 
intlist = list(range(10))#0~9の整数値を要素とするリストを作成
print(intlist)
print(id(intlist))# intlistのアイデンティティーを表示
intlist.clear()
print(intlist)
print(id(intlist))# intlistのアイデンティティーは変わらない
intlist.append(5)
intlist = []# intlistに空のリストを代入　（リストを削除）
print(id(intlist))# intlistのアイデンティティーが変化する

#In [16]:
intlist = [6, 8, -2, -10, -3, 2, 5, 6, -9, 8]
intlist.sort()# intlistを並べ替える
print(intlist)#出力:[-10, -9, -3, -2, 2, 5, 6, 6, 8, 8]

intlist = [6, 8, -2, -10, -3, 2, 5, 6, -9, 8]
intlist.sort(reverse=True)
print(intlist)#出力:[8, 8, 6, 6, 5, 2, -2, -3, -9, -10]

intlist = [6, 8, -2, -10, -3, 2, 5, 6, -9, 8]
intlist.sort(key=abs)# 絶対値を元に並べ替え
print(intlist)#出力:[-2, 2, -3, 5, 6, 6, 8, 8, -9, -10]

#In[1]
strlist = ['abcd', 'abc', 'Abcd', 'abC']
print(sorted(strlist))

#In [24]
intlist1 = list(range(5))
print(intlist1)

intlist1.reverse()
print(intlist1)

intlist2 = list(range(7))
intlist3 = list(reversed(intlist2))
print(intlist2)
print(intlist3)

#In [18]
strlist1 = ['foo', 'bar', 'baz']
strlist2 = strlist1.copy()
strlist3 = strlist1#intlist1とintlist3は同じリストオブジェクトを参照する

print(strlist1)
print(strlist2)

print(id(strlist1))
print(id(strlist2))
print(id(strlist3))

#In [19]
strlist1[0] = 'FOO'
print(strlist3)#['FOO', 'bar', 'baz']

#In [20]
strlist2[0] = 'Foo'
print(strlist1)
print(strlist2)

#In [21]
intlist1 = [[1,2], [3, 4], [5,6]]
intlist2 = intlist1.copy()

print(intlist1)
print(intlist2)

print(id(intlist1))
print(id(intlist2))

#In [22]
intlist1[0][0] = 101
print(intlist1)
print(intlist2)

#In [23]
from copy import deepcopy
intlist1 = [[1, 2], [3, 4], [5, 6]]
intlist2 = deepcopy(intlist1)

print(intlist1)
print(intlist2)

intlist1[0][0] = 101
print(intlist1)
print(intlist2)