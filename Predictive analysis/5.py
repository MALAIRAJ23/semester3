n=int(int(input("Enter no.of items:")))
P1=[]
P0=[]
for i in range(1,n+1):
    x=int(input("Enter value for current year:"))
    P1.append(x)
    y=int(input("Enter value for base year:"))
    P0.append(y)
price_index=(sum(P1)/sum(P0))*100
print("The price index value calculated using simple aggregate method is:",price_index)