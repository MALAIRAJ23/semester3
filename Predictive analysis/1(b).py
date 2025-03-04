n=int(input("Enter the number of days when cars visited the garage:"))
l=[]
for i in range(1,n+1):
    j=float(input("Enter the number of cars:"))
    l.append(j)
#mean
mean=sum(l)/n
print("The mean for the first",n," days is:",mean)
next_day=int(input("Enter the number of  cars that visited on the following day:"))
l.append(next_day)
new_mean=sum(l)/n+1
if mean<new_mean:
    print("The mean value increased on the next day is:",new_mean)
elif mean>new_mean:
    print("the mean value decreased on the next day is:",new_mean)
else:
    print("The mean value remained the same on the next day")