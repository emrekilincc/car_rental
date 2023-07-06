import sqlite3
class Admin_Database():
    def __init__(self, username, password):
        """ 

        Args:
            username (_type_): _description_
            password (_type_): _description_
        """
        self.username= username
        self.password= password
        
        self.connect_admin_database()

    def connect_admin_database(self):
        self.database_connect=sqlite3.connect("admin_info.db")
        self.imlec = self.database_connect.cursor()
        self.imlec.execute("""CREATE TABLE IF NOT EXISTS admin(username TEXT ,password TEXT)""")
        
    
    def admin_register(self):
        admin_password = self.imlec.execute(f""" SELECT password FROM admin WHERE username= "{self.username}" """).fetchone()
        if admin_password== None:
            self.imlec.execute(f"""INSERT INTO admin VALUES("{self.username}","{self.password}" )""")
            print("Kayıt Başarılı")
            self.database_connect.commit()
            self.database_connect.close()
        else:
            print("Yönetici mevcut")
            self.database_connect.close()
    

    def admin_delete(self):    
        admin_password = self.imlec.execute(f"SELECT password FROM admin WHERE username= '{self.username}' ").fetchone()
        if admin_password != None:
            self.imlec.execute(f"""DELETE FROM admin WHERE username="{self.username}" and password="{self.password}" """)
            print("Yönetici Silindi")
            self.database_connect.commit()
            self.database_connect.close()
        else:
            print("Yönetici mevcut değil")


    def admin_login(self):
        admin_log = self.imlec.execute(f"""SELECT password FROM admin WHERE username= "{self.username}" """).fetchone()
        
        if admin_log == None:
            print("kullanıcı adı veya şifre yanlış")
            return False
        
        elif admin_log[0] == self.password:
            return True

        else:
            print("Yanlış şifre")
            return False

#Admin_Database("admin", "admin").admin_register()
#Admin_Database("admin", "admin").admin_login()
#Admin_Database("admin", "admin").admin_delete()