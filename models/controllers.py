from models import Branch
from models import Savings,Current,LoanAccount
from views import View

class BankController:

    def __init__(self, branch_name, bank_name,address):
        self.branch = Branch(branch_name, bank_name,address)
        self.branch.save_branch()
      
    def create_account(self, name, dob, phone, email, acc_type, money):
        try:
            self.branch.create_account(name, dob, phone, email, acc_type, money)
        except ValueError as e:
            View.display_message(str(e))
class TransactionController:
    def money_transfer_debit(self,data_list,money):
         if data_list[0]=='savings':
             amount=Savings().withdrow(money,data_list[1])
             return amount
         if data_list[0]=='current':
             amount=Current('one','two').withdraw(money,data_list[1])
             return amount
        #  if data_list[0]=='loan':
        #      LoanAccount().withdrow(data_list[1])
             
             