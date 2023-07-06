import sqlite3
class Car:
    def __init__(self):
        self.connect_car_database()
        self.connect_branch_database()
    
    def connect_branch_database(self):
        self.database_connect_branch=sqlite3.connect("branch_info.db")
        self.imlec_branch = self.database_connect_branch.cursor()
        self.imlec_branch.execute("""CREATE TABLE IF NOT EXISTS branchs(city TEXT, branchname TEXT ,password TEXT)""")
    
    def connect_car_database(self):
        self.database_connect=sqlite3.connect("car_infos.db")
        self.imlec = self.database_connect.cursor()
        self.imlec.execute("""CREATE TABLE IF NOT EXISTS car(city TEXT, branch TEXT ,model TEXT, count INTEGER)""")
    
    
    def add_city_branch(self, city, branch):
        self.connect_branch_database()
        self.city = city
        self.branch= branch
        
        password= input("password: ")
        
        branch_in_car = self.imlec.execute(f""" SELECT branch FROM car WHERE city= "{self.city}" """).fetchall()
        branch_in_branch = self.imlec_branch.execute(f""" SELECT branchname FROM branchs WHERE city= "{self.city}" """).fetchall()
        
        branch_branch= []
        branch_car =[]
        
        for _ in branch_in_branch:
            branch_branch.append(_)
        
        for _ in branch_in_car:    
            if len(branch_in_car)<1:
                branch_car.append(_)
        
        
        if len(branch_car)== 0 and len(branch_branch) ==0:#iki database de boşsa iki db ye de ekle
            car_model= input("car model: ")
            car_count= int(input("car count:"))
            
            self.imlec.execute(f"""INSERT INTO car VALUES("{self.city}", "{self.branch}", "{car_model}", "{car_count}") """) 
            self.database_connect.commit()
            #Car().add_city_branch(self.city, self.branchname, car_model, car_count)#car_infos db sine ekler
            self.imlec_branch.execute(f"""INSERT INTO branchs VALUES("{self.city}", "{self.branch}", "{password}") """)#branch_infos db sine ekler
            self.database_connect_branch.commit()
            

        elif branch_car == branch_branch:
            print("Şube mevcut")
            print(branch_branch, branch_car) 
        

        elif branch_in_branch!= None or branch_in_car!= None: 

            if len(branch_car)>=1 and len(branch_in_branch)== 0:
                self.imlec_branch.execute(f"""INSERT INTO branchs VALUES("{self.city}", "{self.branch}","{password}" )""")
                self.database_connect_branch.commit()

            elif len(branch_in_branch)>= 1 and len(branch_car)== 0:
                car_model= input("car model: ")
                car_count= int(input("car count:"))
                self.imlec.execute(f"""INSERT INTO car VALUES("{self.city}", "{self.branch}", "{car_model}", "{car_count}") """) 
                self.database_connect.commit()
        '''        
        for x in branch_branch:
            for y in branch_car:
                print(y)
            if self.branch not in x and self.branch not in y:
                car_model= input("car model: ")
                car_count= int(input("car count:"))
                    
                self.imlec.execute(f"""INSERT INTO car VALUES("{self.city}", "{self.branch}", "{car_model}", "{car_count}") """) 

                self.imlec_branch.execute(f"""INSERT INTO branchs VALUES("{self.city}", "{self.branch}", "{password}") """)#branch_infos db sine ekler
                self.database_connect.commit()
                self.database_connect_branch.commit()
            
            self.database_connect.close()
            
            self.database_connect_branch.close()
        ''' 
        
        
        
        '''
        check_city_branch= self.imlec.execute(f"""SELECT city, branch FROM car where city = "{self.city}" and branch= "{self.branch}" and model="{self.model}" """).fetchall()
        cities= []
        branchs=[]
        for _ in check_city_branch:
            cities.append(_[0])
            branchs.append(_[1])
            
        if self.city not in cities:
            self.imlec.execute(f"""INSERT INTO car VALUES("{self.city}", "{self.branch}", "{self.model}", "{self.car_count}") """)
        
        elif self.city in cities and self.branch not in branchs:
            self.imlec.execute(f"""INSERT INTO car VALUES("{self.city}", "{self.branch}", "{self.model}", "{self.car_count}") """)
        
        else:
            print("Şehir mevcut")
                    
        self.database_connect.commit()
        self.database_connect.close()   
            '''

    def add_model(self, city, branch, model, car_count):   
        self.city = city
        self.branch= branch
        self.model = model
        self.car_count = car_count
        self.connect_car_database()
        check_model = self.imlec.execute(f"""SELECT branch, model FROM car WHERE city= ("{self.city}") """).fetchall()
        list_branch = []
        list_model =[]
        datas= {}
        for _ in check_model:
            datas[_[0]] = _[1]
            
        if self.branch in list_branch:
            if self.model not in datas:
                self.imlec.execute(f"""INSERT INTO car VALUES ("{self.city}", "{self.branch}", "{self.model}", "{self.car_count}") """)
            
            else:
                print(f"{self.model} model araç {self.branch} şubesinde mevcut")
            
        else:
            self.imlec.execute(f"""INSERT INTO car VALUES ("{self.city}", "{self.branch}", "{self.model}", "{self.car_count}") """)
            #print("Şube ekleme İşlemi başarılı")
            
        self.database_connect.commit()
        self.database_connect.close()   
    
    '''   
    def list_current_data(self):
        self.connect_car_database()
        
        data = self.imlec.execute(f"""SELECT city FROM car """).fetchall()
   '''     
        
    def list_car(self, city, branch):
        self.city=city
        self.branch= branch      

        #self.connect_car_database()
        #self.count_cars()
        #self.connect_car_database()
        
        cars = self.imlec.execute(f"""SELECT model, count FROM car WHERE city= "{self.city}" and branch= "{self.branch}" """).fetchall()
        if cars != None:
            model= []
            car_count = []
            for _ in cars:
                model.append(_[0])
                car_count.append(_[1])
        
                print(_[0], _[1])

            '''   
            if self.model in model:
                if self.rent == True:
                    print(f"{self.city}'daki {self.branch}'da {self.model} arabasından {self.new_count} tane mevcut") 
                else :
                    print(f"{self.city}'daki {self.branch}'da {self.model} arabasından {self.current_count} tane mevcut") 
                
            else:
                print(f"{self.city}'daki {self.branch}'da {self.model} arac mevcut degil")
            
            self.database_connect.close()
    ''' 
        elif cars == None:
            print("Mevcut değil")
        
        else:
            print("Girilen bilgiler yanlış")    
            
    def list_all_data(self):
        self.connect_car_database()
        
        city=[]
        branch=[]
        model= []
        car_issue= []
        data = self.imlec.execute(f"""SELECT * FROM car """).fetchall()
        if data != None:
            for x in data:
                count = 0
                for _ in x:
                    if count == 0:
                        city.append(_)
                        count+=1
                    elif count == 1:
                        branch.append(_)
                        count+=1
                    elif count == 2:
                        model.append(_)
                        count+=1
                    elif count == 3:
                        count+=1
                        car_issue.append(_)
            count = 0

            while count <len(city):
                print(city[count], branch[count], model[count], car_issue[count])
                count +=1
            
        else:
            print("Database boş")    

    def delete_city(self, city):
        self.city = city
        
        data_check = self.imlec.execute(f"""SELECT city FROM car WHERE city= '{self.city}' """).fetchall()
        data_check_branch= self.imlec_branch.execute(f"""SELECT city FROM branchs WHERE city= '{self.city}'  """).fetchall()
        if data_check == None and data_check_branch== None:
            print("Şehir mevcut değil")
        elif len(data_check) >= 1 and len(data_check_branch) >= 1:
            self.imlec.execute(f"""DELETE FROM car WHERE city= '{self.city}' """)
            self.imlec_branch.execute(f"""DELETE FROM branchs WHERE city= '{self.city}' """)
            print("Data silindi")
        
        elif len(data_check)==0 or len(data_check_branch)== 0:
            if len(data_check) == 0:
                self.imlec_branch.execute(f"""DELETE FROM branchs WHERE city= '{self.city}' """)
            elif len(data_check_branch)== 1:
                self.imlec.execute(f"""DELETE FROM car WHERE city= '{self.city}' """)
                
        self.database_connect.commit()
        self.database_connect_branch.commit()
        self.database_connect_branch.close()
        self.database_connect.close()

    
    def delete_branch(self, city, branch):
        self.city = city
        self.branch = branch
    
        password= input("password: ")

        data_check = self.imlec.execute(f"""SELECT branch FROM car WHERE city= "{self.city}" and branch= '{self.branch}' """).fetchall()
        data_check_branch= self.imlec_branch.execute(f"""SELECT branchname FROM branchs WHERE city= "{self.city}" and password= '{password}'  """).fetchall()
        
        if data_check == None and data_check_branch== None:
            print("Şehir mevcut değil")
            
        elif len(data_check) >= 1 and len(data_check_branch) >= 1:
            self.imlec.execute(f"""DELETE FROM car WHERE branch= '{self.branch}' """)
            self.imlec_branch.execute(f"""DELETE FROM branchs WHERE branchname= '{self.branch}' """)
            print("Data silindi")
        
        elif len(data_check)==0 or len(data_check_branch)== 0:
            if len(data_check) == 0:
                self.imlec_branch.execute(f"""DELETE FROM branchs WHERE branchname= '{self.branch}' """)
            elif len(data_check_branch)== 0:
                self.imlec.execute(f"""DELETE FROM car WHERE branch= '{self.branch}' """)
              
        self.database_connect.commit()
        self.database_connect_branch.commit()
        self.database_connect_branch.close()
        self.database_connect.close()  
        '''
        data_check= self.imlec.execute(f"""SELECT branch FROM car WHERE branch= '{self.branch}' """).fetchall()
        if data_check == None:
            print("Şube mevcut değil")
        elif data_check[0] == self.branch:
            self.imlec.execute(f"""DELETE FROM car WHERE branch= '{self.branch}' and city= "{self.city}" """)
            self.database_connect.commit()
            self.database_connect.close()
            print("Şube silindi")
      '''
        
    def delete_model(self, city, branch, model):
        self.city = city
        self.branch = branch
        self.model = model
        
        data_check = self.imlec.execute(f"""SELECT model FROM car WHERE city= "{self.city}" and branch= "{self.branch}" """).fetchall()
        if data_check == None:
            print("Model mevcut değil")
        
        elif len(data_check) >= 1:
            self.imlec.execute(f"""DELETE FROM car WHERE branch= "{self.branch}" and model= "{self.model}" """)
            '''
            sadece car info dbsindeki veri silinmeli
            #self.imlec_branch.execute(f"""DELETE FROM branchs WHERE branchname= '{self.branch}' and city= "{self.city}" """)
            
            #self.database_connect_branch.commit()
            #self.database_connect_branch.close()
            '''
            self.database_connect.commit()
            self.database_connect.close()
            print("model silindi")   
 
    
    def count_cars(self, city, branch, model):
        self.city = city
        self.branch= branch
        self.model = model
        
        self.data_check = self.imlec.execute(f"""SELECT count FROM car WHERE city= "{self.city}"  and branch= "{self.branch}" and model= "{self.model}" """).fetchone()
        
        if self.data_check == None:
            print("Mevcut değil")

        if self.rent == True:
        
            self.current_count = self.data_check[0]
            if self.current_count <= 1:
                print(f"{self.model} araç mevcut değil")
            else:    
                self.new_count = self.current_count -1
                self.update_db()    
                self.connect_car_database()
                self.database_connect.commit()
        
        self.connect_car_database()
        self.database_connect.close()
        
        
    def update_count(self, city, branch, model, new_count):
            self.city = city
            self.branch= branch
            self.model = model
            self.new_count =new_count
            self.imlec.execute(f"""UPDATE car SET count= "{self.new_count}" WHERE city = "{self.city}" and branch= "{self.branch}" and model = "{self.model}" """)
            self.database_connect.commit()
            self.database_connect.close()
    
    def update_db(self, city, branch, model, rent):
        self.rent= rent
        if self.rent == True:
            
            self.city = city
            self.branch= branch
            self.model = model
            

            count= self.imlec.execute(f"""SELECT count FROM car WHERE city = "{self.city}" and branch= "{self.branch}" and model = "{self.model}" """).fetchone()
            if count[0]>0:
                new_count = count[0] -1
                self.imlec.execute(f"""UPDATE car SET count= "{new_count}" WHERE city = "{self.city}" and branch= "{self.branch}" and model = "{self.model}" """)
                self.database_connect.commit()
                self.database_connect.close()
                print("kiralama işlemi başarılı")
            else: 
                print("Araç tükenmiştir")
    def dell_all_data(self):
        self.imlec.execute("DELETE FROM car")
        self.imlec_branch.execute("DELETE FROM branchs")
        
        self.database_connect_branch.commit()
        self.database_connect.commit()
        
        self.database_connect_branch.close()
        self.database_connect.close()


    def rent_car(self, city, branch, model):
        self.city = city
        self.branch = branch
        self.model= model
        
        count = self.imlec.execute(f"""SELECT count FROM car WHERE city="{self.city}" and branch="{self.branch}" and model= "{self.model}" """).fetchall()
        if len(count) > 0:
            rent = True
            
            self.update_db(self.city, self.branch, self.model, rent)
        
        else: 
            rent= False
            return rent
        #database bak. araba mevcutsa return true kullanıcıdan onay aldıktan sonra
        #count carsa modeldeki araba 1 eksilir database güncellenir
         
         
    def list_cities(self):
        city= self.imlec.execute("""SELECT city FROM car """).fetchall()
        if len(city) ==0:
            print("Şube mevcut değil")
            return False
        else :
            cities=[]
            for _ in city:
                if _[0] not in cities:
                    cities.append(_[0])
            print(cities)
            return True

    def list_branchs(self, city):
        self.city = city
        branchs= self.imlec.execute(f"""SELECT branch FROM car WHERE city= "{self.city}" """).fetchall()
        if len(branchs) == 0:
            print("Mevcut değil")

        else:
            current_branchs=[]
            for _ in branchs:
                current_branchs.append(_[0])
            print(current_branchs)
            

