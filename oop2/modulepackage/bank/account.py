class Account:
    def __init__(self) -> None:
        self.acctype = 'Saving'
        self.accno = ''
        self.balance = 0

    def open_account(self,name:str,acctype:str,accno:str,balance:int):
        self.name = name
        self.acctype = acctype
        self.accno = accno
        self.balance = balance

    def display_balance(self):
        return f'{self.name} account balance = {self.balance} baht'