x=[77,50,71,72,81,94,96,99,67]
y=[82,66,78,34,47,85,99,99,68]
n=len(x)
x_mean=sum(x)/n
y_mean=sum(y)/n
xy_diff=0
x2_diff=0
for i in range(n):
    xy_diff+=((x[i]-x_mean)*(y[i]-y_mean))
    x2_diff+=((x[i]-x_mean)**2)
b1=xy_diff/x2_diff
b0=y_mean-(b1*x_mean)
#y=b0+b1x
print(f"Equation line: y={b0}+{b1}*x")
#prediction
X=int(input("Enter x value:"))
Y=b0+b1*X
print("Predicted value:",Y)