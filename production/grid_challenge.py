def gridChallenge(grid):
    sorted_grid = []
    for row in grid:
        sorted_row = "".join(sorted(row))
        sorted_grid.append(sorted_row)
        
    num_rows = len(sorted_grid)
    num_cols = len(sorted_grid[0])
    
    for col in range(num_cols):
        for row in range(1, num_rows):
            if sorted_grid[row][col] < sorted_grid[row-1][col]:
                return "NO"
                
    return "YES"