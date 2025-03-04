def consistent(h, instance):
    """Check if hypothesis h is consistent with the given instance."""
    for i in range(len(h)):
        if h[i] != "?" and h[i] != instance[i]:
            return False
    return True

def generalize_G(S, G, instance):
    """Specialize G by replacing '?' with specific attribute values except the negative instance."""
    G_new = [] 
    for g in G:
        if consistent(g, instance):
            for i in range(len(g)):
                if g[i] == "?": 
                    for value in set(row[i] for row in data):
                        if value != instance[i]:  
                            new_hypothesis = g[:] 
                            new_hypothesis[i] = value 
                            G_new.append(new_hypothesis)
        else: 
            G_new.append(g) 
    return G_new 

def candidate_elimination(data):
    """Candidate Elimination Algorithm implementation."""
    num_attributes = len(data[0]) - 1  
    S = ["null"] * num_attributes  
    G = [["?"] * num_attributes]  

    for row in data:
        attributes = row[:-1]
        label = row[-1]

        if label == "positive":
            for i in range(num_attributes):
                if S[i] == "null":  
                    S[i] = attributes[i]
                elif S[i] != attributes[i]:
                    S[i] = "?"  
            G = [g for g in G if consistent(g, attributes)]  
            
        else:  
            G = generalize_G(S, G, attributes)

    return S, G

# Example Dataset
data = [
    ["japan", "honda", "blue", "1980", "economy", "positive"],
    ["japan", "toyota", "green", "1970", "sports", "negative"],
    ["japan", "toyota", "blue", "1990", "economy", "positive"],
    ["usa", "chrysler", "red", "1980", "economy", "negative"],
    ["japan", "honda", "white", "1980", "economy", "positive"],
    ["japan", "toyota", "green", "1980", "economy", "positive"]
]

S_final, G_final = candidate_elimination(data)

print("Final Specific Hypothesis (S):", S_final)
print("Final General Hypotheses (G):", G_final)