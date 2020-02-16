# In[1]
intlist = [44, 99, 78, 36, 86, 100, 89, 48, 50, 58]

# In [2]
result = intlist[0] + intlist[1] + intlist[2] +intlist[3] + intlist[4] +\
         intlist[5] + intlist[6] + intlist[7] + intlist[8] + intlist[9]
print(result)

# In [3]
result = 0

for number in intlist:
    result = result + number
print(result)

# In [6]
languages = ['Python', 'Ruby', 'PHP']

print(languages)

counter = 0
for language in languages:
    language = f'{counter}: {language}'
    counter += 1

print(languages)

# In [8]:
languages = ['Python', 'Ruby', 'PHP']

print(languages)

for index, language in enumerate(languages):
    languages[index] = f'[index]: [language]'

print(languages)

# In [9]
namelist = ['一色', 'かわさき', '遠藤', '島田', '小川']
weightlist = [65, 80, 70, 75, 72]

# In [10]
for index, name in enumerate(namelist):
    print(f'{name}さんの体重は{weightlist[index]}kgです')

# In [11]
for name, weight in zip(namelist, weightlist):
    print(f'{name}さんの体重は{weight}kgです')

# In [12]
shortlist = list(range(4))# [0, 1, 2, 3]
longlist = list(range(10, 20))# [10, 11, 12,,,, 19]
for x, y in zip(shortlist, longlist):
    print(x, y)

# In [14]:
intlist = list(range(5))
result = map(lambda x: x * x, intlist)
print(intlist)
print(list(result))#map関数の戻り値（イテレータ）からリストを作成

# In [15]
result = [x * x for x in intlist]
print(result)

#In [16]
intlist = list(range(10)) #[0, 1, 2, ,,, 9]
result = filter(lambda x: x % 2 == 0, intlist) #偶数だけを選択
print(intlist)
print(list(result))