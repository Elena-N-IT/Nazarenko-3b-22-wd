class Person:
    def __init__(self, name, age):
        self.name=name
        self.age=age
    def about_person(self):
        print("Имя:", self.name, "Возраст (полных лет):", self.age)

person1 = Person("Андрей", 30)
person1.about_person()