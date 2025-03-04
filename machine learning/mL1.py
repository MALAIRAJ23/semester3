input_data = [
    [100000, 5, 35],
    [75000, 4, 37],
    [65000, 3, 40],
    [80000, 6, 28],
    [125000, 3, 32]
]
output_data = [50020, 37520.5, 32521.5, 40017, 62571.5]

income = [row[0] for row in input_data]
num_members = [row[1] for row in input_data]
avg_age = [row[2] for row in input_data]
mean_income = sum(income) / len(income)
mean_mem = sum(num_members) / len(num_members)
mean_age = sum(avg_age) / len(avg_age)
mean_expense = sum(output_data) / len(output_data)

print("Mean of variables")
print("Mean of income:", mean_income, "\n",
      "Mean of number of members:", mean_mem, "\n",
      "Mean of average age:", mean_age, "\n",
      "Mean of expense:", mean_expense)

income_data = [i - mean_income for i in income]
num_members_data = [i - mean_mem for i in num_members]
avg_age_data = [i - mean_age for i in avg_age]

income_data1 = sum([(i - mean_income) ** 2 for i in income])
num_members_data1 = sum([(i - mean_mem) ** 2 for i in num_members])
avg_age_data1 = sum([(i - mean_age) ** 2 for i in avg_age])

cov_income_exp = sum(i * j for i, j in zip(income_data, output_data))
cov_mem_exp = sum(i * j for i, j in zip(num_members_data, output_data))
cov_age_exp = sum(i * j for i, j in zip(avg_age_data, output_data))

var_income = income_data1
var_mem = num_members_data1
var_age = avg_age_data1

b1 = cov_income_exp / var_income
b2 = cov_mem_exp / var_mem
b3 = cov_age_exp / var_age

b0 = mean_expense - (b1 * mean_income + b2 * mean_mem + b3 * mean_age)

cov_income_mem = sum(i * j for i, j in zip(income_data, num_members_data))
correl_income_mem = cov_income_mem / ((income_data1 * num_members_data1) ** 0.5)
print("Correlation between income and number of members:", correl_income_mem)

cov_mem_age = sum(i * j for i, j in zip(num_members_data, avg_age_data))
correl_mem_age = cov_mem_age / ((num_members_data1 * avg_age_data1) ** 0.5)
print("Correlation between number of members and average age:", correl_mem_age)

cov_age_income = sum(i * j for i, j in zip(avg_age_data, income_data))
correl_age_income = cov_age_income / ((avg_age_data1 * income_data1) ** 0.5)
print("Correlation between income and average age:", correl_age_income)

x1 = int(input("Enter the income: "))
x2 = int(input("Enter the number of members: "))
x3 = int(input("Enter the average age: "))

predicted_expense = b0 + (b1 * x1) + (b2 * x2) + (b3 * x3)

print("The expense for the family with provided data is predicted to be:", predicted_expense)

