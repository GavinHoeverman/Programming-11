import myClass

acct_list = ['', ' ' , '', '' , '' , '']

option = int(input('1- add an account, 2- Withdraw, 3- Deposit. Please anter 1, 2, or 3:'))

if option == 1:
    print('This option allows you to add a new account to the end of the list?')
    print(acct_list)
    acct = input('what is your name?')
    acct_list.append(acct)
    print(acct_list)

elif option == 2:
    print('This option allows you to remove a city from the list')
    print(acct_list)

    acct_to_remove= input('What city should be removed the list?')

    if acct_to_remove in acct_list:
        acct_list.remove(acct_to_remove)
        print(acct_list)
    else:
        print('That account is not on the list')

        
elif option == 3:
    print('How much would you like to deposit?')
    acct = input('Who is the owner of the account?')
    pos = int(input('Where on the list would you like to add it?'))

    if pos <len(acct_list):
        acct_list.insert(pos, acct)
        print(acct_list)

    else:
        print('Invalid position')
    
