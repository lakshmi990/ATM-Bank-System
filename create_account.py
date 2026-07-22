from Authentication import Authentication
from database import accounts ,load_accounts
class Account:
    def __init__(self , name , pin , account_no , balance ):
        self.name = name
        self.pin =  pin
        self.account_no = account_no
        self.balance = balance
        

    @classmethod
    def create_account(cls):
        name = input("Enter  username : ")
        pin = int(input("Enter 4-digits pin : "))
        while True:
            account_no = int(input("Enter account_no : "))
            verify_obj = Authentication()
       
            account_verify = verify_obj.verify_accountNo(account_no)
          
            if  account_verify :
                print("This account already exist!")
                continue
                
            else:
                break
                
        
        while True:
            balance = float(input("Enter Intial Deposit(Minimum $500) : "))
            if balance >= 500 :
                break 
            else:
                print("Intial Deposit must be minimun $500")
        new_account =  cls( name , pin , account_no , balance)
        accounts.append(new_account)
        load_accounts( new_account )
        return new_account


    
        
        
            
