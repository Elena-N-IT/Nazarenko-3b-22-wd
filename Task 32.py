class Student:
    def __init__(self, name, clas):
        self.name=name
        self.clas=clas

    def study(self):
        print("Школьник", self.name, "", "учится в", self.clas, "", "классе")


Student1 = Student("Элла", 5)

Student1.study()