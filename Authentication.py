from database import accounts
class Authentication :
    @staticmethod
    def verify_accountNo(account_no):
        for account in accounts:
            if account["account_no"] == account_no:
                return account
            
        return None
    @staticmethod
    def verify_pin(pin):
        for account in accounts:
            if account["pin"] == pin :
                return account
                
             