""""
print(cars)
to_str= functools.reduce(operator.add, (cars))
for _ in to_str:
    print(_)
    car_list.append(_)
print(to_str)
print(car_list)
"""
        
#Car("Bursa", "Dogus OTO", "BMW", 5, False).delete_city()
#Car("Bursa", "Bekir OTO", "Fiat", 2, False).list_all_data()
#car=Car()
#car.list_all_data
"""  
list1 = [("İstanbul", "Dogus OTO", "BMW", 5), ("İstanbul", "Dogus OTO", "AUDI", 5), ("İstanbul", "Kamil OTO", "AUDI", 5), ("İstanbul", "Kamil OTO", "BMW", 5), ("Bursa", "Dogus OTO", "AUDI", 5)]
list2 = [("İstanbul", "Dogus OTO", "BMW", 5), ("İstanbul", "Dogus OTO", "AUDI", 5), ("İstanbul", "Kamil OTO", "AUDI", 5), ("İstanbul", "Kamil OTO", "BMW", 5), ("Bursa", "Kamil OTO", "AUDI", 5)]
Car("İstanbul", "Dogus OTO", "BMW", 5, True).dell_all_datas()

for _ in list1:
    Car(_[0], _[1], _[2], _[3], False).add_city_branch()
    Car(_[0], _[1], _[2], _[3], True).add_model()
    # Car(_[0], _[1], _[2], _[3], True).list_car()
    # Car(_[0], _[1], _[2], _[3], True).list_car()
    """   
