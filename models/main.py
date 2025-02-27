from controllers import BankController

if __name__ == "__main__":
    bank = BankController(branch_name="Madurai", bank_name="IOB",address="valayapatti madurai-625022")

    bank.create_account(
        name="Muthu",
        dob="25/10/2004",
        phone="9344058085",
        email="muthuraja05980@gmail.com",
        acc_type="current",
        money=5000
    )

    
