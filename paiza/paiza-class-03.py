# coding: utf-8
#　変数をクラスで管理する

class Player:
    def __init__(self, job):
        self.job = job

    def walk(self):
        print(self.job + "は荒野を歩いていた")

player1 = Player("戦士")
player1.walk()

player2 = Player("魔法使い")
player2.walk()

player1.walk()

#　演習課題
# coding: utf-8
# クラスからオブジェクトを作成しよう

class Greeting:
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print("hello " + self.name)

# この下に、必要な処理を記述します
paiza = Greeting("paiza")
paiza.say_hello()

#  演習課題２

# coding: utf-8
# クラスにインスタンス変数を追加しよう

class Greeting:
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print("hello " + self.name)

paiza = Greeting("paiza")
paiza.say_hello()
