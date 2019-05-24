import pickle
from Class import Person
import os
import msvcrt as m
def wait():
    print("\nEnter to continue .... ")
    m.getch()


def register():
    name=   input("Enter Your Name         - ")
    number= input("Enter your Phone Number - ")
    try:
        number=int(number)
    except:
        print("\nNumber must be a Number \n")
        return -1
    desc=   input("Enter your description  - ")
    obj=Person(name,number,desc)
    # append in file
    with open("Users.txt","ab") as f:
        pickle.dump(obj,f)
    print("\nRegistration Succesful ")
    print("\nYour User ID is ",obj.id)
    wait()

def login():
    Id=     input("Enter you ID            - ")
    try:
        # search in file
        with open("Users.txt","rb") as f:
            while True:
                obj=pickle.load(f)
                #print(obj.name)
                if obj.id==int(Id):
                    return obj
    except:
        print("Wrong ID \n" )
        return 0
    
