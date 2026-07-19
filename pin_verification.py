from database import account 
class pinVerification :
    @staticmethod
    def verify_pin(account_no , pin):
        for account in accounts:
            if account["account_no"] += account_no and account["pin"] == pin :
                return account
            else :
                return None
             