class acct:
    def __init__(self, owner, balance=0, password):
        self.owner = owner
        self.balance = balance
        self.password = password

    def __str__(self):
        return f'acct owner:{self.owner}\nacct balance: ${self.balance}'

    def deposit(self, dep_amt):
        self.balance += dep_amt
        print("your deposit has been accepted")

    def withdraw(self, wd_amt):
        if wd_amt < self.balance:
            self.balance -= wd_amt
            print('Withdrawl accepted', self.owner)

        elif wd_amt == self.balance:
            self.balance -= wd_amt
            print('Account closed', slef.owner)
        else:
            print('Poor',self.owner)



