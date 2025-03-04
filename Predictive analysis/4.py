P1=[10,35,30,10,40]
Q1=[10,4,3,25,3]
P0=[5,35,15,20,40]
Q0=[25,10,15,20,5]
P1Q1=P0Q0=P1Q0=P0Q1=[]
for i in range(len(P1)):
    P1Q1.append(P1[i]*Q1[i])
    P0Q0.append(P0[i]*Q0[i])
    P1Q0.append(P1[i]*Q0[i])
    P0Q1.append(P0[i]*Q1[i])
print(f"Laspyere's index number: {(sum(P1Q1)/sum(P0Q0))*100}")
print(f"Paasche's index number: {(())*100}")
print(f"Fisher's index number: {(())*100}")
print(f"Marshall-Edgeworth's index number: {(())*100}")