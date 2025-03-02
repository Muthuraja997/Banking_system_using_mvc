class View:

    def display_message(message):
        print(message)

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

   
    def display_error(error_message):
        print(f"Error: {error_message}")
class user_input:
    def get_amout(self):
        amount=int(input("Enter The amount:"))
        return amount
    def enter_choice(self):
        print("1.Create a account")
        print("2.withraw")
        print("3.deposit")
        choice=int(input())
        return choice
            