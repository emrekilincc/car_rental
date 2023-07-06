from user_database import Databases
 
from car_database import Car

class User_Login(Databases):
    def __init__(self):
        self.login_user()
    
    
    def register_user(self):
        Databases(self.username, self.password).user_register()
        print("Kayıt Başarılı")
        
        self.user_choise()
   
    def login_user(self):
        self.username= input("username: ")
        self.password= input("password: ")
        if  Databases(self.username, self.password).user_login()== True:
            print("Şifre doğru, Giriş yapılıyor.")
            self.user_choise()
            
        elif Databases(self.username, self.password).user_login()== False:
            x= input("Üyelik mevcut değil, kayıt olmak ister misiniz? (E/H)")
            if x == "E":
                self.register_user()
                
            elif x== "H":
                pass
            
            else:
                print("Hatalı tuşlama") 
                
    def user_choise(self):
        while True:
            
            to_can= int(input("Yapmak istediğiniz işlemi seçiniz\n1.Arabaları listele\n2.Araba Seç,\nSeçim: "))
            if to_can == 1:
                Car().list_all_data()
                # city = input("şehir: ")
                # branch = input("şube: ")
                
                # Car().list_car(city, branch)
                
            elif to_can ==2:
                Car().list_all_data()
                city= input("şehir: ")
                branch= input("şube: ")
                model= input("model: ")
                
                Car().rent_car(city, branch, model)

            
            else: #Hata döndürmeli vs.
                break
#User_Login().login_user()