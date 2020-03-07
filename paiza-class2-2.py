class Box:
    def __init__(self, item):
        self.item = item

    def open(self):
        print("宝箱を開いた。" + self.item + "を手に入れた。")

class JewelryBox(Box):
    def look(self):
        print("宝箱はキラキラと輝いている。")

box = Box("鋼鉄の剣")
box.open()

jewelrybox = JewelryBox("魔法の指輪")
jewelrybox.look()
jewelrybox.open()

# 応用問題
# クラスにメソッドを定義しよう

class Greeting:
    def __init__(self):
        self.msg = "hello"
        self.target = "paiza"

class Hello(Greeting):
    #　この下に, say_helloメソッドを記述する
    def say_hello(self):
        print(self.msg + " " + self.target)


player = Hello()
player.say_hello()

# 応用問題２
# クラスを継承しよう

class Greeting:
    def __init__(self):
        self.msg = "hello"
        self.target = "paiza"

# この下に、Greetingクラスを継承した、Helloクラスを定義する。
# そこに、　say_hello()メソッドの定義を記述する.
class Hello(Greeting):
    def say_hello(self):
        print(self.msg + " " + self.target)

player = Hello()
player.say_hello()

