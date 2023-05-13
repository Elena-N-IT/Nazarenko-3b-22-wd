class Cat:

    def __init__(self, name, age, color):
        self.name=name
        self.age=age
        self.color=color

    def description(self):
        print("Кошка по имени",self.name, ",", self.age, "лет,","цвет", self.color)


cat1=Cat("Пушок", 6, "рыжий")
cat1.description()