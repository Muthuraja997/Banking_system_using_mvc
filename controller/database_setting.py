import mysql.connector
try:
    connection=mysql.connector.connect(
        host='localhost',
        database='banking_system',
        user='root',
        password="Muthu93#"
    )
    # if connection.is_connected():
    #     cursor=connection.cursor()
    #     query=input("enter query to create:")
    #     cursor.execute(query)
    #     print("successed")
    print("databse successfully connected")
except:
    print("Connection not permited")
    exit(0)
# def create_table(self):
            
# obj=settings()
# obj.create_table()
# def add_customer_details(cust_obj):