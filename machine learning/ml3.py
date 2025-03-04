#Implement and demonstrate the Candidate-Elimination algorithm 
# to output a description of the set of all hypotheses consistent 
# with the following Japanese Economy Car training examples
training_data = [
    ["japan", "honda", "blue", "1980", "economy", "positive"],
    ["japan", "toyota", "green", "1970", "sports", "negative"],
    ["japan", "toyota", "blue", "1990", "economy", "positive"],
    ["usa", "chrysler", "red", "1980", "economy", "negative"],
    ["japan", "honda", "white", "1980", "economy", "positive"],
    ["japan", "toyota", "green", "1980", "economy", "positive"]]
S = ["null", "null", "null", "null", "null"]  
G = [["?", "?", "?", "?", "?"]]  
def is_consistent(hypothesis, instance):
    for i in range(len(hypothesis)):
        if hypothesis[i] != "?" and hypothesis[i] != instance[i]:
            return False
    return True
for instance in training_data:
    attributes = instance[:-1]  
    label = instance[-1]  
    if label == "positive":
        for i in range(len(S)):
            if S[i] == "null":
                S[i] = attributes[i]
            elif S[i] != attributes[i]:
                S[i] = "?"
                G = [g for g in G if is_consistent(g, attributes)]
    else:  
        new_G = []
        for g in G:
            if is_consistent(g, attributes):
                for i in range(len(g)):
                    if g[i] == "?":
                        for value in set([row[i] for row in training_data]):
                            if value != attributes[i]:
                                new_hypothesis = g[:]
                                new_hypothesis[i] = value
                                new_G.append(new_hypothesis)
            else:
                new_G.append(g)
        G = new_G
        G = [g for g in G if any(g[i] == "?" or g[i] == S[i] for i in range(len(g)))]
print("Specific Hypothesis (S):", S)
print("General Hypothesis (G):", G)