class Account:
    def __init__(self , name , pin , account_no , balance ,transactions):
        self.name = name
        self.pin =  pin
        self.account_no = account_no
        self.balance = balance
        self.trasactions = []

    @classmethod
    def create_account(cls):
        name = input("Enter  username")
        pin = int(input("Enter 4-digits pin"))
        account_no = int(input("Enter account_no"))
        while True:
            balance = float(input("Enter Intial Deposit(Minimum $500)"))
            if balance >= 500 :
                break 
            else:
                print("Intial Deposit must be minimun $500")

    
    return cls(name , pin , account_no , balance)
            
