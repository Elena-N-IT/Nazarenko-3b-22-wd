class Employee:
    def __init__(self, name, age, salary):
        self.name=name
        self.age=age
        self.salary=salary

    def info(self):
        print(self.name, "", "Возраст:", self.age, "", "Размер зарплаты:", self.salary, "")

employee=Employee("Денис Бондарев", 31, 250000)
employee.info()