from models import Branch
from views import View

class BankController:


    def __init__(self, branch_name, bank_name,address):
        self.branch = Branch(branch_name, bank_name,address)
        self.branch.save_branch()

    def create_account(self, name, dob, phone, email, acc_type, money):
        try:
            self.branch.create_account(name, dob, phone, email, acc_type, money)
            # View.display_account_details(account)
        except ValueError as e:
            View.display_message(str(e))
