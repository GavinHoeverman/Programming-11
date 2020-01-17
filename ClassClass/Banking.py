import myClass

acct1 = myClass.acct('Gavin', 1000000)
acct2 = myClass.acct('Nick', 100)

acct1.deposit(200)
acct1.withdraw(700)
acct2.deposit(300)
acct2.withdraw(400)


print(acct1.owner, acct1.balance)
print(acct2.owner, acct2.balance)
acct1.deposit(20.23*1.22)
print(acct1.__str__())
print(acct2.__str__())
