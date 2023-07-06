import sqlite3
class Databases:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        
        self.connect_user_database()
        
        
    def connect_user_database(self):
        self.database_connect=sqlite3.connect("user_infos.db")
        self.imlec = self.database_connect.cursor()
        self.imlec.execute("""CREATE TABLE IF NOT EXISTS users(username TEXT ,password TEXT)""")

    def user_register(self):
        check_user_pass= self.imlec.execute(f"""SELECT username and password FROM users WHERE username = "{self.username}" and password = "{self.password}" """).fetchall()

        if len(check_user_pass) == 0:
            self.imlec.execute(f"""INSERT INTO users VALUES("{self.username}","{self.password}" )""")
            self.database_connect.commit()
        self.database_connect.close()

    def user_delete(self):      
        self.check_user_pass= self.imlec.execute(f"""SELECT username and password FROM users WHERE username = "{self.username}" and password = "{self.password}" """).fetchall()

        if self.check_user_pass != None:
            self.imlec.execute(f"""DELETE FROM users WHERE username="{self.username}" and password="{self.password}" """)
            self.database_connect.commit()
        self.database_connect.close()
                
    def user_login(self):

        self.connect_user_database()
        db_password = self.imlec.execute(f"""SELECT password FROM users WHERE username= "{self.username}" """).fetchall()      
        if len(db_password) == 1:

            return True
        else:
            return False



#Databases("user", "123").user_register()   
#Databases("user", "123").user_login()   
#Databases("user", "123").user_delete()   
