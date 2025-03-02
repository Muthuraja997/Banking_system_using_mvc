
# from database_setting import connection
from models.customer_dao import customer_to_table_dao
def add_details(record_list,table_name):
        length=len(record_list)
        query = "INSERT INTO " +table_name+" VALUES ("
        for i in range(length-1):
            query += '\'' +record_list[i] + '\','  
        query+='\''+str(record_list[-1])+'\'' 
        query += ");"
        print(query)
        if customer_to_table_dao().insert_data(query):
             print("success")
        else:
             print("ERROR!")

             
def generate_get_amount_query(acc_no,table_name):
        query="SELECT ACC_TYPE, BALANCE FROM "+table_name+" WHERE ACC_NO= "+str(acc_no)+";"
        v=customer_to_table_dao().get_balance(query)
        if v==0:
            print("ERROR")
        else:
            v=list(v)
            return v 
def generate_put_amount_query(acc_no,money,table_name):
    query="UPDATE "+table_name+" SET BALANCE =" +str(money)+" WHERE ACC_NO ="+str(acc_no)+";"
    respose=customer_to_table_dao().put_money(query)
    if respose==0:
         print("ERROR")
    else:
         print("seccess")
        
# generate_get_amount_query(1095,'customers')
            # cursor.execute(query) 
            # connection.commit()
    #         print("success fully inserted")       
    #     else:
    #         print("there is no permision to access")
    # except Exception as e:
# def check_account(cust_id,amount):
#       pass
    
# def branch(list_branch):
#       try:
#         if connection.is_connected():
#             cursor=connection.cursor()
#       except:
#           print("ERROR!")