"""for _ in list2:
    #Car(_[0], _[1], _[2], _[3], True).delete_city()
    #Car(_[0], _[1], _[2], _[3], True).delete_branch()
    Car(_[0], _[1], _[2], _[3], True).delete_model()
"""



#Car().add_city_branch("İstanbul", "Dogus OTO", "BMW", 5)
# Car("İstanbul", "Dogus OTO", "AUDI", 5).add_branch_model()
# Car("İstanbul", "Kamil OTO", "AUDI", 5).add_branch_model()
# Car("İstanbul", "Kamil OTO", "AUDI", 5).add_branch_model()
# Car("İstanbul", "Kamil OTO", "BMW", 5).add_branch_model()
# Car("Eskişehit", "Dogus OTO", "BMW", 5).add_branch_model()
# Car("Bursa", "Dogus OTO", "AUDI", 5).add_city()


# #Car("İstanbul", "Dogus OTO", "BMW", 5).list_car()
#Car("Bursa", "Dogus OTO", "BMW", 5,False).delete_city()
# #Car("İstanbul", "Kamil OTO", "AUDI", 5).delete_branch()
# # Car("İstanbul", "Dogus OTO", "AUDI", 5).delete_branch()
# # Car("İstanbul", "Dogus OTO", "BMW", 5).delete_model()
# # Car("İstanbul", "Kamil OTO", "AUDI", 5).delete_model()
# #Car("İstanbul", "Kamil OTO", "BMW", 5).count_cars(True)
# Car("İstanbul", "Kamil OTO", "BMW", 5).list_car()
