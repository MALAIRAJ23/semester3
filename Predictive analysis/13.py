import matplotlib.pyplot as plt
x=[1.0,1.1,1.2,1.3,1.4,1.5,1.6,1.7,1.8]
y=[8.1,7.8,8.5,9.8,9.5,8.9,8.6,10.2,9.3]
n=len(x)
sum_x=sum(x)
sum_y=sum(y)
sq_x=[i*i for i in x]
sum_sq_x=sum(sq_x) 
xy=[i*j for i,j in zip(x,y)]
sum_xy=sum(xy)
a=((sum_y*sum_sq_x)-(sum_x*sum_xy))/((n*sum_sq_x)-(sum_x**2))
b=((n*sum_xy)-(sum_x*sum_y))/((n*sum_sq_x)-(sum_x**2))
print(f"Linear Regression Line: y={b}x+{a}")
temp_ip=1.75
converted_sugar=(b*temp_ip)+a
print(f"The mean amount of sugar when temp is 1.75 is: {converted_sugar}")
y_pred=[a+b*xi for xi in x]
residuals=[yi-y_pred_i for yi,y_pred_i in zip(y,y_pred)]
plt.scatter(x,residuals,color="m",marker="o",s=30)
plt.xlabel("Temperature")
plt.ylabel("Residuals")
plt.title("Residuals vs Temperature")
plt.show()
