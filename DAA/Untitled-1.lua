algorithm island count(matrix):
rows=len(matrix)
cols=len(matrix[0])
visited[rows][cols]=False
function dfs(r,c)
if r<0 or c<0 or matrix[r][c]==0 or visited [r][c]
return
visited[r][c]=true
dfs(r+1,c)
dfs(r-1,c)
dfs(r,c+1)
dfs(r,c-1)
dfs(r+1,c+1)
dfs(r+1,c-1)
dfs(r-1,c+1)
dfs(r-1,c-1)
island=0
boundisland=0
for row in matrix:
for cols in matrix:





























The provided function island_count(matrix) counts the number of islands in a 2D binary grid (matrix) where 1 represents land and 0 represents water. The function uses Depth First Search (DFS) to traverse the grid and identify distinct islands.

    Here's a breakdown of how this code works:
    
    Base Case: The function first checks if the matrix is empty. If it is, it returns 0 since there are no islands.
    
    Initialization:
    
    rows and cols store the dimensions of the matrix.
    visited is a 2D list initialized to False to keep track of which cells have been visited during the DFS.
    Depth First Search (DFS):
    
    The dfs(r, c) function explores all possible paths from a given cell (r, c).
    It checks bounds to ensure we stay within the grid and whether the current cell is land (1) and not yet visited.
    If the conditions are met, it marks the cell as visited and recursively calls dfs on all 8 neighboring cells (up, down, left, right, and diagonals).
    Counting Islands:
    
    The main loop goes through each cell in the grid. Whenever it finds an unvisited land cell, it calls dfs to mark the entire connected island and increments the island_count.
    Return Value: Finally, it returns the total number of islands found.
    
    Example Output
    Given the matrix:
    
    CopyReplit
    [
        [1, 1, 0, 0, 1],
        [1, 0, 0, 0, 1],
        [1, 0, 1, 1, 0],
        [0, 0, 0, 0, 0],
        [1, 0, 0, 0, 1]
    ]
    The output of print(island_count(matrix)) will be 5, since there are 5 distinct islands in the provided matrix.
    
    To run this code, you need a Python environment. You can paste this code into a Python file or a Jupyter notebook and execute it to see the output. If you have further questions or need additional explanations, feel free to ask!
