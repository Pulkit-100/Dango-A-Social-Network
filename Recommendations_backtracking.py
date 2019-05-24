from update_file import update,render
import os
import msvcrt as m
def wait():
    print("\nEnter to continue .... ")
    m.getch()
def check(obj,V):
    for i in V:
        if obj.id==i.id:
            return 1
    return 0

def destroy(Id,V):
    Id.visited=False
    for i in V:
        i.visited=False
def track(Id,pk,R,V):
    for i in render(Id.following):
        #print(Id.name," -  ",i.name)
        if i.id==pk.id and check(Id,render(pk.following))==0:
            print("HH")
            R.append(Id)
            continue
        if i.id in V:
            continue
        '''if i.id==pk.id and check(Id,render(pk.following))==0:
            print("HH")
            R.append(Id)
            continue'''
        #i.visited=True
        V.append(i.id)
        track(i,pk,R,V)
        if len(R)>=10:
            return
    return

            
def recommendations(Id):
    R=[]
    V=[]
    track(Id,Id,R,V)
    #destroy(Id,V)
    if R==[]:
        print("\nNo Recommendations \n")
        return
    for i in R:
        while True:
            os.system('cls')
            i.display_details()
            print("\n")
            print("1. Follow ")
            print("2. Next Recommendation ")
            print("3. Exit Recommendations \n")
            ch4=input("Enter your choice ")
            if ch4=="1":
                Id.following.append(i.id)
                i.followers.append(Id.id)
                update(Id)
                update(i)
                print("\nSuccesfully followed \n")
                wait()

            elif ch4=="2":
                break
            elif ch4=="3":
                return
            else:
                print("Wrong Input \n")
                wait()
                continue
    else:
        print("\nNo more Recommendations \n")
            
