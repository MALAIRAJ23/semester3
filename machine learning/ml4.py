import pandas as pd
data = {
    'Outlook': ['Sunny', 'Sunny', 'Overcast', 'Rainy', 'Rainy', 'Rainy', 'Overcast', 'Sunny', 
                'Sunny', 'Rainy', 'Sunny', 'Overcast', 'Overcast', 'Rainy'],
    'Temp': ['Hot', 'Hot', 'Hot', 'Mild', 'Cool', 'Cool', 'Cool', 'Mild', 
                'Cool', 'Mild', 'Mild', 'Mild', 'Hot', 'Mild'],
    'Humidity': ['High', 'High', 'High', 'High', 'Normal', 'Normal', 'Normal', 'High', 
                'Normal', 'Normal', 'Normal', 'High', 'Normal', 'High'],
    'Windy': ['False', 'True', 'False', 'False', 'False', 'True', 'True', 'False', 
                'False', 'False', 'True', 'True', 'False', 'True'], 
    'Play': ['No', 'No', 'Yes', 'Yes', 'Yes', 'No', 'Yes', 'No', 
                'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'No'] 
} 
df = pd.DataFrame(data) 
new_instance = {'Outlook': 'Sunny', 'Temp': 'Mild', 'Humidity': 'Normal', 'Windy': 'False'}
def calculate_probabilities(df, target, instance):
    probabilities = {} 
    for value in df[target].unique(): 
        subset = df[df[target] == value]  
        probabilities[value] = len(subset) / len(df) 
        for feature in instance:
            probabilities[value] *= len(subset[subset[feature] == instance[feature]]) / len(subset) 
    return probabilities
probs = calculate_probabilities(df, 'Play', new_instance)
prediction = max(probs, key=probs.get)
print(f"Prediction: {prediction}")