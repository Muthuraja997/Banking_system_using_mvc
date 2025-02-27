
# from database_setting import connection
from customer_dao import customer_to_table_dao
def add_details(record_list,table_name,length):
    # try:
    #     if connection.is_connected():
    #         cursor=connection.cursor()
        query = "INSERT INTO " +table_name+" VALUES ("
        for i in range(length-1):
            query += '\'' + record_list[i] + '\','  
        query+='\''+str(record_list[-1])+'\'' 
        query += ");"
        if customer_to_table_dao().insert_data(query):
             print("success")
        else:
             print("ERROR!")
def generate_get_amount_query(cust_id,table_name):
        query="SELECT TYPE, CURRENT_BALANCE FROM "+table_name+" WHERE CUST_ID= "+str(cust_id)+";"
        v=customer_to_table_dao().get_balance(query)
        if v==0:
            print("ERROR")
        else:
            v=list(v)
            

generate_get_amount_query(1095,'customers')
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