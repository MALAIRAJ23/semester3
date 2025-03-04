y1=[0.81,0.95,0.94,1.04,1.00,0.76,0.91,1.10,0.99,0.78,0.90,0.73]
y2=[80,97,105,90,90,86,100,85,97,91,87,78]
x1=[356,289,319,356,323,381,350,301,379,296,353,306]
x2=[124,117,143,199,240,157,221,186,142,131,221,178]
x3=[55,76,105,108,143,165,119,105,98,94,53,66]
n=len(y1)
#mean
y1_mean=sum(y1)/n
y2_mean=sum(y2)/n
x1_mean=sum(x1)/n
x2_mean=sum(x2)/n
x3_mean=sum(x3)/n
mean_vector=[[y1_mean,y2_mean],[x1_mean,x2_mean,x3_mean]]
print(f"Mean Vector:{mean_vector}")
#covariance
def Cov(x,y,mean_x,mean_y):
    return ((sum((xi-mean_x)*(yi-mean_y)) for xi,yi in zip(x,y))/(n-1))
Sy11=Cov(y1,y1,y1_mean,y1_mean)
Sy12=Cov(y1,y2,y1_mean,y2_mean)
Sy22=Cov(y2,y2,y2_mean,y2_mean)
Syx11=Cov(y1,x1,y1_mean,x1_mean)
Syx12=Cov(y1,x2,y1_mean,x2_mean)
Syx13=Cov(y1,x3,y1_mean,x3_mean)
Syx21=Cov(y2,x1,y2_mean,x1_mean)
Syx22=Cov(y2,x2,y2_mean,x2_mean)
Syx23=Cov(y2,x3,y2_mean,x3_mean)
Sx11=Cov(x1,x1,x1_mean,x1_mean)
Sx12=Cov(x1,x2,x1_mean,x2_mean)
Sx13=Cov(x1,x3,x1_mean,x3_mean)
Sx22=Cov(x2,x2,x2_mean,x2_mean)
Sx23=Cov(x2,x3,x2_mean,x3_mean)
Sx33=Cov(x3,x3,x3_mean,x3_mean)
Cov_matrix=[[Sy11,Sy12,Syx11,Syx12,Syx13],[Sy12,Sy22,Syx21,Syx22,Syx23],[Syx11,Syx21,Sx11,Sx12,Sx13],[Syx12,Syx22,Sx12,Sx22,Sx23],[Syx13,Syx23,Sx13,Sx23,Sx33]]
print("Covariance Matrix:")
for i in Cov_matrix:
    print(i)