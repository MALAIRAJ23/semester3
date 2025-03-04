#def Multistagegraph()
def menu():
    e=int(input("Enter no.of edges:"))
    v=int(input("Enter no.of vertices:"))
    E=[]
    print("Enter path:")
    for i in range(v):
        u,w,wt=map(int,input().split())
        E.append((u,w,wt))
    print("Menu:")
    print("1.Forward Method")
    print("2.Backward Method")
    print("3.Tableau Method")
    print("4.Exiting!")
    for i in E:
        print(i)
menu()