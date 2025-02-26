class View:
    
    @staticmethod
    def display_message(message):
        print(message)

    @staticmethod
    def display_account_details(account):
     
        print("Account Created Successfully!")
        print(f" Customer Name : {account.cust_name}")
        print(f" Date of Birth : {account.dob}")
        print(f" Phone Number  : {account.phone}")
        print(f" Email ID      : {account.email}")
        print(f" Account Type  : {account.type}")
        print(f" Customer ID   : {account.cust_id}")
        print(f" IFSC Code     : {account.cust_ifsc}")
        print(f" Balance       : ₹{account.balance}")

    @staticmethod
    def display_error(error_message):
        print(f"Error: {error_message}")
