class ProductCard:
    def __init__(self, name, cost, quantity):
        self.name = name
        self.cost = cost
        self.quantity = quantity

    def decrease_quantity(self, amount):
        if self.quantity >= amount:
            self.quantity -= amount
            print(f"Количество товара '{self.name}' уменьшено на {amount}.")
        else:
            print("Недостаточное количество товара.")

    def change_cost(self, new_cost):
        if new_cost >= 0:
            self.cost = new_cost
            print(f"Стоимость товара '{self.name}' изменена на {new_cost}.")
        else:
            print("Отрицательная стоимость товара не допускается.")


# Пример использования класса
product = ProductCard("Мобильный телефон", 1000, 10)
product.decrease_quantity(5)  # Выводит: Количество товара 'Мобильный телефон' уменьшено на 5.
product.change_cost(1200)  # Выводит: Стоимость товара 'Мобильный телефон' изменена на 1200.