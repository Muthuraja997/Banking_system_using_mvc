from abc import ABC,abstractmethod
from table_logic import add_details
import random
class account(ABC):
    val=random.randint(999,1500)
    ifsc=random.randint(1500,2500)
    
    def __init__(self,cust_name,dob,phone,email,type,money):
        self.cust_name=cust_name
        self.dob=dob
        self.phone=phone
        self.email=email
        self.type=type
        self.cust_ifsc=account.ifsc
        self.cust_id=account.val
        self.money=money
class savings():
    pass 
class current():
    pass 
class loan_account():
    pass



class branch:
    def __init__(self,branch_name,name,dob,phone,email,type,bank_name,money):
        self.branch_name=branch_name
        self.bank_name=bank_name
        self.ifsc=self.create_account(name,dob,phone,email,type,money,)
        add_details([str(0),self.branch_name,self.bank_name,str(self.ifsc),'address'],'branch',5)
    def create_account(self,name,dob,phone,email,type,money):
        customer=account(name,dob,phone,email,type,money)
        add_details([customer.cust_name,customer.dob,customer.phone,customer.email,customer.type,str(customer.cust_id),str(customer.cust_ifsc),customer.money],'customers',8)
        return customer.ifsc


class bank:
    def __init__(self,branch_name,name,dob,phone,email,type,bank_name,money):
        self.banke_name=bank_name
        self.branch_name=branch_name
        branch(branch_name,name,dob,phone,email,type,bank_name,money)

# class current_Account:
#     def withdrow():
#         pass
#     def creadit():
#         pass 
#     def checkbanlance():
#         pass
# class saving_Account:
#     def withdrow():
#         pass
#     def creadit():
#         pass 
#     def checkbanlance():
#         pass

class customer:
    def create_bank_account(self,branch_name,name,dob,phone,email,type,bank_name,money):
        obj=bank(branch_name,name,dob,phone,email,type,bank_name,money)
    def withdrow(phone,type): 
        pass
        


obj=customer()
obj.create_bank_account("maduraii",'muthu raja','25/10/2004','9344058085','muthuraja05980@gmail.com',"savingss","iob",500)
# bank1=bank("muthu's bank")