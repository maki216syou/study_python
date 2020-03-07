class Box:
    def __init__(self, item):
        self.item = item

    def open(self):
        print("宝箱を開いた. " + self.item + "を手に入れた. ")

class MagicBox(Box):
    def look(self):
        print("宝箱は、妖しく輝いている. ")

    def open(self):
        print("宝箱を開いた. " + self.item + "が襲ってきた！")

box = Box("鋼鉄の剣")
box.open()

magicbox = MagicBox("モノマネモンスター")
magicbox.look()
magicbox.open()

# 演習課題
class Greeting:
    def __init__(self):
        self.msg = "hello"
        self.target = "paiza"

    def say_hello(self):
        print(self.msg + " " + self.target)

class Hello(Greeting):
    # ここにオーバーライドするメソッドを記述する
    def say_hello(self, target):
        print(self.msg + " " + target)
        

player = Hello()
player.say_hello("python")

# 演習課題２
class Greeting:
    def __init__(self):
        self.msg = "hello"
        self.target = "paiza"

    def say_hello(self):
        print(self.msg + " " + self.target)

class Hello(Greeting):
    def say_hello(self):
        print(self.msg + " " + self.target)
        print("YEAH YEAH YEAH!")


player = Hello()
player.say_hello()
