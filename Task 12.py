class Student:
    def __init__(self, name, surname, group, assessment):
        self.name=name
        self.surname=surname
        self.group=group
        self.assessment=assessment
    def gpa(self):
        print(sum(self.assessment)/len(self.assessment))

student=Student("Эльвира", "Бондарева", "51-N", [4, 5, 5])
student.gpa()