class Bank:
    def __init__(self):
        self.clients = {}

    def create_client(self, name):
        if name not in self.clients:
            self.clients[name] = {}

    def open_account(self, client_name, account_name, initial_balance):
        if client_name in self.clients:
            if account_name not in self.clients[client_name]:
                if initial_balance >= 0:
                    self.clients[client_name][account_name] = initial_balance
                    print(f"Открыт счет '{account_name}' для клиента '{client_name}' с начальным балансом {initial_balance}.")
                else:
                    print("Отрицательный начальный баланс не допускается.")
            else:
                print(f"Счет '{account_name}' уже существует для клиента '{client_name}'.")
        else:
            print(f"Клиент '{client_name}' не найден.")

    def make_transfer(self, from_client, from_account, to_client, to_account, amount):
        if from_client in self.clients and to_client in self.clients:
            if from_account in self.clients[from_client] and to_account in self.clients[to_client]:
                if self.clients[from_client][from_account] >= amount:
                    self.clients[from_client][from_account] -= amount
                    self.clients[to_client][to_account] += amount
                    print(f"Перевод с '{from_account}' на '{to_account}' успешно выполнен.")
                else:
                    print("Недостаточно средств на счете отправителя.")
            else:
                print("Указанный счет не найден у клиента.")
        else:
            print("Один из клиентов не найден.")


# Пример использования класса
bank = Bank()
bank.create_client("Иванов")
bank.open_account("Иванов", "Счет1", 1000)
bank.create_client("Петров")
bank.open_account("Петров", "Счет2", 500)
bank.make_transfer("Иванов", "Счет1", "Петров", "Счет2", 300)