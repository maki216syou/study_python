# coding; utf-8
# RPGの敵クラスを作る

class Enemy:
    def __init__(self, name):
        self.name = name
    
    def attack(self):
        print(self.name + "は勇者を攻撃した")

enemies = []
enemies.append(Enemy("スライム"))
enemies.append(Enemy("モンスター"))
enemies.append(Enemy("ドラゴン"))

for enemy in enemies:
    enemy.attack()


#　演習課題

# coding: utf-8
# RPGの攻撃シーン

class Player:
    def __init__(self, name):
        self.name = name

    def attack(self, enemy):
        print(self.name + "は" + enemy + "を攻撃した")

team = []
team.append(Player("勇者"))
team.append(Player("戦士"))
team.append(Player("魔法使い"))

for player in team:
    player.attack("スライム")