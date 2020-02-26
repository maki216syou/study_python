# coding: utf-8
# クラスを作成する

class Player:
    def walk(self):
        print("勇者は荒野を歩いていた")
    def attack(self, enemy):
        print("勇者は" + enemy + "を攻撃した")

player1 = Player()
player1.walk()
player1.attack("スライム")

# 演習課題

# coding: utf-8
# クラスからオブジェクトを作成しよう

class Greeting:
    def say_hello(self):
        print("hello paiza")

# この下に、必要なコードを追加してください
paiza = Greeting()
paiza.say_hello()

# 演習課題2

# coding: utf-8
# クラスにメソッドを定義しよう

class Greeting:
    # この下に、必要なコードを追加してください
    def say_hello(self):
        print("hello python")

paiza = Greeting()
paiza.say_hello()


