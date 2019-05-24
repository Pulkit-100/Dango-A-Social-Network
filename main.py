from Register import register,login
from Searching_BFS import search
from Recommendations_backtracking import recommendations
from Ascii_art import title
from update_file import update
import os
import msvcrt as m
def wait():
    print("\nEnter to continue .... ")
    m.getch()

while True:
    os.system('cls')
    title()
    print("\n\n")
    print("1. REGISTER ")
    print("2. LOGIN ")
    print("3. Exit \n ")
    ch=input("Enter your choice ")
    os.system('cls')
    pk=None
    if ch=="1":
        register()
        continue
        
    elif ch=="2":
        pk=login()
        #print(pk)
        while pk:
            os.system('cls')
            pk.display_details()
            print("\n\n")
            print("1. Search a Friend ")
            print("2. Recomendations ")
            print("3. Followers ")
            print("4. Following ")
            print("5. Logout \n")
            chh=input("Enter your choice ")
            if chh=="1":
                while True:
                    os.system('cls')
                    print("\n\n")
                    print("1. Search by Name or Number ")
                    print("2. Go back \n")
                    chhh=input("Enter your choice ")
                    if chhh=="1":
                        name=   input("Enter Name or Number to be searched     - ")
                        search(name,pk)
                    elif chhh=="2":
                        break
                    else:
                        print("Wrong Input \n\n")

            elif chh=="2":
                os.system('cls')
                recommendations(pk)

            elif chh=="3":
                os.system('cls')
                pk.display_followers()
                
            elif chh=="4":
                os.system('cls')
                pk.display_following()
                
            elif chh=="5":
                os.system('cls')
                update(pk)
                print("Logging Out \n")
                break
                
            else:
                print("Wrong Input ")
                wait()
                continue
            wait()

        else:
            wait()
            continue
    elif ch=="3":
          print("Good Bye ")
          exit()

    else:
        print("Wrong Input \n")
        continue
    wait()
