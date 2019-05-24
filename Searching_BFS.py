from update_file import update,render
import pickle
import os
import msvcrt as m
def wait():
    print("\nEnter to continue .... ")
    m.getch()

'''BFS (G, s)                   //Where G is the graph and s is the source node
      let Q be queue.
      Q.enqueue( s ) //Inserting s in queue until all its neighbour vertices are marked.

      mark s as visited.
      while ( Q is not empty)
           //Removing that vertex from queue,whose neighbour will be visited now
           v  =  Q.dequeue( )

          //processing all the neighbours of v  
          for all neighbours w of v in Graph G
               if w is not visited 
                        Q.enqueue( w )             //Stores w in Q to further visit its neighbour
                        mark w as visited.
'''

def destroy(Id,V):
    #print(len(V)," relevant people appeared in search ")
    Id.visited=False
    for i in V:
        i.visited=False
    

def bfs1(x,Id):
    A=[]
    V=[]
    A.append(Id)
    Id.visited=True
    while(A!=[]):
        v=A.pop(0)
        following=render(v.following)
        for i in following:
            if i.id not in V:
                V.append(i.id)
                A.append(i)
                i.visited=True
                #print(i.name)
                if x.lower() in i.name.lower() or x ==str(i.number):
                    os.system('cls')
                    i.display_details()
                    if check(i,render(Id.followers)):
                        print("\n** Following You \n")
                    while True:
                        print("\n1. Follow ")
                        print("2. Search next ")
                        print("3. End Search \n")
                        ch4=input("Enter your choice ")
                        if ch4=="1":
                            if check(i,render(Id.following)):
                                print("\nAlready following \n")
                                continue
                            Id.following.append(i.id)
                            i.followers.append(Id.id)
                            # Make changes in file for pk and i
                            update(Id)
                            update(i)
                            
                            print("\nSuccesfully followed \n")
                            wait()
                            break
                            #destroy(Id,V)
                            #return
                        elif ch4=="2":
                            break
                        elif ch4=="3":
                            #destroy(Id,V)
                            return
                        else:
                            print("Wrong Input ")
                            wait()
                            continue
    else:
        #destroy(Id,V)
        brute(x,Id,V)

def check(obj,V):
    for i in V:
        if obj.id==i.id:
            return 1
    return 0
def brute(x,Id,V):
    users=[]
    try:
        with open("Users.txt","rb") as f:
            while True:
                obj=pickle.load(f)
                if obj.id==Id.id or obj.id in V:
                    continue
                users.append(obj)
    except:
        pass
    for i in users:
        if x.lower() in i.name.lower() or x ==str(i.number):
            os.system('cls')
            i.display_details()

            while True:
                print("\n1. Follow ")
                print("2. Search next ")
                print("3. End Search \n")
                ch4=input("Enter your choice ")
                if ch4=="1":
                    Id.following.append(i.id)
                    i.followers.append(Id.id)
                    # Make changes in file for pk and i
                    update(Id)
                    update(i)
                    
                    print("\nSuccesfully followed \n")
                    wait()
                    break

                elif ch4=="2":
                    break
                elif ch4=="3":
                    return
                else:
                    print("Wrong Input ")
                    wait()
                    continue
    else:
        print("No more people found ")
        wait()
    

    

    
def search(x,Id):
    print("Searching ",x,"")
    bfs1(x,Id)
