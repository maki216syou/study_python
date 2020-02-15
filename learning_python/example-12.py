#In [1]
def hello(whom):
    message = 'Hello' + str(whom)
    print(message)

#In [2]
hello('World')

#In [3]
def get_ans4ultimateQ():
    return 42
#In [4]
def get_ans4ultimateQ():
    return 42 #関数の実行はここで終了
    print('can not reach this line') # この行は実行されることはない
#In [5]
result = get_ans4ultimateQ()
print(result)

#In [6]
print(get_ans4ultimateQ())

#In [12]
def fizzbuzz(number):
    result = str(number)
    if number % 3 == 0 and number %5 == 0:
        result = 'FizzBuzz'
    elif number %3 == 0:
        result = 'Fizz'
    elif number %5 == 0:
        result = 'Buzz'
    return result

number = input('何か数値を入力してください: ')
number = int(number)

print(fizzbuzz(number))

#In [13]
print(some_func())

def some_func():
    print('you called some_func')


