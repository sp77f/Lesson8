from abc import ABC , abstractmethod

class Weapon(ABC):
    @abstractmethod
    def attack(self):
        pass
class Sword():
    def __init__(self,name,damage):
        self.name = name
        self.damage = damage
    def attack(self):
        print("Боец наносит удар мечом. Монстру причинен урон "+str(self.damage))

class Knife(Weapon):
    def __init__(self,name,damage):
        self.damage = damage
        self.name = name
    def attack(self):
        print("Боец наносит удар ножом. Монстру причинен урон "+str(self.damage))

class Bow(Weapon):
    def __init__(self,name,damage):
        self.damage = damage
        self.name = name
    def attack(self):
        print("Боец наносит удар из лука. Монстру причинен урон "+str(self.damage))

class Fighter():
    def __init__(self,weapon):
        self.weapon = weapon
    def fight(self,weapon):
        weapon.attack()
    def changeWeapon(self,weapon):
        self.weapon = weapon
        print("Боец выбрал оружие "+str(self.weapon.name))
class Monster():
    def __init__(self,health):
        self.health = health
    def change_health(self,damage):
        self.health = self.health - damage


sword = Sword("Меч Паладина",20)
knife = Knife("Нож ассасина",5)
bow = Bow("Лук Эбонит",15)
fighter = Fighter(sword)
monster_health = 40
monster = Monster(monster_health)
print("Появился монстр. Он имеет здоровье "+str(monster.health))
while monster.health > 0:
    weapon = input("Выберите оружие: 1 - меч, 2 - нож, 3 - лук: ")
    if weapon == '1':
        fighter.changeWeapon(sword)
        fighter.fight(sword)
    elif weapon == '2':
        fighter.changeWeapon(knife)
        fighter.fight(knife)
    elif weapon == '3':
        fighter.changeWeapon(bow)
        fighter.fight(bow)
    else:
        print("Неверный ввод")
        continue
    monster.change_health(fighter.weapon.damage)
    monster_health = monster.health
    if monster_health < 0:
        monster_health = 0
    print("Здоровье монстра "+str(monster_health))
print("Монстр погиб")

