from controller.controllers import BankController
from bussiness_logic_files.transaction_logic import Transactions
from view.views import View,user_input
def main():
    choice=user_input.enter_choice(main)
    if choice==1:
        bank = BankController(branch_name="Madurai", bank_name="IOB",address="valayapatti madurai-625022")
        bank.create_account(
            name="Muthu",
            dob="2004/10/25",
            phone="9314158089",
            email="muthuraja05980@gmail.com",
            acc_type="current",
            money=5000,
            address="solanguruni-madurai"
        )
    elif choice==2:
        amount=user_input.get_amout(main)
        Transactions().debit('1377',amount)
    elif choice==3:
        amount=user_input.get_amout(main)
        Transactions().credit('1377',amount)
    else:
        print("Invalid input")
        main()
    
