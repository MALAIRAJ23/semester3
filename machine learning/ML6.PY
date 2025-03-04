import numpy as np

square_footage = np.array([1500,1800, 1200, 2400, 2000, 1300, 1700, 2200, 1600, 2500])
number_of_bedrooms = np.array([3, 4, 2, 4, 3, 2, 3, 5, 3, 5])
age_of_house = np.array([10, 5, 20, 2, 15, 25, 8, 3, 12, 1])
distance_to_city_center = np.array([5, 3, 7, 2, 6, 10, 4, 1, 8, 1])
local_school_rating = np.array([8, 9, 7, 10, 8, 6, 9, 10, 7, 10])
house_price = np.array([300000, 450000, 250000, 600000, 350000, 200000, 400000, 550000, 320000, 700000])


X = np.column_stack((np.ones(len(square_footage)),square_footage,number_of_bedrooms,age_of_house,distance_to_city_center,local_school_rating))


Y = house_price


XtX = np.dot(X.T, X) 

XtY = np.dot(X.T, Y) 

XtX_inv = np.linalg.inv(XtX)
print(XtX_inv)  
beta = np.dot(XtX_inv, XtY)  
print("Multiple linear regression equation:")
print(f"y = {beta[0]:.2f} + {beta[1]:.2f} + {beta[2]:.2f}*x2 + {beta[3]:.2f}*x3 + {beta[4]:.2f}*x4 + {beta[5]:.2f}*x5")
print("y = ",(beta[0]) + (beta[1])*1800 + (beta[2])*4 + (beta[3])*5 + (beta[4])*3 + (beta[5])*9)