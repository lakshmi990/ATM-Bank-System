from database import accounts
class Authenticationn :
    @staticmethod
    def verify_pin(accounts ):
        for account in accounts:
            if account.pin == pin :
                return account
            
        return None
    @staticmethod
    def verify_accountNo(accounts):
        for account in accounts:
            if account.pin == account_no:
                return account
            
        return None
             