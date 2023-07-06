import sqlite3
from car_database import Car 
from branch_database import Branch_Database

class Branch_Login:
    def __init__(self) -> None:
        pass

        #self.login_branch()
    '''
    def info_cities(self):
        self.city= input("\nİşlem yapmak istediğiniz şehrin adını giriniz: ")
        self.branch= input("\nİşlem yapmak istediğiniz şubenin adını giriniz: ")
    '''

    def login_branch(self):
        
        if Car().list_cities() == True:
            self.city= input("\nİşlem yapmak istediğiniz şehrin adını giriniz: ")
            
            Car().list_branchs(self.city)
            self.branch= input("\nİşlem yapmak istediğiniz şubenin adını giriniz: ")
            password= input("password: ")
            if Branch_Database().login_branch(self.branch, password, self.city) == True:
                print("Şifre doğru, Giriş yapılıyor.")
                self.choice_branch()
            else:
                print("Hatalı şifre")
        else:
            return False
            
    def choice_branch(self):
        while True:
            to_can=int(input("Yapmak istedğiniz işlemi seçiniz\n1.Araç ekleme,\n2.Araç çıkarma,\n3.Araçları Listeleme\n4.Çıkış\nSeçim: "))
            

            if to_can == 1:
                self.model= input("\nİşlem yapmak istediğiniz modelin adını giriniz: ")
                self.car_issue= input("\nİşlem yapmak istediğiniz arabanın sayısını giriniz: ")
           
                #car.infos databasedeki verileri alsın kontrol etsin yoksa eklesin varsa mevcut desin. eğer ekleme işlemi olursa hem kendi databasesine hemde car_infos.db ye eklesin
                #Car().add_city_branch(self.city, self.branch, self.model, self.car_issue)
                Branch_Database().add_model(self.city, self.branch, self.model, self.car_issue)
            
            elif to_can ==2:
                self.model= input("\nİşlem yapmak istediğiniz modelin adını giriniz: ")

                Branch_Database().del_model(self.city, self.branch, self.model)
                
            elif to_can == 3:

                Car().list_car(self.city, self.branch)  
                
            else:
                break
#Branch_Login().login_branch()