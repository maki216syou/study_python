def myfunc():
    print('b:',b)
b = 'Python'
myfunc()

def myfunc():
    global a    #「a」はグローバル変数aであると宣言
    a = 'Python' # グローバル変数aの値を変更
    print('a:', a)

a = 'Ruby'
myfunc()
print(a)
