def allpaths(cost, n):
    A = [[cost[i][j] for j in range(n)] for i in range(n)]
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if A[i][k] == float('inf') or A[k][j] == float('inf'):
                    continue
                A[i][j] = min(A[i][j], A[i][k] + A[k][j])
    
    return A
cost = [
    [0, 4,11],
    [6, 0, 2],
    [3, float('inf'), 0]
]
n = 3
results = allpaths(cost, n)
print("All Pairs Shortest Path:")
for row in results:
    print(row)