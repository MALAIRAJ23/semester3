data = [
    ['A', 'Yes', 'A', 'Yes'],
    ['B', 'No', 'A', 'Yes'],
    ['C', 'Yes', 'B', 'No'],
    ['B', 'Yes', 'A', 'Yes'],
    ['A', 'No', 'A', 'Yes'],
    ['B', 'No', 'B', 'No'],        
] 
attributes = [row[:-1] for row in data] 
labels = [row[-1] for row in data] 
def find_s_algorithm(attributes, labels):
    hypothesis = [None] * len(attributes[0])  # null hypothesis
    for i in range(len(labels)): 
        label = labels[i] 
        if label == 'Yes': 
            example = attributes[i] 
            if hypothesis == [None] * len(attributes[0]):
                hypothesis = example[:]  
            else:
                for j in range(len(hypothesis)):
                    if hypothesis[j] != example[j]:
                        hypothesis[j] = '?'  
    return hypothesis 
most_specific_hypothesis = find_s_algorithm(attributes, labels)
print("Most Specific Hypothesis:", most_specific_hypothesis)