class Dog:
    def __init__(self, name, breed, age):
        self.name=name
        self.breed=breed
        self.age=age
    def about_dog(self):
        print("Имя:", self.name, "Порода:", self.breed, "Возраст (полных лет):", self.age)

dog1 = Dog("Тотошка", "джек-рассел", 1)
dog1.about_dog()