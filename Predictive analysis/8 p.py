
locations = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y1 = [35, 35, 40, 10, 6, 20, 35, 35, 35, 30]
y2 = [3.5, 4.9, 30.0, 2.8, 2.7, 2.8, 4.6, 10.9, 8.0, 1.6]
y3 = [2.80, 2.70, 4.38, 3.21, 2.73, 2.81, 2.88, 2.90, 3.28, 3.20]
n=len(locations)

y1_mean=sum(y1)/len(y1)
y2_mean=sum(y2)/len(y2)  
y3_mean=sum(y3)/len(y3)
mean_vector=[y1_mean, y2_mean, y3_mean]


y11=[i*i for i in y1]
s11=(sum(y11)-n*y1_mean**2)/(n-1)
y22=[i*i for i in y2]
s22=(sum(y22)- n*y2_mean**2)/(n-1)
y33=[i*i for i in y3]
s33=(sum(y33)-n*y3_mean**2)/(n-1)
y12=[i*j for i,j in zip(y1,y2)]
s12=(sum(y12)- n*y1_mean*y2_mean)/(n-1)
y23=[i*j for i,j in zip(y2,y3)]
s23=(sum(y23)- n*y2_mean*y3_mean)/(n-1)
y13=[i*j for i,j in zip(y1,y3)]
s13=(sum(y13)- n*y1_mean*y3_mean)/(n-1)
s31=s13
s21=s12
s32=s23
covariance_matrix=[[s11,s12,s13],
                   [s21,s22,s23],
                   [s31,s32,s33]]
print("Mean vector")
print(mean_vector)
print("Covariance matrix")
print(covariance_matrix)