from database import accounts
class Authenticationn :
    @staticmethod
    def verify_accountNo(account_no):
        for account in accounts:
            if account["account_no"] == account_no:
                return account
            
        return None
             