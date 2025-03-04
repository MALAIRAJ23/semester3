def find(parent, u):
    if parent[u] != u:
        parent[u] = find(parent, parent[u])  
    return parent[u]

def union(parent, rank, u, v):
    root_u = find(parent, u)
    root_v = find(parent, v)

    if root_u == root_v:
        return False 
    
    
    if rank[root_u] > rank[root_v]:
        parent[root_v] = root_u
    elif rank[root_u] < rank[root_v]:
        parent[u] = root_v
    else:
        parent[root_v] = root_u
        rank[root_u] += 1
    return True

def has_cycle_kruskal(matrix):
    n = len(matrix)  
    edges = []

    
    for i in range(n):
        for j in range(i + 1, n): 
            if matrix[i][j] != 0:  
                edges.append((i, j, matrix[i][j]))

    edges.sort(key=lambda x: x[2]) 
    parent = list(range(n))
    rank = [0] * n
    edge_count = 0  

    for u, v, _ in edges:
        if edge_count == n - 1: 
            break
        if union(parent, rank, u, v):  
            edge_count += 1

    return edge_count < n - 1 


graph_matrix = [
    [0, 10, 5, 0],
    [10, 0, 15, 0], 
    [5, 15, 0, 20], 
    [0, 0, 20, 0]   
]

print(has_cycle_kruskal(graph_matrix)) 
