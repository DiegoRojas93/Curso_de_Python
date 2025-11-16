class bankAccount:
    def __init__(self, balance):
        self.__balance = balance
        
    def deposit(self, amount):
        if( amount > 0 ):
            self.__balance += amount
        
    def get_balance(self):
        return self.__balance
    
acount = bankAccount(1000)
acount.deposit(500)
print(f"Balance: {acount.get_balance()}")