import myClass
import time

acct = []

checkacct = input('do you have an account')

if checkacct.upper == ('no') or checkacct.upper == ('n'):
    name = input('Name?')
    bank = input('Deposit?')
    passw = input('Password make')

elif checkacct.upper == ('yes') or checkacct.upper == ('y'):
    print('Fortnite Vbuck Bank')
    checkName
    checkpassw
    enter = True
else:
    checkacct

while enter == True:
    if name == checkName and passw == checkpassw:
    print('')
    time.sleep(2)
    deposity = input('')
    myClass.acct.deposit
    withdraw = input('')
    myClass.acct.withdraw
    print(myClass.acct.balance)

##acct.append(myClass.acct(name, bank, passw))
##
##checkName = input('what is your name')
##checkpassw = input('what is your password?')
##enter = True
##
##if name == checkName and passw = checkpassw:
##    print('')
