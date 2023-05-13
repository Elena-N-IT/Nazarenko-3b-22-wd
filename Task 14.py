class Student:

    def __init__(self, name, surname, age, speciality):
        self.name=name
        self.lastname=surname
        self.age=age
        self.speciality=speciality

    def info(self):
        print(self.name, "-", self.lastname, self.age,"лет", self.speciality)


student=Student("Эльвира", "Бондарева", 30, "Юриспруденция")
student.info()