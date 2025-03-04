l_ind=[60,72,55,81,70,63,58,85,67,77]
l_dep=[100000,90000,140000,110000,120000,120000,150000,120000,170000,150000]

#mean
mean_x=0
sum_x=0
for i in l_ind:
    sum_x+=i 
mean_x=sum_x/len(l_ind)
mean_y=0
sum_y=0
for i in l_dep:
    sum_y+=i 
mean_y=sum_y/len(l_dep)
#coefficient1
diff_l_x=[]
for i in l_ind:
    j=i-mean_x
    diff_l_x.append(j)
sum_diff_x=0
for j in diff_l_x:
    sum_diff_x+=j
diff_l_y=[]
for i in l_dep:
    j=i-mean_y
    diff_l_y.append(j)
sum_diff_y=0
for j in diff_l_y:
    sum_diff_y+=j
multiply_l=[]
for i,j in zip(l_ind,l_dep):
    multiply_l.append(i*j)
sum_multiply=0
for i in multiply_l:
    sum_multiply+=i
square_list=[]
for i in diff_l_x:
    square_list.append(i*i)
square_sum=0
for i in square_list:
    square_sum+=i

b1=sum_multiply/square_sum

#coefficient0
b0=mean_y-(b1*mean_x)

#y-value
num=int(input("enter the number of records for which ticket fare has to be predicted:"))
for i in range(0,num):
    x=int(input("Enter the number of passengers:"+str(i)+"th record"))
    y=b0+(b1*x)
    print("The ticket fare woul be:",y,"for",str(i),"th record")