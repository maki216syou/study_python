# Humanというクラスを作成します
class Human:
    class_name = "Human"

    def __init__(self):
        self.name = None

    def show(self):
        print(self.name)

# Humanクラスのインスタンスhumanを作成する
human = Human()

# humanの変数nameに大泉という文字を保存します
human.name = "大泉"

# humanのメソッドであるshow()を実行します。
# ターミナルには大泉と表示されます。
human.show()

# Human クラス内にあるクラス変数class_nameをターミナルに表示しています。
print(Human.class_name)

