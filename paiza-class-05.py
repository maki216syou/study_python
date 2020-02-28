# coding: utf-8
# クラスで、引数と戻り値のあるメソッドを作る

class Item:
    tax = 1.08
    
    def __init__(self, price, quantity):
        self.price = price
        self.quantity = quantity
        
    def total(self):
        return int(self.price * self.quantity * Item.tax)
        
apple = Item(120, 15)
total = apple.total()
print("合計金額は" + str(apple.total()) + "円です")

orange = Item(85, 32)
print("合計金額は" + str(orange.total()) + "円です")

#　演習課題
# coding: utf-8
# 学生メソッドを呼び出す

class Gakusei:
    def __init__(self, kokugo, sansu):
        self.kokugo = kokugo
        self.sansu  = sansu

    def sum(self):
        return str(self.kokugo + self.sansu)

# この下に、必要な処理を記述します
yamada = Gakusei(70, 43)
print("合計は" + yamada.sum() + "点です")

# 演習課題2

# coding: utf-8
# 学生メソッドを作る

class Gakusei:
    def __init__(self, kokugo, sansu):
        self.kokugo = kokugo
        self.sansu  = sansu

    # この下に、合計得点を戻り値として返すsumメソッドを記述する
    def sum(self):
        return str(self.kokugo + self.sansu)
yamada = Gakusei(70, 43)
print("合計は" + str(yamada.sum()) + "点です")
