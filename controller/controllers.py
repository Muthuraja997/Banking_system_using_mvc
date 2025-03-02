from  sourses.models import Savings,Current,LoanAccount,Branch
from view.views import View

class BankController:

    def __init__(self, branch_name, bank_name,address):
        self.branch = Branch(branch_name, bank_name,address)
        self.branch.save_branch()
      
    def create_account(self, name, dob, phone, email, acc_type, money,address):
        try:
            self.branch.create_account(name, dob, phone, email, acc_type, money,address)
        except ValueError as e:
            View.display_message(str(e))
class TransactionController:
    def money_transfer_debit(self,data_list,money):
         if data_list[0]=='savings':
             amount=Savings('one','two').withdrow(money,data_list[1])
             return amount
         if data_list[0]=='current':
             amount=Current('one','two').withdraw(money,data_list[1])
             return amount
         if data_list[0]=='loan':
             LoanAccount('one','two').withdrow(data_list[1])
    def money_transfer_credit(self,data_list,money):
         if data_list[0]=='savings':
             amount=Savings('one','two').deposit(money,data_list[1])
             return amount
         if data_list[0]=='current':
             amount=Current('one','two').deposit(money,data_list[1])
             return amount
         if data_list[0]=='loan':
             LoanAccount('one','two').deposit(money,data_list[1])
             
             