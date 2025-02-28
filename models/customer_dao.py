from database_setting import connection
class customer_to_table_dao:
    def insert_data(self,query):
        try:
            if connection.is_connected():
                cursor=connection.cursor()
                cursor.execute(query) 
                connection.commit()
                return True 
            else:
                return False
        except Exception as e:
            print("ERROR MSG IS :",e)
            return False 
    def get_balance(self,query):
        try:
            if connection.is_connected():
                cursor=connection.cursor()
                cursor.execute(query)
                responce=cursor.fetchone()
                if responce:
                    return responce
        except Exception as e:
            print("ERROR! :",e)
            return 0
class transaction_dao:
    def debit(amount):
        pass


            