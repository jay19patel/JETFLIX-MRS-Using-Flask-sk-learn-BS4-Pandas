
from Test.movies_data import Movies_data
    # 1) --> Login 
    # 2) --> Registration 
    # 3) --> Home 
    # 4) --> Profile 
    # 5) --> Find Movies
    # 6) --> Find Using Description 
    # 7) --> Exit
from pymongo import MongoClient
import os 

class Folder():
    login_user = []

    mydatabase = MongoClient('localhost',27017)
    folder =mydatabase["JetFlix_Consol"]
    db =folder['User_data']


    def Login():
        os.system('cls')
        print("---------- Login Page ----------")
        username = str(input("Eneter User Name : "))
        passwords = str(input("Eneter Passwords : "))
        userdata = Folder.db.find_one({"username":username})
        if passwords == userdata['password']:
            Folder.login_user.append(userdata['username'])
            print("Login Sucessfully") 
        print("Somthing Error")

    def Registration():
        print("---------- Registration Page ----------")
        name = str(input("Eneter  Name : "))
        username = str(input("Eneter User Name : "))
        password1 = str(input("Eneter Passwords : "))
        password2 = str(input("Eneter Passwords Agian : "))
        
        if password1 == password2:
            Folder.db.insert_one({"name":name,"username":username,"password":password1})
            print(" Registration Sucessfully ")
        else:
            print(" Something Wrong ")
    
    def Home():
        print("---------- Home Page ----------")
        if Folder.login_user:
            print(f'''
            ---------- Welcome to Jetflix ---------- 

            : Top 5 2023 Movies :           
            ''')
            Movie = Movies_data()
            n = 1
            for i in Movies_data.Best_movies():
                print(f"{n} :-> {i}")
                n=n+1
        else:
            print("Uer Are Not Login Login Plase :") 


               
    
    def Profile():
        print("---------- Profile Page ----------")
        return " Profile "
    
    def Find_Movies():
        print("---------- Find Movies Page ----------")
        return " Find_Movies "
    
    def Find_Using_Description():
        print("---------- Find Using Description Page ----------")
        return " Find_Using_Description "

    