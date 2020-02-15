#In [1]:
def myfunc(param1, param2, param3):
    return f'param1: {param1}, param2: {param2}, param3: {param3}'
#In [2]:
print(myfunc(1, 2, 3))

#In [3]:
print(myfunc(param3=1, param2='string', param1=0.5))

#In [4]:
print(myfunc(1, param3='param3', param2=2)) #正しい

#In [5]:
#print(myfunc(param3='param3', 2, 1)) #エラー

#In [6]:
print(myfunc(*'abc'))
print(myfunc(1, *'23'))
print(myfunc(*'12', 3))

#In [7]
#print(myfunc(*'abcd'))  #エラー

#In [9]
arg_dict = {'param3': 'param3', 'param2':2, 'param1': 1.0}

#In [10]
print(myfunc(**arg_dict))

#In [11]
def myfunc(param1='param1', param2='param2', param3='param3'):
    return f'param1: {param1}, param2: {param2}, param3: {param3}'

#In [12]
print(myfunc()) #引数を全て省略
print(myfunc(1))# 第２引数と第３引数を省略
print(myfunc(param2=2))#　パラメーターparam2の値だけを指定して、他は省略

#In [13]:
#def myfunc(param1='param1', param2, param3='param3'):
    #return F'param1: {param1}, param2: {param2}, param3: {param3}'


#In [14]: 
print('some', 'value')

#In [15]:
import sys
print('some','value', sep='', end='\n', file=sys.stdout, flush=False)

#In [16]
print('some', 'value', sep='')

#In [17]
def myfunc(param1, param2, *args):
    return f'param1: {param1}, param2: {param2}, other: {args}'

#In [18]
print(myfunc(1,2))
print(myfunc(1,2,3))
print(myfunc(1,2,3,4))

def myfunc(param1, param2, *args):
    tmp = f'param1: {param1}, param2: {param2}'
    index = 3 
    for item in args:
        tmp += f', param{index}: {item}'
        index += 1
    return tmp

print(myfunc(1, 2))
print(myfunc(1, 2, 3))
print(myfunc(1, 2, 3, 4))

#In [23]:
def myfunc(param1, **kwargs):
    return f'param1: {param1}, others: {kwargs}'

#In [24]:
print(myfunc(param2='param2', param1=1,foo='foo'))

#In [25]:
def myfunc(param1, **kwargs):
    tmp = f'param1: {param1}'
    for item in kwargs.items():
        tmp += f', {item[0]}: {item[1]}'
    return tmp

print(myfunc(param2='param2', param1=1, foo='foo'))