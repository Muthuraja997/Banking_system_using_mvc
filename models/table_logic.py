
from database_setting import connection
def add_customer_details(cust_list):
    try:
        if connection.is_connected():
            cursor=connection.cursor()
            query = "INSERT INTO customers (cust_name, DOB, phone, email, type) VALUES ("
            query += '\'' + cust_list[0] + '\','  
            query += '\'' + cust_list[1] + '\','  
            query += '\'' + cust_list[2] + '\','  
            query += '\'' + cust_list[3] + '\','  
            query += '\'' + cust_list[4] + '\''   
            query += ");"
            cursor.execute(query) 
            connection.commit()
            print("success fully inserted")       
            
        else:
            print("there is no permision to access")
    except Exception as e:
      
        print(f"An error occurred: {e}")