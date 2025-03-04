def island_count(matrix):
    if not matrix:
        return 0

    rows = len(matrix)
    cols = len(matrix[0])
    visited = [[False for _ in range(cols)] for _ in range(rows)]

    def dfs(r, c):
        if r < 0 or c < 0 or r >= rows or c >= cols or matrix[r][c] == 0 or visited[r][c]:
            return
        
        
        visited[r][c] = True

        dfs(r + 1, c)   # Down
        dfs(r - 1, c)   # Up
        dfs(r, c + 1)   # Right
        dfs(r, c - 1)   # Left
        dfs(r + 1, c + 1) # Down-Right
        dfs(r + 1, c - 1) # Down-Left
        dfs(r - 1, c + 1) # Up-Right
        dfs(r - 1, c - 1) # Up-Left

    island_count = 0

    for r in range(rows):
        for c in range(cols):
            if matrix[r][c] == 1 and not visited[r][c]:
                dfs(r, c)
                island_count += 1

    return island_count


matrix = [
    [1, 1, 0, 0, 1],
    [0, 0, 0, 0, 1],
    [1, 0, 1, 0, 0],
    [1, 0, 1, 0, 0]
]

print(island_count(matrix))  