from abc import ABC 
from table_logic import add_customer_details

class account(ABC):
    def __init__(self,cust_name,dob,phone,email,type):
        self.cust_name=cust_name
        self.dob=dob
        self.phone=phone
        self.email=email
        self.type=type
        self.cust_ifsc=123

class branch:
    def __init__(self,branch_name,name,dob,phone,email,type,bank_name):
        self.branch_name=branch_name
        self.bank_name=bank_name
        self.create_account(name,dob,phone,email,type)
    def create_account(self,name,dob,phone,email,type):
        customer=account(name,dob,phone,email,type)
        add_customer_details([customer.cust_name,customer.dob,customer.phone,customer.email,customer.type])


class bank:
    def __init__(self,branch_name,name,dob,phone,email,type,bank_name):
        self.banke_name=bank_name
        branch(branch_name,name,dob,phone,email,type,bank_name)

class current_Account:
    def withdrow():
        pass
    def creadit():
        pass 
    def checkbanlance():
        pass
class saving_Account:
    def withdrow():
        pass
    def creadit():
        pass 
    def checkbanlance():
        pass

class customer:
    def create_bank_account(self,branch_name,name,dob,phone,email,type,bank_name):
        obj=bank(branch_name,name,dob,phone,email,type,bank_name)
    def withdrow(phone,type): 
        if type=='savings':
            v=saving_Account().withdrow(acc_no)
            if v==1:
                print("Money Has been Debited")
            elif v==2:
                print("server bussy")
            elif v==3:
                print(" invalid money")
            else:
                print("Error!")
        else:
            v=current_Account().withdrow(phone)
            if v==1:
                print("Money Has been Debited")
            elif v==2:
                print("server bussy")
            elif v==3:
                print(" invalid money")
            else:
                print("Error!")

        


obj=customer()
obj.create_bank_account("madurai",'muthu raja','25/10/2004','9344058085','muthuraja05980@gmail.com',"savings","iob")
# bank1=bank("muthu's bank")