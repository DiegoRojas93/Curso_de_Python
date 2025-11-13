class BankAccount:
    
    interest_rate = 0.02
    
    def __init__(self, holder, balance):
        self.holder = holder
        self.balance = balance
        
    @classmethod
    def change_interest_rate( cls, new_rate ):
        print(f'\nInteres anterior: {cls.interest_rate}.')
        cls.interest_rate = new_rate
        print(f'Interés actual: {cls.interest_rate}.\n')
        
    @staticmethod
    def validate_amount(amount):
        return amount > 0
        
    def withdraw(self, amount):
        if self.validate_amount(amount):
            if self.balance >= amount:
                self.balance -= amount
                print("Retiro éxitoso.")
            else:
                print("Balance insuficiente.")
        else:
            print("El monto debe ser mayor a cero.")
            
acount1 = BankAccount('Diego', 1000)
acount2 = BankAccount('Maria', 300)

BankAccount.change_interest_rate(0.03)

acount1.withdraw(500)
acount2.withdraw(500)

print(BankAccount.validate_amount(100))
print(BankAccount.validate_amount(-100))