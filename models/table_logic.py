
from database_setting import connection
def add_details(record_list,table_name,length):
    try:
        if connection.is_connected():
            cursor=connection.cursor()
            query = "INSERT INTO " +table_name+" VALUES ("
            for i in range(length-1):
                query += '\'' + record_list[i] + '\','  
            query+='\''+str(record_list[-1])+'\'' 
            query += ");"
            cursor.execute(query) 
            connection.commit()
            print("success fully inserted")       
            
        else:
            print("there is no permision to access")
    except Exception as e:
      
        print(f"An error occurred: {e}")
def branch(list_branch):
      try:
        if connection.is_connected():
            cursor=connection.cursor()
      except:
          print("ERROR!")