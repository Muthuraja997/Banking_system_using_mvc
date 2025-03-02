# from sourses.models import Branch
from bussiness_logic_files.table_logic import generate_get_amount_query,generate_put_amount_query
from controller.controllers import TransactionController
class Transactions:
    def debit(self,acc_no,amount):
        balance_and_type=self.chack(acc_no)
        current_money=TransactionController().money_transfer_debit(balance_and_type,amount)
        generate_put_amount_query(acc_no,current_money,'account')
    def chack(self,acc_no):
        v=generate_get_amount_query(acc_no,'account')
        return v
    def credit(self,acc_no,amount):
        balance_and_type=self.chack(acc_no)
        current_money=TransactionController().money_transfer_credit(balance_and_type,amount)
        generate_put_amount_query(acc_no,current_money,'account')