#activity2
make a bankaccount class with private balance and controlled deposit/withdraw methods


class BankAccount:
	def __init__(self,balance):
		self.__balance=balance
	@property
	def name(self):
		return self.__name
	@balance.setter
	def balance(self,value):
		if value.strip():
			self.__name=value
p=BankAccount("SKY123")
print(p.balance)
p.balance


class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Private balance

    @property
    def balance(self):
        return self.__balance
    
    @balance.setter
    def balance(self, value):
        if isinstance(value, (int, float)) and value >= 0:
            self.__balance = value
        else:
            print("Invalid balance amount.")
    
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("Deposit must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient balance or invalid amount.")



		