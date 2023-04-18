from Test.test1 import Folder
import os 




def fun_mov():
    print('''

   --------- JETFLIX ---------

    1) --> Profile 
    2) --> Find Movies
    3) --> Find Using Description 
    4) --> Home

 
    
    ''')

    while True:
        Choice = int(input(" : -> "))

        if Choice == 1:
            Home=Folder.Profile()
            break

        elif Choice == 2:
            Home=Folder.Find_Movies()
            break

        elif Choice == 3:
            Home=Folder.Find_Using_Description()
            break
        
        elif Choice == 4:
            Home=Folder.Home()
            break
        else:
            print("Invalid input. Please try again.:(")

def Mainapp():
    os.system('cls')
    print('''

    ---------------------------
    Movie Recomandation System
    --------- JETFLIX ---------

    1) --> Login 
    2) --> Registration 
    3) --> Home 
    4) --> Profile 
    5) --> Find Movies
    6) --> Find Using Description 
    7) --> Exit
 
    
    ''')

    while True:
        Choice = int(input(" : -> "))

        if Choice == 1:
            Login =Folder.Login()
            Folder.Home()
            break

        elif Choice == 2:
            Registration=Folder.Registration()
            Folder.Login()
            break

        elif Choice == 3:
            Home=Folder.Home()
            fun_mov()
            break

        elif Choice == 4:
            Profile=Folder.Profile()
            print(Profile)
            break

        elif Choice == 5:
            Find_Movies = Folder.Find_Movies()
            print(Find_Movies)
            break

        elif Choice == 6:
            Find_Using_Description = Folder.Find_Using_Description()
            print(Find_Using_Description)
            break

        elif Choice == 7:
            os.system('cls')
            print("\n \n \n  Thank you For Wisiting..: ) \n \n \n ")
            os._exit(0)
        else:
            print("Invalid input. Please try again.:(")



Mainapp()

