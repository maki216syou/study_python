class Player:
    def __init__(self, name):
        self.name = name

    def attack(self, enemy):
        print(self.name + "は、" + enemy + "を攻撃した！")

class Wizard(Player):
    def attack(self, enemy):
        print("ズバーン！")
        print(self.name + "は、" + enemy + "に炎を放った！")

print("=== パーティーでスライムと戦う ===")
hero = Player("勇者")
# hero.attack("スライム")
warrior = Player("戦士")
wizard = Wizard("魔法使い")

party = [hero, warrior, wizard]
for member in party:
    member.attack("スライム")

#　演習課題

# coding: utf-8
# RPGの攻撃シーン

class Player:
    def __init__(self, name):
        self.name = name

    def attack(self, enemy):
        print(self.name + "は" + enemy + "を攻撃した")

class Warrior(Player):
    def attack(self, enemy):
        print(self.name + "は" + enemy + "を猛攻撃した")

team = []
team.append(Player("勇者"))
team.append(Player("魔法使い"))
team.append(Warrior("戦士"))


for person in team:
    person.attack("スライム")
