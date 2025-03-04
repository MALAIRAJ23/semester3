# Dataset
data = [
    ['A', 'Yes', 'A', 'Yes'],   
    ['A', 'No', 'A', 'Yes'],    
    ['C', 'Yes', 'B', 'No'],    
    ['B', 'Yes', 'A', 'Yes'],  
    ['A', 'No', 'A', 'Yes'],    
    ['B', 'No', 'B', 'No']     
]
features = [row[:-1] for row in data]  
target = [row[-1] for row in data]    

hypothesis = 'pi'

for i in range(len(features)):
    if target[i] == 'Yes':  
        if hypothesis=='pi': 
            hypothesis = features[i]
        else:
            for j in range(len(features[i])):
                if hypothesis[j] != features[i][j]:
                    hypothesis[j] = '?'  
                    print(hypothesis)

if hypothesis:
    print("Most Specific Hypothesis:", hypothesis)
else:
    print("No positive examples found.")