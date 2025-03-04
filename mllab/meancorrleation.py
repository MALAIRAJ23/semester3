def calculate_mean(values):
    total = 0 
    count = 0 
    for value in values: 
        total += value 
        count += 1 
    return total / count 
mean_income = calculate_mean(income) 
mean_family_members = calculate_mean(family_members) 
mean_average_age = calculate_mean(average_age) 
# 2. Correlation between independent features 
def calculate_correlation(x, y):
    n = len(x) 
    mean_x = calculate_mean(x) 
    mean_y = calculate_mean(y) 
    numerator = 0 
    denominator_x = 0 
    denominator_y = 0 
    for i in range(n):
        numerator += (x[i] - mean_x) * (y[i] - mean_y)
        denominator_x += (x[i] - mean_x) ** 2 
        denominator_y += (y[i] - mean_y) ** 2 
    denominator = (denominator_x ** 0.5) * (denominator_y ** 0.5)
    return numerator / denominator if denominator != 0 else 0
correlation_income_family = calculate_correlation(income, family_members)
correlation_income_age = calculate_correlation(income, average_age)
correlation_family_age = calculate_correlation(family_members, average_age)
# 3. Predict expenses for (150000, 4, 30)
# Linear regression formula: y = b1*x1 + b2*x2 + b3*x3
b = 0.5  # coefficient for all independent variables
x1, x2, x3 = 150000, 4, 30
predicted_expenses = b * (x1 + x2 + x3)
# Output results 
print("Mean of Income:", mean_income)
print("Mean of Family Members:", mean_family_members)
print("Mean of Average Age:", mean_average_age) 
print("Correlation between Income and Family Members:", correlation_income_family) 
print("Correlation between Income and Average Age:", correlation_income_age) 
print("Correlation between Family Members and Average Age:", correlation_family_age) 
print("Predicted Expenses for (150000, 4, 30):", predicted_expenses)