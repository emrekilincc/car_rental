from admin_login import Admin_Login
from branch_login import Branch_Login
from user_login import User_Login

login = int(input("Admin için 1'e,\nŞube için 2'ye,\nKullanıcı için 3'e,\nÇıkış için 4'e basınız\nSeçim: "))


if login ==1:
    Admin_Login().login_ad()  #admine ait işlemleri yapmak için bunu çalıştır ##############3 Şube silerken branch_infos.daki veriyi de siliyor.!!!
        
elif login==2:
    Branch_Login().login_branch()

elif login==3:
    User_Login()
    