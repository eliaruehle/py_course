class Bankaccount:

    forename:str
    surename:str
    balance:float
    active:bool

    def __init__(self, forename:str, surename:str, balance:float, active=True):
        self.forename = forename
        self.surename = surename
        self.balance = balance
        self.active = active

    def __str__(self) -> str:
        return f"This is the bank account of {self.forename} {self.surename}."
    
    def get_name(self) -> str:
        return f"{self.forename} {self.surename}"
    
    def get_balance(self) -> float:
        return self.balance
    
    def pay_in(self, amount:float) -> None:
        if not self.active:
            print("Account not active!")
            return
        if amount <= 0:
            print("Amount is to low!")
        elif amount >= 15000:
            self.balance += 0.99 * amount
        else:
            self.balance += amount
    
    def pay_out(self, amount:float) -> None:
        if not self.active:
            print("Account not active!")
            return
        if amount > self.balance:
            print("Not enough money on your account!")
        else:
            self.balance -= amount
    
    def deactivate(self):
        if self.active:
            self.active = False
    
    def activate(self):
        if not self.active:
            self.active = True

# main entry point of the programm
if __name__ == "__main__":
    account = Bankaccount("Max", "Mustermann", 20_000)
    
    # make a transaction:
    account.pay_in(10_000)
    print(account.get_balance())
    assert account.get_balance() == 30_000
    # make an invalid transaction:
    account.pay_in(-1)
    account.pay_out(40_000)
    # deactivate the account
    account.deactivate()
    # try a transaction: should print an error message
    account.pay_in(20)
    # reactivate the account
    account.activate()
    # try an transaction:
    account.pay_out(10_000)
    print(account.get_balance())
    assert account.get_balance() == 20_000