n = int(input("Enter number of items: "))
profits = []
weights = []
for i in range(n):
    p = int(input("Enter profit for item : "))
    w = int(input("Enter weight for item : "))
    profits.append(p)
    weights.append(w)
c = int(input("Enter capacity: "))
objects = []
for i in range(n):
    objects.append((profits[i], weights[i], profits[i] / weights[i]))
sorted_profit = sorted(objects, key=lambda x: x[0])  
sorted_weight = sorted(objects, key=lambda x: x[1])
sorted_ratio = sorted(objects, key=lambda x: x[2], reverse=True)
def knapsack_alg(s, c):
    solutionset = [0] * len(s)
    profit = 0
    w = c
    for i in range(len(s)):
        if s[i][1] <= w:
            solutionset[i] = 1
            w -= s[i][1]
            profit += s[i][0]
        else:
            portion = w / s[i][1]
            solutionset[i] = portion 
            profit += portion * s[i][0]
            break
    return profit, solutionset
feasible1 = knapsack_alg(sorted_profit, c)
optimal = knapsack_alg(sorted_ratio, c)

print("Feasible Solution:-profits in ascending order", feasible1)
print("Optimal Solution:-ratio of p and w in descending order", optimal)