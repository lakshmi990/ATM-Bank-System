
from database import accounts
from Authentication import Authentication
class Deposit:

    def __init__( self , amount):
        self.amount = amount
    @classmethod
    def deposit_money(cls):
        
        while True:
            account_no = int(input( " Enter account_no"))
            verify = Authentication()
            account = verify.verify_accountNo(account_no)
            if account is None:
                print("Wrong account_no")
                return
                amount = float(input("Enter amount"))
            
            pin = int(input("Enter Pin"))
            pin_verify = verify.verify_pin(pin)
            if not pin_verify:
                print("Incorrect Pin!")
                return 
           
            account.balance+=amount
            print("Deposited Sucessfully---")

 
    

