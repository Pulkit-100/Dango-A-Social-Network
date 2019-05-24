import pickle
from update_file import render
import os
import msvcrt as m
def wait():
    print("\nEnter to continue .... ")
    m.getch()
class Person:
    
    def __init__(self,name="",number=None, desc=""):
        p=None
        try:
            with open("ID.txt","r") as f:
                p=f.read()
                p=int(p)+1
                #print(p,"H")
        except:
            p=1
        with open("ID.txt","w") as f:
            f.write(str(p))
        self.id=p #None
        self.name=name
        self.number=number
        self.desc=desc
        self.followers=[]
        self.following=[]
        self.visited=False

    def get_followers_count(self):
        return len(self.followers)
    def get_following_count(self):
        return len(self.following)
    def display_details(self):
        print("\n\n Name      - ",self.name,"\n",
              "Number    - ",self.number ,"\n\n",
              "Description \n\n",self.desc,"\n\n",
              "Followers - ",self.get_followers_count(),"\n",
              "Following - ",self.get_following_count(),"\n\n")
    def display_followers(self):
        print("Followers Count - ",self.get_followers_count())
        A=render(self.followers)
        for i in A:
            wait()
            os.system('cls')
            print("Followers Count - ",self.get_followers_count())
            i.display_details()
            self.mutual_followers(i)
            self.mutual_following(i)
            
    def display_following(self):
        print("Following Count - ",self.get_following_count())
        A=render(self.following)
        #print(len(A))
        for i in A:
            wait()
            os.system('cls')
            print("Followers Count - ",self.get_followers_count())
            i.display_details()
            self.mutual_followers(i)
            self.mutual_following(i)
    def mutual_followers(self,obj):
        P=[]
        #A=render(self.followers)
        #B=render(obj.followers)
        for i in self.followers:
            if i in obj.followers:
                P.append(i)
        print("Total ",len(P)," mutual followers ")
        for i in render(P):
            print(i.name,end="  ")
        print()

    def mutual_following(self,obj):
        P=[]
        #A=render(self.following)
        #B=render(obj.following)        
        for i in self.following:
            if i in obj.following:
                P.append(i)
        print("Total ",len(P)," mutual following ")
        for i in render(P):
            print(i.name,end="  ")
        print()


'''
P=Person("Pulkit",7838011378,"PK")

A=Person("Aka",9999999999,"aa")

AA=Person("Akanshita",5435923490,"Heya !")

P.following.append(A.id)
A.followers.append(P.id)

A.following.append(AA.id)
AA.followers.append(A.id)



f=open("Users.txt","wb")
pickle.dump(P,f)
pickle.dump(A,f)
pickle.dump(AA,f)
f.close()
print(P.display_following())
print("Done")
'''

