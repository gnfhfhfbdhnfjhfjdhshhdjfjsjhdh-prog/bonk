
class Bank:

    def _init_(self, name, balance):
        self.name = name
        self.__balance = balance
        self.history = []

    # Getter
    def get_balance(self):
        return self.__balance

    # Setter
    def set_balance(self, amount):
        if amount >= 0:
            self.__balance = amount
        else:
            print("Invalid balance!")

    def deposit(self, amount):
        if amount > 0:
            self.set_balance(self.get_balance() + amount)
            self.history.append(f"Deposit: {amount}")
            print("Deposit successful!")
        else:
            print("Invalid amount!")

    def withdraw(self, amount):
        if 0 < amount <= self.get_balance():
            self.set_balance(self.get_balance() - amount)
            self.history.append(f"Withdraw: {amount}")
            print("Withdraw successful!")
        else:
            print("Insufficient balance!")

    def transfer(self, other, amount):
        if other is self:
            print("Cannot transfer to same account!")

        elif 0 < amount <= self.get_balance():
            self.set_balance(self.get_balance() - amount)
            other.set_balance(other.get_balance() + amount)

            self.history.append(f"Transfer: {amount}")
            other.history.append(f"Received: {amount}")

            print("Transfer successful!")
        else:
            print("Invalid amount or balance!")

    def show_balance(self):
        print(self.name, self.get_balance())

    def show_history(self):
        for transaction in self.history:
            print(transaction)


account1 = Bank("Mohamed", 1000)
account2 = Bank("Ahmed", 500)

while True:
    print("\n1. Deposit")
    print("2. Withdraw")
    print("3. Balance")
    print("4. Transfer")
    print("5. History")
    print("6. Exit")

    choice = input("Choose: ")

    if choice == "1":
        amount = float(input("Amount: "))
        account1.deposit(amount)

    elif choice == "2":
        amount = float(input("Amount: "))
        account1.withdraw(amount)

    elif choice == "3":
        account1.show_balance()

    elif choice == "4":
        amount = float(input("Amount: "))
        account1.transfer(account2, amount)

    elif choice == "5":
        account1.show_history()



    else:
        print("Wrong choice")