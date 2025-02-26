from abc import ABC, abstractmethod
import random
from table_logic import add_details


class Account(ABC):
    
    def __init__(self, cust_name, dob, phone, email, acc_type, money, branch_ifsc):
        self.cust_name = cust_name
        self.dob = dob
        self.phone = phone
        self.email = email
        self.type = acc_type
        self.cust_ifsc = branch_ifsc  
        self.cust_id = random.randint(999, 1500)  
        self.balance = money
        add_details([self.cust_name,self.dob,self.phone,self.email,self.type,str(self.cust_id),str(self.cust_ifsc),self.balance],'customers',8)
    # def to_list(self):
     
    #     return [self.cust_name, self.dob, self.phone, self.email, self.type, str(self.cust_id), str(self.cust_ifsc), self.balance]

    @abstractmethod
    def withdraw(self, amount):
        pass

    @abstractmethod
    def deposit(self, amount):
        pass


class Savings(Account):
    def withdraw(self, amount):
        if self.balance - amount >= 1000:
            self.balance -= amount
            return f"Withdrawn ₹{amount}. Balance: ₹{self.balance}"
        return "Invalid."

    def deposit(self, amount):
        self.balance += amount
        return f"Deposited ₹{amount}. New Balance: ₹{self.balance}"

class Current(Account):
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return f"Withdrawn ₹{amount}.Balance: ₹{self.balance}"
        return "Invalid"

    def deposit(self, amount):
        self.balance += amount
        return f"Deposited ₹{amount}. Balance: ₹{self.balance}"

class LoanAccount(Account):
   

    def withdraw(self, amount):
        return "Withdrawals are not allowed for loan accounts."

    def deposit(self, amount):
        self.balance -= amount 
        return f"Loan repayment of ₹{amount} made.  loan: ₹{self.balance}"


class Branch:
  

    def __init__(self, branch_name, bank_name,address):
        self.branch_name = branch_name
        self.bank_name = bank_name
        self.address=address
        self.ifsc_code = random.randint(1500, 2500)  

    def create_account(self, cust_name, dob, phone, email, acc_type, money):
        account = self._get_account_type(cust_name, dob, phone, email, acc_type, money, self.ifsc_code)
        # add_details(account.to_list(), 'customers', 8)
        # return account

    def _get_account_type(self, name, dob, phone, email, acc_type, money, ifsc):
        if acc_type.lower() == "savings":
            return Savings(name, dob, phone, email, acc_type, money, ifsc)
        elif acc_type.lower() == "current":
            return Current(name, dob, phone, email, acc_type, money, ifsc)
        elif acc_type.lower() == "loan":
            return LoanAccount(name, dob, phone, email, acc_type, money, ifsc)
        else:
            raise ValueError("Invalid")

    def save_branch(self):
        add_details([str(0), self.branch_name, self.bank_name, str(self.ifsc_code), self.address], 'branch', 5)
