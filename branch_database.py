import sqlite3
from car_database import Car

class Branch_Database():
    def __init__(self) -> None:

        self.connect_car_database()
        self.connect_branch_database()

    def connect_car_database(self):
        self.database_connect_car=sqlite3.connect("car_infos.db")
        self.imlec_car = self.database_connect_car.cursor()
        self.imlec_car.execute("""CREATE TABLE IF NOT EXISTS car(city TEXT, branch TEXT ,model TEXT, count INTEGER)""")
        
    def connect_branch_database(self):
        self.database_connect_branch=sqlite3.connect("branch_info.db")
        self.imlec_branch = self.database_connect_branch.cursor()
        self.imlec_branch.execute("""CREATE TABLE IF NOT EXISTS branchs(city TEXT, branchname TEXT ,password TEXT)""")

    '''     
    def register_branch(self):  #sadece admin eklesin
        branch_in_car = self.imlec_car.execute(f""" SELECT branch FROM car WHERE city= "{self.city}" """).fetchall()
        branch_in_branch = self.imlec_branch.execute(f""" SELECT branchname FROM branchs WHERE password= "{self.password}" """).fetchall()
        print(branch_in_branch)
        print(branch_in_car)
        
        branch_branch= []
        branch_car =[]
        
        for _ in branch_in_branch:
            branch_branch.append(_)
        
        for _ in branch_in_branch:    
            branch_car.append(_)
        
        
        if branch_in_car== None and branch_in_branch ==None:#iki database de boşsa iki db ye de ekle
            car_model= input("car model: ")
            car_count= int(input("car count:"))
            Car().add_city_branch(self.city, self.branchname, car_model, car_count)#car_infos db sine ekler
            print(self.city, self.branchname, self.password)
            self.imlec_branch.execute(f"""INSERT INTO branchs VALUES("{self.city}", "{self.branchname}", "{self.password}") """)#branch_infos db sine ekler
            self.database_connect_branch.commit()
        elif branch_in_car == branch_in_branch:
            print("Şube mevcut")
        

        if branch_in_branch!= None or branch_in_car!= None: 

            if branch_in_car[0] not in branch_in_branch[0]:
                self.imlec_branch.execute(f"""INSERT INTO branchs VALUES("{self.city}", "{self.branchname}","{self.password}" )""")

            elif branch_in_branch[0] not in branch_in_car[0]:
                car_model= input("car model: ")
                car_count= int(input("car count:"))
                Car().add_city_branch(self.city, self.branchname, car_model, car_count)
###########################################################################################
        if branch_password== None:
            #elf.imlec.execute(f"""INSERT INTO branch VALUES("{self.city}", "{self.branchname}","{self.password}" )""")
            print("Kayıt Başarılı")
            self.database_connect.commit()
            self.database_connect.close()
        else:
            print("Şube mevcut")
            self.database_connect.close()
'''

    def login_branch(self, branchname, password, city):
        self.city = city
        self.branchname = branchname
        self.password = password
        
        login_branch = self.imlec_branch.execute(f"""SELECT password FROM branchs WHERE branchname= "{self.branchname}" and city="{self.city}" """).fetchone()
        
        if login_branch == None:
            print("kullanıcı adı veya şifre yanlış")
            return False
        
        elif login_branch[0] == self.password:
            return True

    '''      
    def delete_branch(self):    #sadece adminin silme yetkisi olsun 
        branch_password = self.imlec_branch.execute(f"SELECT password FROM branchs WHERE username= '{self.branchname}' and city= '{self.city}' ").fetchone()
        if branch_password != None:
            self.imlec_branch.execute(f"""DELETE FROM branchs WHERE username="{self.branchname}" and password="{self.password}" """)
            print("Şube Silindi")
            self.database_connect_branch.commit()
            self.database_connect_branch.close()
        else:
            print("Yönetici mevcut değil")
    '''
    
    def add_model(self, city, branchname, model, car_count):
        self.city = city
        self.branchname=branchname
        self.car_count= car_count
        self.model = model
        Car().add_model(self.city, self.branchname, self.model, self.car_count)


    def del_model(self,city, branchname, model):
        self.city = city
        self.branchname = branchname
        self.model=model
        
        Car().delete_model(self.city, self.branchname, self.model)
        

    def list_models(self, city, branchname):
        self.city=city
        self.branchname=branchname
        models= self.imlec_car.execute(f"""SELECT model, count FROM car WHERE city= "{self.city}" and branch= "{self.branchname}" """).fetchall()
        
        if len(models) == 0:
            print("Mevcut değil")
        
        else: 
            current_model=[]
            current_count=[]
            for _ in models:
                current_model.append(_[0])
                current_count.append(_[1])
        
    
#Branch_Database("Dogus OTO", "dogus", "İstanbul").register_branch()


#Branch_Database().del_model("İstanbul", "Dogus OTO", "Audi")

#Branch_Database().list_models("İstanbul", "Dogus OTO")