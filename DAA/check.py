def isSafe(grid, i, j, visited):
    rows, cols = len(grid), len(grid[0])
    return (0 <= i < rows and 0 <= j < cols and 
            not visited[i][j] and grid[i][j] == 1)

def DFS(grid, i, j, visited):
    # Mark the current cell as visited
    visited[i][j] = True

    # Move in 4 directions (Up, Down, Left, Right)
    if isSafe(grid, i - 1, j, visited):  # Up
        DFS(grid, i - 1, j, visited)
    if isSafe(grid, i + 1, j, visited):  # Down
        DFS(grid, i + 1, j, visited)
    if isSafe(grid, i, j - 1, visited):  # Left
        DFS(grid, i, j - 1, visited)
    if isSafe(grid, i, j + 1, visited):  # Right
        DFS(grid, i, j + 1, visited)

def countIslands(grid):
    if not grid:
        return 0

    rows, cols = len(grid), len(grid[0])
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    count = 0

    for i in range(rows):
        for j in range(cols):
            if not visited[i][j] and grid[i][j] == 1:
                DFS(grid, i, j, visited)
                count += 1  # Increase island count

    return count

# Example grid
graph = [[1, 1, 0, 0, 0],
        [0, 0, 0, 0, 1],
        [1, 1, 0, 1, 1],
        [0, 0, 0, 1, 0],
        [1, 1, 1, 0, 1]]

print("Number of islands is:", countIslands(graph))
