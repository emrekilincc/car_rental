from admin_database import Admin_Database
from car_database import Car

class Admin_Login(Admin_Database, Car):
    def __init__(self):
        #Admin.__init__(self, username, password)
        #Car.__init__(self, _city, _branch, _car_model, _car_count, _rent)
        pass
    
    def login_ad(self):

        username = input("Kullanıcı adı: ")
        password = input("\npassword: ")
    
        if  Admin_Database(username, password).admin_login() == True:
            print("Şifre doğru, Giriş yapılıyor.")
            self.choice_ad()
        else:
            print("Hatalı şifre")
            
    def info_cities(self):
        self.city= input("\nİşlem yapmak istediğiniz şehrin adını giriniz: ")
        self.branch= input("\nİşlem yapmak istediğiniz şubenin adını giriniz: ")
    
    def choice_ad(self):
        while True:
            to_can=int(input(["Yapmak istediğiniz işlemi seçiniz",
                        "1.Ekleme,",
                        "2.Çıkarma",
                        "3.Mevcut arabaları listleme",
                        "Çıkmak için '4' e basın"]))

            if to_can == 1:
                self.info_cities()
                which= int(input("1.Şehir,Şube, 2.Model, 3.araç sayısı?"))
                if which ==1:
                    Car().add_city_branch(self.city, self.branch)

                elif which == 2:
                    self.model= input("model: ")
                    self.car_count= input("car count: ")
                    Car().add_model(self.city, self.branch, self.model, self.car_count)
                
                elif which == 3:
                    self.model= input("model: ")
                    new_count= int(input("new count: "))
                    Car().update_count(self.city, self.branch, self.model, new_count)
                    
                # self.contin = input("Eklemeye devam edecek misiniz? (E/H)") 
                # if self.contin == "E":
                #     self.choise_ad()
                
            elif to_can == 2:
                which= input("1.Şehir, 2.Şube, 3.Model, 4.tüm veriler?")
                car_class=Car()
                
                if which == "1":
                    city= input("\nİşlem yapmak istediğiniz şehrin adını giriniz: ")
                    car_class.delete_city(city)
                
                elif which == "2":
                    city= input("\nİşlem yapmak istediğiniz şehrin adını giriniz: ")
                    branch= input("\nİşlem yapmak istediğiniz şubaenin adını giriniz: ")
                    car_class.delete_branch(city, branch)
                
                elif which == "3":
                    city= input("\nİşlem yapmak istediğiniz şehrin adını giriniz: ")
                    branch= input("\nİşlem yapmak istediğiniz şubenin adını giriniz: ")
                    model= input("\nİşlem yapmak istediğiniz modelin adını giriniz: ")
                    car_class.delete_model(city, branch, model)
                
                elif which == "4":
                    car_class.dell_all_data()
                
                
            elif to_can == 3:
                Car().list_all_data()
            
            
            elif to_can == 4:
                break


            else:
                raise AttributeError("Yanlış seçim")


#Admin_Login().login_ad()