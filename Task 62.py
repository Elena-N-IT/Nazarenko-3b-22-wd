class Robot:
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed

    def move(self, time):
        distance = self.speed * time
        print(f"{self.name} прошел {distance} километров.")

class CaterpillarRobot(Robot):
    def __init__(self, name, speed, territory):
        super().__init__(name, speed)
        self.territory = territory

class WheeledRobot(Robot):
    def __init__(self, name, speed, car_brand):
        super().__init__(name, speed)
        self.car_brand = car_brand


# Пример использования классов
robot1 = Robot("Обычный робот", 10)
robot1.move(5)  # Выводит: Обычный робот прошел 50 километров.

robot2 = CaterpillarRobot("Гусеничный робот", 5, "Лес")
robot2.move(3)  # Выводит: Гусеничный робот прошел 15 километров.

robot3 = WheeledRobot("Робот на колесах", 8, "Марка автомобиля")
robot3.move(2)  # Выводит: Робот на колесах прошел 16 километров.