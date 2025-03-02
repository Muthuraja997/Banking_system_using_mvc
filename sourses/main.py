from controller.controllers import BankController
from bussiness_logic_files.transaction_logic import Transactions
from view.views import View
def main():
    bank = BankController(branch_name="Madurai", bank_name="IOB",address="valayapatti madurai-625022")

    bank.create_account(
        name="Muthu",
        dob="25/10/2004",
        phone="9344058085",
        email="muthuraja05980@gmail.com",
        acc_type="current",
        money=5000
    )
    amount=View.get_amout()
    Transactions().debit('1124',amount)

    
