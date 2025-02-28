from models import Branch
from table_logic import generate_get_amount_query
from controllers import TransactionController
class Transactions:
    def debit(self,acc_no,amount):
        balance_and_type=self.chack(acc_no)
        current_money=TransactionController().money_transfer_debit(balance_and_type,amount)
        print(current_money)
    def chack(self,acc_no):
        v=generate_get_amount_query(acc_no,'account')
        return v
ob=Transactions()
ob.debit('1124',100)