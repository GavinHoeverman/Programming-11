##answer=input('Would you like the sauce?')
##if answer.lower() == 'yes':
##    print('You have aquired the sauce')
##    print('You are speaking the language of the Gods!')
##
##if answer == 'no':
##    print('You must be an illiterate fool to not want the sauce')
##    print('you will never be worthy')

####deposit = input('Deposit amount?')
####if float (deposit)> 100:
####    print('you get a free toaster')
####else:
####    print ('you degenerate')
####print('have a nice day')
####    
##tax=12
##deposit=input(float 'How much you spend at the club tonight')
##if float (deposit)> 100:
##    print ('you have been granted free drank')
##else:
##    print('Banned')

tax=12
item_1 = float(input ("Enter the price of your first drank: "))
item_2 = float(input ("how much did you pay to get in: "))
item_3 = float(input ("how much did you pay to dance: "))
price_without_tax = item_1 + item_2 + item_3
print ('Cost before tax %.2f' % price_without_tax)
Cost = price_without_tax*tax
print('Aight G, you owe %.2f dollars' % Cost)
