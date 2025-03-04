def find(parent, node):
    if parent[node] != node:
        parent[node] = find(parent, parent[node])
    return parent[node]

def union(parent, node1, node2):
    root1 = find(parent, node1)
    root2 = find(parent, node2)

    if root1 == root2:
        return False
    
    parent[root2] = root1
    return True

def has_cycle(matrix):
    n = len(matrix)
    edges = []

    for i in range(n):
        for j in range(i + 1, n):
            if matrix[i][j] != 0:
                edges.append((i, j))

    parent = list(range(n))

    for u, v in edges:
        if not union(parent, u, v):
            return True
    
    return False

graph = [
    [0, 1, 0, 1],  
    [1, 0, 1, 0],  
    [0, 1, 0, 1],  
    [1, 0, 1, 0]   
]

print(has_cycle(graph))
