from Authentication import Authenticationn
from create_account import Account

while True :
    print("---WELCOME TO YONO SBI---")
    print("International or Local") 
    print(" 1. Create an account") 
    print(" 2. Deposit money")
    print(" 3. Withdrawl money")
    print(" 4. Check balance")
    print(" 5. Save transaction history")
    print(" 6. Exit")
    choice = int (input(" select one option : "))
    if choice == 1 :
        Account.create_account()
        
        print("Account created scuccessfully !...")
    elif choice == 2 :
        deposit_money()
        if account : 
            print("Login succesfull")
        else:
            print("Check account number or pin")

    elif choice == 3 :
        withdrawl_money()
    elif choice == 4 :
        check_balance()
    elif choice ==5 :
        save_history()
    elif choice == 6:
        exit()
    else :
        print("")