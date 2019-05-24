import pickle
import os

def update(Id):
    updating(Id)
    '''for i in Id.followers:
        updating(i)
    for i in Id.following:
        updating(i)'''

def updating(Id):
    f2=open("temp.txt","wb")
    try:
        with open("Users.txt","rb") as f:
            while True:
                obj=pickle.load(f)
                if obj.id==Id.id:
                    pickle.dump(Id,f2)
                    continue
                pickle.dump(obj,f2)
    except:
        f2.close()
        
    os.remove("Users.txt")
    os.rename("temp.txt","Users.txt")

def render(ids):
    A=[]
    if ids==[]:
        #print("khali h bhai ")
        return []
    ids=set(ids)
    try:
            
        with open("Users.txt","rb") as f:
            while True:
                obj=pickle.load(f)
                if obj.id in ids:
                    ids-={obj.id}
                    A.append(obj)

    except:
        return A
        
                
