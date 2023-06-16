class GameCharacter:
    def __init__(self, name, level, health, attack, defense):
        self.name = name
        self.level = level
        self.health = health
        self.attack = attack
        self.defense = defense

    def apply_damage(self, damage):
        self.health -= damage

    def level_up(self):
        self.level += 1
        self.health *= 1.1
        self.attack *= 1.1

    def print_status(self):
        print(f"Имя: {self.name}")
        print(f"Уровень: {self.level}")
        print(f"Здоровье: {self.health}")
        print(f"Атака: {self.attack}")
        print(f"Защита: {self.defense}")
        print()


# Создаем персонажи
character1 = GameCharacter("Персонаж 1", 1, 100, 10, 5)
character2 = GameCharacter("Персонаж 2", 1, 100, 8, 7)

# 3 раунда битвы
for i in range(1, 4):
    print(f"Раунд {i}:")
    print("----------")

    # character1 атакует character2
    damage = character1.attack - character2.defense
    if damage > 0:
        character2.apply_damage(damage)

    # character2 атакует character1
    damage = character2.attack - character1.defense
    if damage > 0:
        character1.apply_damage(damage)

    # Выводим статус после раунда
    print("Статус персонажей после раунда:")
    character1.print_status()
    character2.print_status()

    print()

# Определение победителя
print("Итоговый результат:")
if character1.health > character2.health:
    print(f"Победитель: {character1.name}")
    print(f"Проигравший: {character2.name}")
elif character1.health < character2.health:
    print(f"Победитель: {character2.name}")
    print(f"Проигравший: {character1.name}")
else:
    print("Ничья")