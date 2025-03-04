data = [
    ["Sunny", "Hot", "High", "False", "No"], ["Sunny", "Hot", "High", "True", "No"], ["Overcast", "Hot", "High", "False", "Yes"],
    ["Rainy", "Mild", "High", "False", "Yes"], ["Rainy", "Cool", "Normal", "False", "Yes"], ["Rainy", "Cool", "Normal", "True", "No"], 
    ["Overcast", "Cool", "Normal", "True", "Yes"], ["Sunny", "Mild", "High", "False", "No"], ["Sunny", "Cool", "Normal", "False", "Yes"], 
    ["Rainy", "Mild", "Normal", "False", "Yes"], ["Sunny", "Mild", "Normal", "True", "Yes"], ["Overcast", "Mild", "High", "True", "Yes"], 
    ["Overcast", "Hot", "Normal", "False", "Yes"], ["Rainy", "Mild", "High", "True", "No"]
]
input_eg = ["Sunny", "Cool", "Normal", "True"]
output_eg="No"
ycount = sum(1 for record in data if record[4] == "Yes")
ncount = sum(1 for record in data if record[4] == "No")
totcount = len(data)
probab_yes = ycount / totcount
probab_no = ncount / totcount 
def likelihood(index_f, value_f, class_d):
    class_count = sum(1 for record in data if record[index_f] ==value_f and record[4] == class_d)
    t_class_count = ycount if class_d == "Yes" else ncount
    return class_count / t_class_count if t_class_count > 0 else 0 
probab_class_y = 1
probab_class_n = 1
for i in range(len(input_eg)):
    probab_class_y *= likelihood(i, input_eg[i], "Yes")  
    probab_class_n *= likelihood(i, input_eg[i], "No")
prediction = "Yes" if probab_class_y > probab_class_n else "No"  
print("Prediction for :", input_eg)
print(prediction)
print(probab_class_y)
print(probab_class_n)
if prediction!=output_eg:
    print("Risk:",1-probab_class_y)
else:
    print("Risk:",0)
