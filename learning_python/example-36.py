#In [1]
def some_func():
    print('some func')
    return 100

#In [2]
#def hello(whom):
    #print('hello' + whom) # whomは文字列でないとならない

#hello(100)

#In [*]
import random
answer = random.randint(1,100)

while True:# 無限ループ
    try:
        #例外を発生させる可能性があるコード
        number = int(input('100までの数値を入力してください:'))
    except ValueError:
        # ValueError例外を処理するコード
        print('数字以外が入力されました。数字のみを入力してください')
        continue
    if answer < number:
        print('もっと小さな数値です')
    elif answer > number:
        print('もっと大きな数値です')
    else:
        break# 変数answerの値と変数numberの値が等しければ終了

print('素晴らしい！正解です！')

#In [*]:
while True:
    try:
        print()
        print('1: ValueError例外を発生')
        print('2: IndexError例外を発生')
        print('3: 例外を発生させない')
        print('4: 終了')
        selection = int(input('どれにします:'))
        if selection == 1:
            tmp = int('foo')#ValueError
        elif selection == 2:
            tmp = 'str'[5]#IndexError
        elif selection == 3:
            print()
            print('例外を発生させませんでした')
        elif selection == 4:
            print()
            print('終了します')
            break
        else:
            print(undefined_var)#未定義の変数を参照
    except ValueError as e:
        print('Value Error')
        print(e.args)
        print()
    except IndexError:
        print('Index Error')
        print()
    except Exception as e:
        print('Exception')
        print(e.args)
        print()
    print('try文の直後の行を実行しました')

print('無限ループを終了しました')