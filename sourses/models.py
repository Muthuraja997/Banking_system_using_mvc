from abc import ABC, abstractmethod
import random
from bussiness_logic_files.table_logic import add_details
from view.views import View
# from Views import View
class Account(ABC):
    def __init__(self,*args): #self, cust_name, dob, phone, email, acc_type, money, branch_ifsc):
        self.cust_name = args[0]
        self.dob = args[1]
        self.phone = args[2]
        self.email = args[3]
        self.type = args[4]
        self.cust_ifsc = args[6]  
        self.cust_id = random.randint(999, 1500)  
        self.balance = args[5]
        self.acc_no=random.randint(999,1500)
        # add_details([self.cust_name,self.dob,self.phone, self.email,str(self.cust_id)],'customers')
        # add_details([str(self.acc_no),str(self.cust_id),str(self.balance),self.type],'account')
    @abstractmethod
    def withdraw(self, amount):
        pass
    @abstractmethod
    def deposit(self, amount):
        pass
class Savings(Account):
    def __init__(self,*args): #self, cust_name, dob, phone, email, acc_type, money, branch_ifsc):
        if len(args)!=2:
            self.cust_name = args[0]
            self.dob = args[1]
            self.phone = args[2]
            self.email = args[3]
            self.type = args[4]
            self.cust_ifsc = args[6]  
            self.cust_id = random.randint(999, 1500)  
            self.balance = args[5]
            self.acc_no=random.randint(999,1500)
            self.address=args[7]
            add_details([str(self.cust_id),self.cust_name,self.email,self.phone,self.address,self.dob,str(self.cust_ifsc)],'customers')
            add_details([str(self.acc_no),str(self.cust_id),self.type,self.balance],'account')

    def withdraw(self, amount,balance):
        if balance - amount >= 1000:
            balance -= amount
            return balance

    def deposit(self, amount,balance):
        balance += amount
        return balance

class Current(Account):
    def __init__(self,*args): #self, cust_name, dob, phone, email, acc_type, money, branch_ifsc):
        if len(args)!=2:
            self.cust_name = args[0]
            self.dob = args[1]
            self.phone = args[2]
            self.email = args[3]
            self.type = args[4]
            self.cust_ifsc = args[6]  
            self.cust_id = random.randint(999, 1500)  
            self.balance = args[5]
            self.acc_no=random.randint(999,1500)
            self.address=args[7]
            add_details([str(self.cust_id),self.cust_name,self.email,self.phone,self.address,self.dob,str(self.cust_ifsc)],'customers')
            add_details([str(self.acc_no),str(self.cust_id),self.type,self.balance],'account')
        # self.amount=amount
        # self.balance=balance
    def withdraw(self, amount,balance):
        if balance >= amount:
            balance -= amount
            return balance
  

    def deposit(self, amount,balance):
        balance += amount
        return balance

class LoanAccount(Account):
    def __init__(self,*args): #self, cust_name, dob, phone, email, acc_type, money, branch_ifsc):
        if len(args)!=2:
            self.cust_name = args[0]
            self.dob = args[1]
            self.phone = args[2]
            self.email = args[3]
            self.type = args[4]
            self.cust_ifsc = args[6]  
            self.cust_id = random.randint(999, 1500)  
            self.balance = args[5]
            self.acc_no=random.randint(999,1500)
            self.address=args[7]
            self.branch_id=args[8]
            add_details([str(self.cust_id),self.cust_name,self.email,self.phone,self.address,self.dob,str(self.cust_ifsc)],'customers')
            add_details([str(self.acc_no),str(self.cust_id),self.type,self.balance],'account')
    def withdraw(self, amount):
        return "Withdrawals are not allowed for loan accounts."
    
    def deposit(self, amount,balance):
        balance += amount 
        return balance


class Branch:
    _customers=[]
    def __init__(self, branch_name='', bank_name='',address=''):
        self.branch_name = branch_name
        self.bank_name = bank_name
        self.address=address
        self.ifsc_code = random.randint(1500, 2500)
    def create_account(self, cust_name, dob, phone, email, acc_type, money,address):
        account = self._get_account_type(cust_name, dob, phone, email, acc_type, money, self.ifsc_code,address)
        Branch._customers.append(account)
        View.display_account_details(account) 
    # def get_customer_obj(self,cust_id):
    #     for i in Branch._customers:
    #         if i.cust_id==cust_id:
    #             return i 
    #     print("Invalid cust_id")
    #     return 

    def _get_account_type(self, name, dob, phone, email, acc_type, money, ifsc,address):
        if acc_type.lower() == "savings":
            return Savings(name, dob, phone, email, acc_type, money, ifsc,address)
        elif acc_type.lower() == "current":
            return Current(name, dob, phone, email, acc_type, money, ifsc,address)
        elif acc_type.lower() == "loan":
            return LoanAccount(name, dob, phone, email, acc_type, money, ifsc,address)
        else:
            raise ValueError("Invalid")

    def save_branch(self):
        add_details([str(0), self.branch_name, self.bank_name, str(self.ifsc_code), self.address], 'branch')
